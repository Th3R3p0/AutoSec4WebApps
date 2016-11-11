from funcs import setsecuritylevel, loadconfig

config = loadconfig()

# this is a best practice check. this can be used out of the box with any URL.
# this check is assuming that the http requests should ALWAYS redirect to https
def test_http_to_https():
    s = setsecuritylevel(seclevel=config['seclevel'])

    # use the url from config, but turn it into an insecure request if using https
    url = "%s/index.php" % config['url']
    if url.startswith("https://"):
        insecure_url = url.replace("https://", "http://")
    elif url.startswith("http://"):
        insecure_url = url
    else:
        raise NameError("URL is not valid - must start with http:// or http://")

    r = s.get(insecure_url, allow_redirects=False)
    # make sure a redirection occurs
    print(r.status_code)
    assert r.status_code == 301 or r.status_code == 302
    if r.status_code == 301 or r.status_code == 302:
        # make sure the redirection is to an https protocol
        if "Location" in r.headers:
            https_redirect = r.headers["Location"].startswith("https://")
            assert https_redirect is True
        else:
            raise NameError("Redirect location did not appear in the headers")
