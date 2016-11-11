from funcs import setsecuritylevel, loadconfig
import re

config = loadconfig()


# Check to see if the text "PHP Credits" appears on the page
# Can't check for "PHP Version" because the text appears in the footer
def test_check_for_phpinfo_page():
    s = setsecuritylevel(seclevel=config['seclevel'])
    url = "%s/index.php?page=phpinfo.php" % config['url']
    r = s.get(url)
    php = re.compile(r"PHP Credits")
    assert php.search(r.text) is None
