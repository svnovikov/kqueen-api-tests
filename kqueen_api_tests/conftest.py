import pytest
import yaml

from kqueen_api_tests.client import KqueenAPIclient
from kqueen_api_tests.utils import get_abspath


@pytest.fixture(autouse=True, scope='session')
def client():
    with open(get_abspath(__file__, "./config.yaml")) as f:
        config = yaml.load(f)
    return KqueenAPIclient(config['url'],
                           username=config.get('username'),
                           password=config.get('password'))
