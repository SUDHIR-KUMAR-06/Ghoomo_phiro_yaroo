import logging

logger = logging.getLogger(__name__)


class NotificationService:
    def notify_new_inquiry(self, inquiry_id: str) -> None:
        logger.info("TODO: implement email, WhatsApp, or CRM notification for inquiry %s", inquiry_id)
