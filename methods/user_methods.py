import requests
import url


class UserMethods:

    @staticmethod
    def registration_user(body):
        return requests.post(f'{url.MAIN_PAGE_URL}{url.REGISTRATION}', json=body)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{url.MAIN_PAGE_URL}{url.DELETE}', headers={'Authorization': token})
