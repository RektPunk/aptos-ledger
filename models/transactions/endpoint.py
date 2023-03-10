from models.metadata.endpoint import Endpoint


class TransactionsEndpoint(Endpoint):
    ACCOUNT_TRANSACTIONS: str = (
        "https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/transactions"
    )
