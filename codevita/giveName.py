from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace this with the WebDriver path
driver_path = "C:\\Users\\DELL\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe"
leetcode_profile_url = "https://leetcode.com/u/sk_aayush/"
output_file = "questions.txt"

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

    # Initialize an empty list to store question names
    question_names = []

    while True:
        # Collect all question titles
        questions = driver.find_elements(By.XPATH, "//div[contains(@class, 'hover:bg-overlay-1')]")
        for question in questions:
            name = question.text.split("\n")[0]  # Extract the question name
            if name not in question_names:
                question_names.append(name)

        # Check for "Show More" button
        try:
            show_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show More')]")
            show_more_button.click()
            time.sleep(3)  # Wait for new questions to load
        except:
            # If no "Show More" button is found, break the loop
            break

    # Save the question names to a file
    with open(output_file, "w", encoding="utf-8") as file:
        for name in question_names:
            file.write(name + "\n")

    print(f"Saved {len(question_names)} questions to {output_file}")

finally:
    driver.quit()
