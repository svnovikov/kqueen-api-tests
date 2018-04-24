import requests
from urllib.parse import urljoin


def parse_response(func):
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        try:
            decoded_json = resp.json()
        except Exception:
            decoded_json = None
        return resp.status_code, decoded_json
    return wrapper


class KqueenAPIclient(object):

    def __init__(self, url, **kwargs):
        self.url = url
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')

    def _make_url(self, endpoint=None):
        if endpoint:
            return urljoin(self.url, endpoint)
        return self.url

    @parse_response
    def _get(self, endpoint=None, **kwargs):
        return requests.get(self._make_url(endpoint), **kwargs)

    @parse_response
    def _post(self, endpoint=None, **kwargs):
        return requests.post(self._make_url(endpoint), **kwargs)

    @parse_response
    def _put(self, endpoint=None, **kwargs):
        return requests.put(self._make_url(endpoint), **kwargs)

    @parse_response
    def _delete(self, endpoint=None, **kwargs):
        return requests.delete(self._make_url(endpoint), **kwargs)
