from models.metadata.params import Params


class AccountResourcesParams(Params):
    address: str
    ledger_version: str
    limit: int
    start: str
