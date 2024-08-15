from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.chrome.options import Options
# Path to your ChromeDriver
chrome_driver_path = '/home/sourav/Desktop/chromedriver-linux64/chromedriver'
service = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram
driver.get("https://www.instagram.com/")
username = 'ekartlogistic63@gmail.com'
password = 'agastya_shah01'

# Define explicit wait
wait = WebDriverWait(driver, 20)  # Wait for up to 20 seconds
driver.delete_all_cookies()
def login():    
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys(username)
    pass_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    pass_field.send_keys(password)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    
def remove():
    try:
        not_now_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1i10hfl.xqeqjp1")))
        not_now_button.click()
    except Exception as e:
        print(f"Error finding 'Not Now' button: {e}")
    
    try:
        notification_not_now_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
        notification_not_now_button.click()
    except Exception as e:
        print(f"Error finding notification 'Not Now' button: {e}")

def send_random_message():
    messages = [
        "OP BOLTE KHOPDI KHOLTE",
        "EEEEEEEEEEEEEEEEEEEEEE",
        "TERI CHUUUUUU",
        "I like to touch kidss"
    ]
    
    driver.get("https://www.instagram.com/direct/t/8031804303580240/")
    
    try:
        message_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message']")))

        while True:
            try:
                random_message = random.choice(messages)
                print(f"Sending message: {random_message}")
                message_input.send_keys(random_message)
                message_input.send_keys(Keys.RETURN)
                print(f"Sent message: {random_message}")
                time.sleep(5)  # Wait for 5 seconds before sending the next message
            except Exception as e:
                print(f"Error sending message: {e}")
                # Try to locate the message input again if an error occurs
                message_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message']")))
    except Exception as e:
        print(f"Error accessing the message input field: {e}")

# Perform the actions
login()
remove()
send_random_message()

# Close the browser
# The script will run indefinitely, so the driver.quit() line will not be reached.
