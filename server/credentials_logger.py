from typing import *
from dataclasses import dataclass


@dataclass
class Credential:
    username: str
    password: str


credential_list = list()


def log_credentials(username: str, password: str):
    credential_list.append(Credential(username, password))
    print(username, password)


def get_credentials() -> List[Credential]:
    return credential_list