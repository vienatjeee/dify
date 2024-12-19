from api.libs.helper import VerificationCodeManager
from api.models.account import Account


class VerificationService:

    @classmethod
    def generate_account_deletion_verification_code(cls, account: Account) -> str:
        return VerificationCodeManager.generate_verification_code(
            account=account,
            code_type="account_deletion",
        )

    @classmethod
    def verify_account_deletion_verification_code(cls, account: Account, verification_code: str) -> bool:
        return VerificationCodeManager.verify_verification_code(
            account=account,
            code_type="account_deletion",
            verification_code=verification_code,
        )
