import os

from blueforge.api import Api

__version__ = '0.0.1'
WHATSIT_SDK_PY_ROOT = os.path.dirname(os.path.abspath(__file__))


def get_service(service_name):
    return Api(service_name)
