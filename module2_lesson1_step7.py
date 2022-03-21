from selenium import webdriver
import math
import time

try: 

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    image = browser.find_element_by_id("treasure")
    img_value = image.get_attribute("valuex")
    y = calc(img_value)

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