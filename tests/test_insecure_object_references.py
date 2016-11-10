from funcs import setsecuritylevel, loadconfig
import re

config = loadconfig()


def test_lfi_source_code_viewer():
    s = setsecuritylevel(seclevel=config['seclevel'])
    badinput = "./../../../../etc/passwd"
    url = "%s/index.php?page=source-viewer.php" % config['url']
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "page=%s&phpfile=show-log.php&source-file-viewer-php-submit-button=View+File" % badinput
    r = s.post(url, data, headers=headers)
    passwd = re.compile(r"/bin/sh")
    assert passwd.search(r.text) is None
