from models.meta.params import Params


class AccountTransactionsParams(Params):
    address: str
    limit: int
    start: str
