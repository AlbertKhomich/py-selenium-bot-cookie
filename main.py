from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

time_out = time.time() + (5 * 60)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')

time_machine = driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine')
portal = driver.find_element(By.CSS_SELECTOR, '#buyPortal')
lab = driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab')
shipment = driver.find_element(By.CSS_SELECTOR, '#buyShipment')
mine = driver.find_element(By.CSS_SELECTOR, '#buyMine')
factory = driver.find_element(By.CSS_SELECTOR, '#buyFactory')
grandma = driver.find_element(By.CSS_SELECTOR, '#buyGrandma')
cursor = driver.find_element(By.CSS_SELECTOR, '#buyCursor')

money = driver.find_element(By.CSS_SELECTOR, '#money')
result = driver.find_element(By.CSS_SELECTOR, '#cps')


elements = [time_machine, portal, lab, shipment, mine, factory, grandma, cursor]
id_ = [
    '#buyTime\ machine', '#buyPortal',
    '#buyAlchemy\ lab', '#buyShipment',
    '#buyMine', '#buyFactory',
    '#buyGrandma', '#buyCursor'
]


def upgrading():

    for i in range(8):
        try:
            if convert(elements[i]) <= convert(money):
                elements[i].click()
                break
        except:
            elements[i] = driver.find_element(By.CSS_SELECTOR, id_[i])
            if convert(elements[i]) <= convert(money):
                elements[i].click()
                break
    clicking()


def clicking():
    if time.time() >= time_out:
        print(result.text)
    x = 0
    while True:
        cookie.click()
        x += 1
        if x == 300:
            break
    upgrading()


def convert(elem):
    result = elem.text
    x = result.split('\n')
    y = x[0].strip("zaqwsxcderfvbgtyhnmjuiklopZAQWSXCDERFVBGTYHNMJUIKLOP-. ")
    x = y.split(',')
    y = ''.join(x)
    return int(y)


clicking()
