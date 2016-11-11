from funcs import setsecuritylevel, loadconfig, auth

config = loadconfig()


# Response header "Logged-In-User" displays what user is logged in.
# This test ensures that you cannot manipulate the uid cookie on the client side
def test_uid_cookie_manipulation():
    s = setsecuritylevel(seclevel=config['seclevel'])

    s = auth(config['validuser'], config['validpass'], s)
    url = "%s/index.php" % config['url']
    r = s.get(url)
    actual_user = (r.headers["Logged-In-User"])
    s.cookies.set('uid', '1', domain=config["domain"], path=config["path"])
    r = s.get(url)

    assert actual_user == r.headers["Logged-In-User"]
