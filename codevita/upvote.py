from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace this with the WebDriver path
driver_path = "C:\\Users\\DELL\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe"
leetcode_profile_url = "https://leetcode.com/u/sk_aayush/"

# Create a Service object and pass it to the WebDriver
service = Service(driver_path)
driver = webdriver.Edge(service=service)

try:
    # Open the user's LeetCode profile
    driver.get(leetcode_profile_url)

    # Wait for the "Solutions" tab to become visible and clickable
    wait = WebDriverWait(driver, 15)  # 15-second timeout
    solutions_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(), 'Solutions')]")
        )
    )

    # Click on the "Solutions" tab
    solutions_tab.click()
    time.sleep(5)  # Allow the solutions page to load

    # Scroll to load all solutions (if lazy loading is used)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Collect all solution links
    solution_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/solutions/')]")
    solution_urls = [link.get_attribute("href") for link in solution_links]

    # Open each solution in a new tab and upvote
    for url in solution_urls:
        driver.execute_script(f"window.open('{url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)  # Allow the solution page to load

        # Click the upvote button
        try:
            upvote_button = driver.find_element(By.XPATH, "//button[contains(@class, 'upvote')]")
            upvote_button.click()
            print(f"Upvoted solution: {url}")
        except Exception as e:
            print(f"Could not upvote solution {url}: {e}")

        # Close the tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

finally:
    # Close the browser
    driver.quit()
