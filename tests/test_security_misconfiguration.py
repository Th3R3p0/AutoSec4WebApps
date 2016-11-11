from funcs import setsecuritylevel, loadconfig
from bs4 import BeautifulSoup

config = loadconfig()


def test_post_vs_get_form():
    s = setsecuritylevel(seclevel=config['seclevel'])
    url = "%s/index.php?page=user-info.php" % config['url']
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    inputs = soup.find_all("form")
    # check and make sure there is only one form
    assert len(inputs) == 1
    # check to make sure the method is sending values over POST and not a GET request
    assert inputs[0]["method"] == "POST"
