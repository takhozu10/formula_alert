# Find Formula

This repo is an example of how I setup an automated alert to find my baby his formulas. The code is hardcoded with https://abbottstores.com and Similac Sensitive version of Pro and 360 product family and looking for 32oz only, you will need to adjust the Selenium part of the code using XPATH or CSS-selector to identify the correct item on the webpage. Use this as an example and make adjust to your baby's favorite formulas. 

This script is using yagmail to send status of formula availability if it's IN STOCK.

Python Library used in this code.
-Selenium
-Yagmail
-Keyring


## Setup Script using Crontab on macOS
1. Create a throwaway gmail account which Yagmail will use to send alert email to your real email address. After you create, navigate to Manage Google Account > Security > Less Secure App Access. Enable this setting. 
2. Download and install Python version 3.8 or higher, This is due to an issue with keyring you will encounter with older version of Python
3. Download "main.py"
4. Place the main.py in a directory you want to run from. 
5. Open terminal and navigate to the directory with main.py
6. Create venv by running the following command where <dir> is the directory path to the main.py:
```
python3.10 -m venv /<dir>/venv
```
7. Activate venv:
```
source /<dir>/venv/bin/activate
```
8. Once you activate pip install Selenium, keyring, and yagmail.
```
pip install selenium
pip install keyring
pip install yagmail
```
9. Start Python console and setup yagmail so that username and password to your gmail account is setup in Apple keychain. 
```
python
```
```python
import yagmail
yamail.register('username', 'password')
```
10. Use a text editor and edit send_email_alert() function. 
  Replace 'fromemail@gmail.com' portion with your sending email. 
  Replace 'toemail@gmail.com' protion with recepient email. If you have second one replace 'toemail2@gmail.com'. Otherwise, you can remove the list bracket. 
11. Setup crontab job to run every 15 minutes. Make sure to add source command before running so that it would enble the venv.
```
  crontab -e
```
```
  */15 * * * * /usr/bin/env bash -c 'cd /<dir>/ && source /<dir>/venv/bin/activate && python ./main.py
```

FEATURE REQUESTs
- Add ability to check Walmart, Target for formula availability.
- Add ability to check different brands. 
