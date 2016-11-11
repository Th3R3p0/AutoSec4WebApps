import requests
import json


# Todo: look into the open config file location
def loadconfig():
    with open('../config.json') as json_data_file:
        config = json.load(json_data_file)
    return config

config = loadconfig()


# This function only exists for DVWA. This would not be needed in a real world application
# This function returns a session with a security level - security levels are mapped to a jsessionid
def setsecuritylevel(seclevel=0):
    if seclevel == 0:
        s = requests.Session()
        return s
    if seclevel == 1:
        s = requests.Session()
        s.get("%s/index.php" % config['url'])
        s.get("%s/index.php?do=toggle-security" % config['url'], allow_redirects=False)
        return s
    if seclevel == 5:
        s = requests.Session()
        s.get("%s/index.php" % config['url'], allow_redirects=False)
        s.get("%s/index.php?do=toggle-security" % config['url'], allow_redirects=False)
        s.get("%s/index.php?do=toggle-security" % config['url'], allow_redirects=False)
        return s


# This function returns the python session so that the cookies can be used for future requests
def auth(user, pwd, s=None):
    if s is None:
        s = requests.Session()
    data = "username=%s&password=%s&login-php-submit-button=Login" % (user, pwd)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    s.post("%s/index.php?page=login.php" % config['url'], data, headers=headers)
    return s
