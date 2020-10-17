from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	btn = browser.find_element_by_id("book")
	btn.click()
	
	#вычисляем нужное значение
	x_element = browser.find_element_by_id("input_value")
	#получаем текст между открывающим и закрывающим тегом
	x = x_element.text
	y = calc(x)

	#заполняем поле y
	input_ans = browser.find_element_by_id("answer")
	input_ans.send_keys(y)
	btn = browser.find_element_by_css_selector("#solve")
	btn.click()


finally:
	time.sleep(15)
	browser.quit()