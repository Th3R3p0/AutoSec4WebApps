from funcs import setsecuritylevel, loadconfig
from bs4 import BeautifulSoup
import re

config = loadconfig()


# use beautiful soup to extract the csrf token
def get_csrf_token(r):
    soup = BeautifulSoup(r.text, "html.parser")
    inputs = soup.find_all("input")
    for i in inputs:
        if i["name"] == "csrf-token":
            csrftoken = i["value"]
    return csrftoken


# ensures that csrf tokens are different
def test_csrf_blog_post():
    s = setsecuritylevel(seclevel=config['seclevel'])
    url = "%s/index.php?page=add-to-your-blog.php" % config['url']
    r = s.get(url)
    csrf_token_one = get_csrf_token(r)
    r = s.get(url)
    csrf_token_two = get_csrf_token(r)
    assert csrf_token_one != csrf_token_two


