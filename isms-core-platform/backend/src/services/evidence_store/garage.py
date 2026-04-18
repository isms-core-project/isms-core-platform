"""Garage S3 file storage helper — used alongside OpenSearchEvidenceStore."""
from __future__ import annotations

import logging
from typing import IO

import boto3
from botocore.client import Config

from src.core.config import get_settings

logger = logging.getLogger(__name__)


def _client():
    s = get_settings()
    return boto3.client(
        "s3",
        endpoint_url=s.garage_endpoint,
        aws_access_key_id=s.garage_access_key,
        aws_secret_access_key=s.garage_secret_key,
        config=Config(signature_version="s3v4"),
        region_name="garage",
    )


class GarageService:
    """Upload / download / delete files in Garage S3."""

    def upload(self, bucket: str, key: str, fileobj: IO[bytes], content_type: str = "application/octet-stream") -> str:
        """Upload fileobj to bucket/key. Returns the S3 key."""
        _client().upload_fileobj(fileobj, bucket, key, ExtraArgs={"ContentType": content_type})
        logger.debug("uploaded s3://%s/%s", bucket, key)
        return key

    def download_url(self, bucket: str, key: str, expires: int = 3600) -> str:
        """Return a presigned GET URL valid for `expires` seconds."""
        return _client().generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": key},
            ExpiresIn=expires,
        )

    def delete(self, bucket: str, key: str) -> None:
        _client().delete_object(Bucket=bucket, Key=key)
        logger.debug("deleted s3://%s/%s", bucket, key)

    def evidence_key(self, org_id: str, doc_id: str, filename: str) -> str:
        return f"{org_id}/{doc_id}/{filename}"
