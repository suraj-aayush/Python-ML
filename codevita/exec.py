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
    wait = WebDriverWait(driver, 15)
    solutions_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Solutions')]"))
    )
    solutions_tab.click()

    time.sleep(5)  # Allow the solutions page to load

    # Collect all solution links
    solution_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/solutions/')]")
    solution_urls = [link.get_attribute("href") for link in solution_links]

    # Open each solution in a new tab
    for url in solution_urls:
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(1)  # Slight delay for browser stability

    print(f"Opened {len(solution_urls)} solutions in new tabs.")

finally:
    driver.quit()
