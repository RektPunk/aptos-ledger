from enum import Enum


class AccountEndpoint(Enum):
    ACCOUNT_RESOURCES: str = "https://fullnode.mainnet.aptoslabs.com/v1/accounts/{address}/resources"

