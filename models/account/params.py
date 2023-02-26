from typing import Optional
from models.metadata.params import Params


class AccountResourcesParams(Params):
    address: str
    ledger_version: Optional[str]
    limit: Optional[int]
    start: Optional[str]
