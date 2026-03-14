from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://isms_user:change_this_password_in_production@isms-core-postgres:5432/isms_db"
    db_pool_size: int = 20
    db_max_overflow: int = 10
    db_echo: bool = False

    # Redis
    redis_url: str = "redis://:change_this_redis_password@isms-core-redis:6379/0"

    # Auth
    secret_key: str = "change_this_secret_key_in_production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    refresh_token_expire_minutes: int = 10080  # 7 days

    # Paths (read-only mounts)
    isms_data_path: str = "/app/isms-data"
    assessments_path: str = "/app/assessments"
    datasets_path: str = "/app/datasets"
    framework_path: str = "/app/isms-framework"
    operational_path: str = "/app/isms-operational"
    privacy_path: str = ""   # ISO 27701:2025 content mount (/app/isms-privacy)
    cloud_path: str = ""     # ISO 27018:2025 content mount (/app/isms-cloud)
    cache_path: str = "/app/cache"
    uploads_path: str = "/app/uploads"

    @property
    def extra_paths(self) -> str:
        """Comma-separated non-ISMS product paths for importers."""
        return ",".join(p for p in [self.privacy_path, self.cloud_path] if p)

    # AI
    anthropic_api_key: str = ""
    ai_model: str = "claude-sonnet-4-6"

    # OpenSearch
    opensearch_url: str = "http://isms-core-opensearch:9200"

    # Platform URL (used in email links)
    platform_url: str = "http://localhost:3000"

    # Email / SMTP
    # Leave MAIL_HOST unset (empty) to disable email — all send calls become no-ops.
    # Dev:  point at mailhog  (MAIL_HOST=isms-core-mailhog  MAIL_PORT=1025)
    # Prod: point at internal Postfix relay or SmtpToGraphBridge on port 25
    mail_host: str = ""
    mail_port: int = 1025
    mail_from: str = "isms-core@localhost"
    mail_from_name: str = "ISMS CORE"
    mail_timeout: int = 10  # seconds

    # Admin bootstrap (set these in .env to seed/override the admin user on startup)
    admin_email: str = "admin@isms-core.dev"
    admin_password: str = "admin123"

    # App
    debug: bool = False
    log_level: str = "INFO"
    cors_origins: str = "http://localhost:3000,http://localhost:8000"

    model_config = {"env_file": ".env", "case_sensitive": False}


@lru_cache()
def get_settings() -> Settings:
    return Settings()
