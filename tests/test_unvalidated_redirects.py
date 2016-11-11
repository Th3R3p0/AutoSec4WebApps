from funcs import setsecuritylevel, loadconfig
import re

config = loadconfig()


# this test checks for a redirect. this redirect is not a 301 or 302,
# but rather a http-equiv="refresh" located at the end of the body
def test_unvalidated_redirect():
    s = setsecuritylevel(seclevel=config['seclevel'])
    redirect_url = "http://www.th3r3p0.com"
    url = "%s/index.php?page=redirectandlog.php&forwardurl=%s" % (config['url'], redirect_url)
    r = s.get(url, allow_redirects=False)
    redirect = re.compile(r"%s" % redirect_url)
    assert redirect.search(r.text) is None

test_unvalidated_redirect()
