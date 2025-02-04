from core.ledgers.schemas import BaseLedgerOperation


class AppLedgerOperation(BaseLedgerOperation):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
