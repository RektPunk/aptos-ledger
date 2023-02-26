from typing import Any, List, Dict, Tuple, Union
import requests
from models.account.endpoint import AccountEndpoint
from models.transactions.endpoint import TransactionsEndpoint
from models.metadata.params import Params
from utils.variables import HEADERS


def validate_addresses(addresses: Union[List[str], str])-> List[str]:
    if isinstance(addresses, str):
        addresses = [addresses]
    return addresses


def _transform_url(url: str, params: Params) -> Tuple[str, Params]:
    if AccountEndpoint.isin(url) or TransactionsEndpoint.isin(url):
        url = url.format(address=params.address)
        params.address = None
    return url, params


def get_response(url: str, params: Params) -> Dict[str, Any]:
    _url, _params = _transform_url(url, params)
    _response = requests.get(
        url=_url,
        params=_params,
        headers=HEADERS,
    )
    if _response.status_code == 200:
        return _response.json()
    else:
        raise Exception("Invalid response")
