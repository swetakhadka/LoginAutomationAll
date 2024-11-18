# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json
from loginmodule import login
import time


def main():
    # Load website details from config.json
    with open("config.json", "r") as file:
        config = json.load(file)

    # Extract the details for the 'siam99' website
    website = config["siam99"]

    # Initialize WebDriver with explicit Service object
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Call the login function with the extracted details
    login(
        driver,
        website["url"],
        website["username_xpath"],
        website["password_xpath"],
        website["login_button_xpath"],
        website["submit_button_xpath"],
        website["username"],
        website["password"]
    )

    # Close the browser after the test
    driver.quit()


if __name__ == "__main__":
    main()  # Run the login test
