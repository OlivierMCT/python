import re
import subprocess
import datetime
import getpass
import platform


def getUserName() -> str:
    user = input("[Username (press enter to system username)]> ")
    if(len(user) == 0):
        user = getpass.getuser()
    return user


def getPassword() -> str:
    pwd = ""
    while True:
        pwd = getpass.getpass("[Password]> ")
        if(len(pwd) > 0):
            break
        print("please enter your password\n")
    return pwd


def getMachineInfo() -> str:
    return "{} ({})".format(platform.node(), platform.system())


def getDateTimeInfo() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def getIpAdresses() -> list:
    pattern = br"Adresse IPv4.*: (?P<ip>([0-9]{1,3}\.){3}[0-9]{1,3})"
    output = subprocess.check_output("ipconfig")
    return [m["ip"].decode() for m in re.finditer(pattern, output)]


def getLog(username: str, isSuccess: bool) -> str:
    return "[{3}] {1:<7} for {0} on {2} with ips {4}".format(
        username,
        "SUCCESS" if isSuccess else "FAIL",
        getMachineInfo(),
        getDateTimeInfo(),
        getIpAdresses()
    )


username = getUserName()
password = getPassword()
isAuthenticated = password == "azerty"
print(getLog(username, isAuthenticated))
if(isAuthenticated):
    print("👋 Bonjour", username)
else:
    print("😡 Echec de l'authentification")
