from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import keyring
import yagmail


def formula_stock_status(product_fam):
    '''
    Run Selenium to automate navigating Abbott Store to find stock_status of 32oz Ready to Feed formula of specified
    product family.
    :param product_fam: Specify product family. Example: Similac 360 Total Care, Similac Pro-Advance
    :return: return stock status. Example: "IN STOCK" "OUT OF STOCK"
    '''
    browser = webdriver.Chrome()
    browser.get("https://abbottstore.com/")
    browser.implicitly_wait(10)
    similac_menu_path = "//*[text()= 'Similac']"
    sim_pro_sen_path = f"//a[contains(text(), '{product_fam}')]"
    similac_menu = browser.find_element(By.XPATH, similac_menu_path)
    sim_pro_menu = browser.find_element(By.XPATH, sim_pro_sen_path)
    hoover_over = ActionChains(browser)
    hoover_over.move_to_element(similac_menu)
    hoover_over.click(sim_pro_menu)
    hoover_over.perform()
    ready_to_feed_path = "//img[contains(@alt, '32') and contains(@alt, 'Sensitive')]/../figcaption"
    ready_to_feed_menu = browser.find_element(By.XPATH, ready_to_feed_path)
    ready_to_feed_menu.click()
    stock_status_path = "//p[@id='stock-status']"
    stock_status = browser.find_element(By.XPATH, stock_status_path).text
    browser.close()
    return stock_status


def send_email_alert(status):
    '''
    Send email alert using yagmail
    :param status: The email content you want to send.
    :return: No return.
    '''
    mail = yagmail.SMTP('fromemail@gmail.com')
    contents = status
    mail.send(['toemail@gmail.com', 'toemail2@gmail.com'], 'Similac In Stock Alert', contents)


if __name__ == "__main__":
    sim_pro_sen = formula_stock_status("Similac Pro-Sensitive")
    print(f"Similac Pro-Sensitive: {sim_pro_sen}")
    sim_360_sen = formula_stock_status("Similac 360 Total Care")
    print(f"Similac 360 Total Care: {sim_360_sen}")
    status = f"Similac Pro-Sensitive: {sim_pro_sen}\nSimilac 360 Total Care: {sim_360_sen}"
    if sim_pro_sen == 'IN STOCK' or sim_360_sen == 'IN STOCK':
        send_email_alert(status)
