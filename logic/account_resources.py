from typing import List, Dict, Union
from models.account.endpoint import AccountEndpoint
from models.account.params import AccountResourcesParams
from utils.get_data import get_response, validate_addresses


def get_account_resources(
    addresses: Union[List[str], str],
) -> Dict[str, List[Dict]]:
    addresses = validate_addresses(addresses)
    responses = {}
    for address in addresses:
        _params = AccountResourcesParams(
            address=address,
        )
        _response = get_response(
            url=AccountEndpoint.ACCOUNT_RESOURCES.value, params=_params
        )
        responses.update({address: _response})
    return responses
