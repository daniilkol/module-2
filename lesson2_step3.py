from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1')
y_element = browser.find_element_by_id('num2')
x = x_element.text
y = y_element.text
result = int(x) + int(y)


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(result))

button = browser.find_element_by_css_selector("button.btn")
button.click()
