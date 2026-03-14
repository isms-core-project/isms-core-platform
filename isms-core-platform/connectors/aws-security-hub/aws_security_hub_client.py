"""AWS Security Hub API client.

Uses boto3 to query AWS Security Hub findings, standards, and insights.
Authentication supports:
  - Explicit credentials (access_key_id + secret_access_key)
  - IAM role assumption (role_arn)
  - Instance profile / environment credentials (if running on EC2/ECS)

Environment variables:
  AWS_ACCESS_KEY_ID      — AWS access key ID (optional if using instance profile)
  AWS_SECRET_ACCESS_KEY  — AWS secret access key
  AWS_DEFAULT_REGION     — AWS region, e.g. eu-west-2

Requires: boto3>=1.34 (add to requirements.txt or install separately)
"""

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)


def _get_boto3_client(service: str, cfg: dict) -> Any:
    """Build a boto3 client with credentials from cfg or environment."""
    try:
        import boto3
    except ImportError as exc:
        raise ImportError(
            "boto3 is required for the AWS Security Hub connector. "
            "Add boto3>=1.34 to requirements.txt."
        ) from exc

    region = cfg.get('region') or os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
    access_key = cfg.get('access_key_id') or os.environ.get('AWS_ACCESS_KEY_ID', '')
    secret_key = cfg.get('secret_access_key') or os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    role_arn = cfg.get('role_arn') or os.environ.get('AWS_ROLE_ARN', '')

    session_kwargs: dict = {"region_name": region}

    if role_arn:
        # Assume the specified IAM role
        sts = boto3.client(
            'sts',
            region_name=region,
            **({"aws_access_key_id": access_key, "aws_secret_access_key": secret_key}
               if access_key and secret_key else {}),
        )
        assumed = sts.assume_role(RoleArn=role_arn, RoleSessionName="ISMS-CORE-Connector")
        creds = assumed["Credentials"]
        session_kwargs.update({
            "aws_access_key_id": creds["AccessKeyId"],
            "aws_secret_access_key": creds["SecretAccessKey"],
            "aws_session_token": creds["SessionToken"],
        })
    elif access_key and secret_key:
        session_kwargs.update({
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
        })
    # Otherwise fall through to instance profile / env credentials

    return boto3.client(service, **session_kwargs)


class AWSSecurityHubClient:
    def __init__(self, **cfg) -> None:
        self._cfg = cfg
        self._client = None

    def _hub(self):
        if self._client is None:
            logger.info("Creating AWS Security Hub boto3 client...")
            self._client = _get_boto3_client('securityhub', self._cfg)
        return self._client

    def get_findings_summary(self) -> dict:
        """Return active Security Hub findings grouped by severity.

        Paginates through all findings with RecordState=ACTIVE.
        Returns counts by severity label: CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL.
        """
        logger.info("Fetching Security Hub findings...")
        hub = self._hub()
        sev_counts: dict[str, int] = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
            "INFORMATIONAL": 0,
        }
        total = 0
        paginator = hub.get_paginator('get_findings')
        pages = paginator.paginate(
            Filters={
                "RecordState": [{"Value": "ACTIVE", "Comparison": "EQUALS"}],
                "WorkflowStatus": [
                    {"Value": "NEW", "Comparison": "EQUALS"},
                    {"Value": "NOTIFIED", "Comparison": "EQUALS"},
                ],
            },
            PaginationConfig={"MaxItems": 10000, "PageSize": 100},
        )
        try:
            for page in pages:
                for finding in page.get("Findings", []):
                    sev_label = finding.get("Severity", {}).get("Label", "INFORMATIONAL")
                    sev_counts[sev_label] = sev_counts.get(sev_label, 0) + 1
                    total += 1
        except Exception as e:
            logger.warning("Error paginating findings: %s", e)

        logger.info("Security Hub findings: %d total", total)
        return {"total": total, "by_severity": sev_counts}

    def get_standards_summary(self) -> list[dict]:
        """Return subscribed Security Hub standards with enabled/disabled control counts."""
        logger.info("Fetching Security Hub standards subscriptions...")
        hub = self._hub()
        try:
            resp = hub.describe_standards_subscriptions()
            standards = resp.get("StandardsSubscriptions", [])
            result: list[dict] = []
            for std in standards:
                arn = std.get("StandardsArn", "")
                sub_arn = std.get("StandardsSubscriptionArn", "")
                status = std.get("StandardsStatus", "")
                # Get control counts for this standard
                passed = 0
                failed = 0
                disabled = 0
                try:
                    ctrl_paginator = hub.get_paginator('describe_standards_controls')
                    for ctrl_page in ctrl_paginator.paginate(StandardsSubscriptionArn=sub_arn):
                        for ctrl in ctrl_page.get("Controls", []):
                            ctrl_status = ctrl.get("ControlStatus", "")
                            if ctrl_status == "ENABLED":
                                comp = ctrl.get("ComplianceStatus", "")
                                if comp == "PASSED":
                                    passed += 1
                                else:
                                    failed += 1
                            else:
                                disabled += 1
                except Exception as e:
                    logger.warning("Could not fetch controls for %s: %s", arn, e)
                total_controls = passed + failed + disabled
                score_pct = round(100 * passed / total_controls, 1) if total_controls > 0 else 0.0
                result.append({
                    "standards_arn": arn,
                    "status": status,
                    "passed": passed,
                    "failed": failed,
                    "disabled": disabled,
                    "total_controls": total_controls,
                    "compliance_score_pct": score_pct,
                })
            logger.info("Fetched %d subscribed standards", len(result))
            return result
        except Exception as e:
            logger.warning("Could not fetch standards subscriptions: %s", e)
            return []

    def get_insights(self, limit: int = 10) -> list[dict]:
        """Return top Security Hub managed insights."""
        logger.info("Fetching Security Hub insights...")
        hub = self._hub()
        try:
            resp = hub.get_insights(MaxResults=limit)
            insights = resp.get("Insights", [])
            logger.info("Fetched %d insights", len(insights))
            return insights
        except Exception as e:
            logger.warning("Could not fetch insights: %s", e)
            return []
