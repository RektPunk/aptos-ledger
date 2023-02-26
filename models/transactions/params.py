from typing import Optional
from models.metadata.params import Params


class AccountTransactionsParams(Params):
    address: str
    limit: Optional[int]
    start: Optional[str]
