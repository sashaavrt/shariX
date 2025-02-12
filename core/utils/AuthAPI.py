'''
That class provides the ability to authenticate an application account through the
API and store these authentication tokens.

Modules using the API should log in ShariX system using this class.
'''

import requests

from core.settings import API_URL


class AuthAPI:
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._token = None
        self._headers = None

    def _create_token(self):
        try:
            response = requests.post(
                f"{API_URL}/auth/token/login/",
                {
                    "phone_number": self._login,
                    "password": self._password
                }
            )
            self._token = response.json()["auth_token"]
        except requests.exceptions.ConnectionError:
            print("\033[31m" + f"{self.__class__.__name__}: Can't connect to the API." + "\033[0m")
        except KeyError:
            print("\033[31m" + f"{self.__class__.__name__}: Incorrect login data." + "\033[0m")

    @property
    def token(self):
        if self._token is None:
            self._create_token()
        return self._token

    @property
    def headers(self):
        if self._token is None:
            self._create_token()
            self._headers = {'Authorization': f'Token {self._token}'}
        return self._headers
