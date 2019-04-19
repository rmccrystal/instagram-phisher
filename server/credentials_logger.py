from typing import *
from dataclasses import dataclass


@dataclass
class Credential:
    username: str
    password: str
    ip_addr: str


credential_list = list()


def log_credentials(username: str, password: str, ip_addr=None):
    credential_list.append(Credential(username, password, ip_addr))
    print('\n----------HIT----------\n'
          'Username: \'{0}\'\n'
          'Password: \'{1}\'\n'
          '-----------------------\n'
          .format(username, password))


def get_credentials() -> List[Credential]:
    return credential_list