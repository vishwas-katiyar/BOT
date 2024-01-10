import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor

def perform_test(url):
    driver = webdriver.Chrome()  # You can use other browsers by changing this line accordingly
    driver.get(url)

    clickable_elements = driver.find_elements(By.XPATH, '//*[self::a or self::button]')

    selected_element = random.choice(clickable_elements)

    actions = ActionChains(driver)
    actions.move_to_element(selected_element).perform()

    selected_element.click()


    driver.quit()

if __name__ == "__main__":
    url = "http://localhost:3000/"  # Replace this with the URL you want to test
    num_browsers = 5

    with ThreadPoolExecutor(max_workers=num_browsers) as executor:
        executor.map(perform_test, [url] * num_browsers)
