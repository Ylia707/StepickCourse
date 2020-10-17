from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	btn = browser.find_element_by_css_selector(".btn")
	btn.click()
	confirm = browser.switch_to.alert
	confirm.accept()
	#вычисляем нужное значение
	x_element = browser.find_element_by_id("input_value")
	#получаем текст между открывающим и закрывающим тегом
	x = x_element.text
	y = calc(x)

	#заполняем поле y
	input_ans = browser.find_element_by_id("answer")
	input_ans.send_keys(y)
	btn = browser.find_element_by_css_selector(".btn")
	btn.click()


finally:
	time.sleep(15)
	browser.quit()