from envelopes import Envelope
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


def mail(send_to, text):
    envelope = Envelope(
        from_addr=(u'powderbot812@gmail.com', u'Powder Updates'),
        to_addr=send_to,
        subject=u'Powder in stock',
        text_body=text
    )
    envelope.send('smtp.googlemail.com', login='powderbot812@gmail.com',
                  password='uoRdD48CokP3', tls=True)


def check_varget_powdervalley(browser):
    # 1-pound
    browser.get('https://www.powdervalleyinc.com/product/hodgdon-varget/')
    Select(browser.find_element(By.ID, "pa_options")).select_by_value("hodgdon-varget-1")
    element = browser.find_element(By.CLASS_NAME, "stock")
    if element.text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "Powder Valley has Varget 1 pound!!!")
    # 8-pound
    browser.get('https://www.powdervalleyinc.com/product/hodgdon-varget/')
    Select(browser.find_element(By.ID, "pa_options")).select_by_value("hodgdon-varget-8")
    element = browser.find_element(By.CLASS_NAME, "stock")
    if element.text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "Powder Valley has Varget 8 pound!!!")


def check_h4895_powdervalley(browser):
    # 1-pound
    browser.get('https://www.powdervalleyinc.com/product/hodgdon-h4895/')
    Select(browser.find_element(By.ID, "pa_options")).select_by_value("hodgdon-h4895-1")
    element = browser.find_element(By.CLASS_NAME, "stock")
    if element.text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "Powder Valley has H4895 1 pound!!!")
    # 8-pound
    browser.get('https://www.powdervalleyinc.com/product/hodgdon-h4895/')
    Select(browser.find_element(By.ID, "pa_options")).select_by_value("hodgdon-h4895-8")
    element = browser.find_element(By.CLASS_NAME, "stock")
    if element.text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "Powder Valley has H4895 8 pound!!!")


def check_varget_midwayusa(browser):
    # 1-pound
    browser.get('https://www.midwayusa.com/product/1009281345?pid=963843')
    browser.find_element(By.CLASS_NAME, "product-filter-heading-container").click()
    elements = browser.find_elements(By.CLASS_NAME, "product-filter-status")
    if elements[0].text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "MidwayUSA has Varget 1 pound!!!")
    # 8-pound
    browser.get('https://www.midwayusa.com/product/1009281345?pid=963843')
    browser.find_element(By.CLASS_NAME, "product-filter-heading-container").click()
    elements = browser.find_elements(By.CLASS_NAME, "product-filter-status")
    if elements[1].text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "MidwayUSA has Varget 8 pound!!!")


def check_h4895_midwayusa(browser):
    # 1-pound
    browser.get('https://www.midwayusa.com/product/1009336348?pid=882564')
    browser.find_element(By.CLASS_NAME, "product-filter-heading-container").click()
    elements = browser.find_elements(By.CLASS_NAME, "product-filter-status")
    if elements[0].text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "MidwayUSA has H4895 1 pound!!!")
    # 8-pound
    browser.get('https://www.midwayusa.com/product/1009336348?pid=882564')
    browser.find_element(By.CLASS_NAME, "product-filter-heading-container").click()
    elements = browser.find_elements(By.CLASS_NAME, "product-filter-status")
    if elements[1].text != "Out of stock":
        pass
    else:
        mail("cshreck1@gmail.com", "MidwayUSA has H4895 8 pound!!!")


def loop():
    while True:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        check_h4895_powdervalley(browser)
        check_varget_powdervalley(browser)
        browser.close()
        time.sleep(900000)


if __name__ == "__main__":
    loop()
