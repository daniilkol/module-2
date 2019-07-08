from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
#Считываем значение из сундука :) и считаем его по формуле
x_element = browser.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)
#Записываем посчитанный ответ в форму
input = browser.find_element_by_id('answer')
input.send_keys(str(y))
#Нажимае чекбокс
input_1 = browser.find_element_by_id('robotCheckbox')
input_1.click()
#Нажимаем кнопку "роботы рулят"
input_2 = browser.find_element_by_id('robotsRule')
input_2.click()
#отправляем и получаем код
button = browser.find_element_by_css_selector("button.btn")
button.click()
