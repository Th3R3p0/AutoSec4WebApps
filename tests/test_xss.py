from funcs import loadconfig
from funcs import setsecuritylevel
import re

config = loadconfig()


# Test for Reflected (type one) XSS on the "DNS Lookup" page
def test_xss_dns_lookup():
    s = setsecuritylevel(seclevel=config['seclevel'])
    badinputs = ['%3Cscript%3Ealert%281%29%3C%2Fscript%3E']
    # todo: fix the following:
    # the regex will only search for the one badinput listed above. I tried to parse the badinputs, but the parenthesis
    #    needed to be escaped.
    for badinput in badinputs:
        url = "%s/index.php?page=dns-lookup.php" % config['url']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = "target_host=%s&dns-lookup-php-submit-button=Lookup+DNS" % badinput
        r = s.post(url, data, headers=headers)
        xss = re.compile("<script>alert\(1\)</script>")
        # This will error out if a badinput triggers the sqli error text to be displayed
        assert xss.search(r.text) is None
