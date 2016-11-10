from funcs import loadconfig
from funcs import setsecuritylevel
import re

config = loadconfig()


# Test for SQLi on the "View your details" page
def test_view_your_details():
    s = setsecuritylevel(seclevel=config['seclevel'])
    badinputs = ['%27', '%22']
    # You could configure the sqli test to check for a 500 error instead of specific text on a page
    sqli_error = re.compile(r"Error: Failure is always an option and this situation proves it")
    for badinput in badinputs:
        url = "%s/index.php?page=user-info.php&username=%s&password=&user-info-php-submit-button=View+Account+Details"\
              % (config['url'], badinput)
        r = s.get(url)
        # This will error out if a badinput triggers the sqli error text to be displayed
        assert sqli_error.search(r.text) is None


