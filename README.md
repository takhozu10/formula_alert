# Formula availability status alert

This repo is an example of how I setup an automated alert to find our baby's formulas. The code is hardcoded with https://abbottstores.com and Similac Sensitive version of Pro and Total Care 360 product family, looking for 32oz only. You will need to adjust the Selenium part of the code using XPATH or CSS-selector to identify the correct item on the webpage. Use this as an example and make adjust to your baby's favorite formulas. 
If you need to find the status of out of order product, you can take the similar approach show here. If you want to learn more about Selenium, I recommend taking this Udemy course: https://www.udemy.com/course/elegant-browser-automation-with-python-and-selenium/

This script is using yagmail to send status of formula availability if it's IN STOCK.

Python Library used in this code.
- Selenium
- Yagmail
- Keyring


## Setup Script using Crontab on macOS
1. Create a throwaway gmail account which Yagmail will use to send alert emails to your real email address. After you create, navigate to Manage Google Account > Security > Less Secure App Access. Enable this setting. 
2. Download and install Python version 3.8 or higher, This is due to an issue with keyring you will encounter with older version of Python
3. Download the chromedriver that matches the version of Chrome browser you have installed on the computer. https://chromedriver.chromium.org/downloads
4. Create a symbolic link to the Chromedriver in /usr/local/bin/. I recommend running the driver at least once since macOS will most likely block them.
```
ln -s /<path>/<to>/<chromedriver> /usr/local/bin/chromedriver
```
6. Download "main.py"
7. Place the main.py in a directory you want to run from. 
8. Open terminal and navigate to the directory with main.py
9. Create venv by running the following command where <dir> is the directory path to the main.py:
```
python3.10 -m venv /<dir>/venv
```
10. Activate venv:
```
source /<dir>/venv/bin/activate
```
11. Once you activate pip install Selenium, keyring, and yagmail.
```
pip install selenium
pip install keyring
pip install yagmail
```
12. Start Python console and setup yagmail so that username and password to your gmail account is setup in Apple keychain. 
```
python
```
```python
import yagmail
yamail.register('username', 'password')
```
13. Use a text editor and edit send_email_alert() function. 
  Replace 'fromemail@gmail.com' portion with your sending email. 
  Replace 'toemail@gmail.com' protion with recepient email. If you have a second email adress to send the alert, replace 'toemail2@gmail.com'. Otherwise, you can remove the list bracket. 
14. Setup a crontab job to run every 15 minutes. Make sure to add source command before running so that it would enble the venv.
```
  crontab -e
```
```
  PATH=/usr/local/bin
  */5 * * * * cd /<dir>/ && source /<dir>/venv/bin/activate && python ./main.py >> ~/cron.log 2>&1
```
15. Lastly, you will need to add cron to allow Full Disk access. This can be done by going to System Preferences > Security & Privacy > Privacy > Full Disk Access. Unlock by providing the admin access. Click the + icon, press Shift + Command + G to navigate to /usr/sbin/cron. Select cron and cron will be added to the Full Disk Access to peform the above task without any permissions issue. 

FEATURE REQUESTs
- Add ability to check Walmart, Target for formula availability.
- Add ability to check different brands. 
