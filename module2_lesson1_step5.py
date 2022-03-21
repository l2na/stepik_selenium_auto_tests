from selenium import webdriver
import math
import time

try: 

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    result = browser.find_element_by_id("answer")
    result.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector('[value="robots"]')
    robot_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(7)
    browser.quit()