
from datetime import timedelta

from extensions.ext_database import db

from api.configs import dify_config
from api.libs.helper import get_current_datetime
from api.models.account import AccountDeletionLog


class AccountDeletionLogService:
    @classmethod
    def create_account_deletion_log(cls, email, reason):
        account_deletion_log = AccountDeletionLog()
        account_deletion_log.email = email
        account_deletion_log.reason = reason
        account_deletion_log.updated_at = get_current_datetime()
        return account_deletion_log

    @classmethod
    def email_in_freeze(cls, email):
        log = db.session.query(AccountDeletionLog).filter(email=email).order_by(AccountDeletionLog.created_at.desc()).first()
        if not log:
            return False
        # check if the account is in freeze period
        if log.created_at + timedelta(days=dify_config.ACCOUNT_REGISTER_COOLDOWN_DAYS) > get_current_datetime():
            return True
        return False
