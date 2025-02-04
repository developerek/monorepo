# monorepo/core/ledgers/exceptions.py

class InsufficientBalanceError(Exception):
    pass


class DuplicateTransactionError(Exception):
    pass
