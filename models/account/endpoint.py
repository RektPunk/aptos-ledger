from models.meta.endpoint import Endpoint


class AccountEndpoint(Endpoint):
    ACCOUNT_RESOURCES: str = (
        "https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/resources"
    )
