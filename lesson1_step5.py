from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
#Считываем значение и считаем его по формуле
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)
#Записываем посчитанный ответ в форму
input = browser.find_element_by_css_selector('#answer')
input.send_keys(str(y))
#Нажимае чекбокс
input_1 = browser.find_element_by_css_selector('#robotCheckbox')
input_1.click()
#Нажимаем кнопку "роботы рулят"
input_2 = browser.find_element_by_css_selector('#robotsRule')
input_2.click()
#отправляем и получаем код
button = browser.find_element_by_css_selector("button.btn")
button.click()
