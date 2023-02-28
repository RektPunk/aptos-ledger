from typing import List, Dict, Union
from models.transactions.endpoint import TransactionsEndpoint
from models.transactions.params import AccountTransactionsParams
from utils.get_data import get_response, validate_addresses


def get_account_transactions(
    addresses: Union[List[str], str],
) -> Dict[str, List[Dict]]:
    addresses = validate_addresses(addresses)
    responses = {}
    for address in addresses:
        _params = AccountTransactionsParams(
            address=address,
        )
        _response = get_response(
            url=TransactionsEndpoint.ACCOUNT_TRANSACTIONS.value, params=_params
        )
        responses.update({address: _response})
    return responses
