# login_module.py
from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver, url, username_xpath, password_xpath, login_button_xpath, submit_button_xpath, username, password):
    driver.get(url)  # Open the website
    driver.find_element(By.XPATH, login_button_xpath).click()  # Click the login button
    driver.find_element(By.XPATH, username_xpath).send_keys(username)  # Enter username
    driver.find_element(By.XPATH, password_xpath).send_keys(password)  # Enter password
    driver.find_element(By.XPATH, submit_button_xpath).click()  # Click submit button
