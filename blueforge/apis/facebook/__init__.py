import json

import requests

from blueforge.apis.facebook.message import RequestDataFormat


class FacebookMessageException(Exception):
    pass


class CreateFacebookApiClient(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def send_message(self, message):
        req = requests.post(url='https://graph.facebook.com/v2.6/me/messages?access_token=%s' % self.access_token,
                            data=json.dumps(message.get_data()),
                            headers={'Content-Type': 'application/json'})
        if req.status_code != 200:
            raise FacebookMessageException("Can't send the message to facebook api server")

        return req.json()

    def __send_action(self, recipient_id, action):
        return self.send_message(RequestDataFormat(recipient=recipient_id, sender_action=action))

    def set_typing_on(self, recipient_id):
        return self.__send_action(recipient_id, 'typing_on')

    def set_typing_off(self, recipient_id):
        return self.__send_action(recipient_id, 'typing_off')

    def set_mark_seen(self, recipient_id):
        return self.__send_action(recipient_id, 'mark_seen')
