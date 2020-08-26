import paramiko


def main():
    ip = "192.168.0.56"
    username = "msfadmin"
    password = "msfadmin"

    client_policy = paramiko.AutoAddPolicy()

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(client_policy)

    client.connect(ip, username=username, password=password)
    print(client)


if __name__ == "__main__":
    main()
