from enum import Enum


class TransactionsEndpoint(Enum):
    ACCOUNT_TRANSACTIONS: str = "https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/transactions"

