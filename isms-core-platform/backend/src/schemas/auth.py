from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


class MfaVerifyRequest(BaseModel):
    mfa_token: str
    code: str  # 6-digit TOTP or XXXX-XXXX backup code


class MfaLoginResponse(BaseModel):
    mfa_required: bool = True
    mfa_token: str


class MfaSetupResponse(BaseModel):
    secret: str
    otpauth_uri: str
    qr_data_uri: str  # base64 PNG data URI for QR code display


class MfaEnableRequest(BaseModel):
    code: str  # must verify before enabling


class MfaEnableResponse(BaseModel):
    backup_codes: list[str]  # shown once — user must copy these


class MfaDisableRequest(BaseModel):
    code: str  # must verify current TOTP to disable


class MfaBackupCodesResponse(BaseModel):
    backup_codes: list[str]  # shown once — user must copy these
