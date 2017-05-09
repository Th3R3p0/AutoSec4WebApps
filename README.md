# AutoSec4WebApps

This repository contains some sample pytest scripts to run against a Mutillidae 1 web server. You can use these scripts to become familiar with the pytest framework and help you visualize some different ways to test for vulnerabilities which you may have found in your application in the past. 

To use: 

1. git clone https://github.com/Th3R3p0/AutoSec4WebApps.git
2. download and run Metasploitable 2 which contains Mutillidae and other vulnerable web apps - https://sourceforge.net/projects/metasploitable/files/Metasploitable2/
3. modify config.json file to include the correct URL, domain and path of your Mutillidae web server
4. create a virtualenv and activate it
5. pip install -r requirements.txt
6. from AutoSec4WebApps directory run: pytest tests/test_*.py
7. You can modify the config.json seclevel to level 0, 1 or 5. Level 5 is the most secure level of mutillidae and Level 0 is the most insecure. All tests will fail on level 0 and all but 1 test will pass on level 5.
