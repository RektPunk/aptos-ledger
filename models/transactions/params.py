from models.metadata.params import Params


class AccountTransactionsParams(Params):
    address: str
    limit: int
    start: str
