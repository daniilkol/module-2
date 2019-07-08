from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока цена нам не подойдет
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_css_selector('#book').click()


x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(str(y))

button_1 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
button_1.click()
