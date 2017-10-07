from json import loads

import requests

from whatsitsdk.util import file


class Api(object):
    def __init__(self, service_name):
        self.__raw_json = file.get_latest_api_json_file(service_name)
        if self.__raw_json:
            for method in self.__raw_json['api']:
                Api.__create_dynamic_method(self.__raw_json['meta']['endpoint'], method)
        else:
            raise Exception('The {} service does not exist.'.format(service_name))

    @classmethod
    def __create_dynamic_method(cls, endpoint, method_obj):
        def request_http(self, *args, **kwargs):
            method = method_obj['method']
            url = (endpoint + method_obj['uri']).format(*args)
            params = {}
            print(url)
            for param in method_obj['params']:
                if param['name'] in kwargs:
                    params[param['name']] = kwargs[param['name']]

            if method == 'PUT':
                resp = requests.put(url=url, json=params, timeout=60)
            elif method == 'POST':
                resp = requests.post(url=url, params=params, timeout=60)
            else:
                resp = requests.get(url=url, params=params, timeout=60)

            return loads(resp.text)

        request_http.__name__ = method_obj['name']
        setattr(cls, request_http.__name__, request_http)
