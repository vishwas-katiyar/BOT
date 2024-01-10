import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor

def perform_test(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Maximize the browser window

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)

    # Step 2: Open 5 new tabs
    for _ in range(4):
        driver.execute_script("window.open('about:blank', '_blank');")

    # Step 3: Switch to each tab and navigate to the URL
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

    # Step 4: Close the first tab (optional)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    # Wait for a few seconds to see the result
    # time.sleep(5)

    # Close all browser windows
    driver.quit()

if __name__ == "__main__":
    url = "https://mihir-music.vercel.app/"  # Replace this with the URL you want to test
    num_browsers = 5

    with ThreadPoolExecutor(max_workers=num_browsers) as executor:
        executor.map(perform_test, [url] * num_browsers)
