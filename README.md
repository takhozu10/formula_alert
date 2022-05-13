# Find Formula

This repo is an example of how I setup an automated alert to find my baby his formulas. The code is hardcoded with https://abbottstores.com and Similac Sensitive version of Pro and 360 product family and looking for 32oz only, you will need to adjust the Selenium part of the code using XPATH or CSS-selector to identify the correct item on the webpage. Use this as an example and make adjust to your baby's favorite formulas. 

This script is using yagmail to send status of formula availability if it's IN STOCK.

Python Library used in this code.
-Selenium
-Yagmail
-Keyring

FEATURE REQUESTs
- Add ability to check Walmart, Target for formula availability.
- Add ability to check different brands. 
