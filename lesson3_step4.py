from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(str(y))

button_1 = browser.find_element_by_css_selector("button.btn")
button_1.click()
