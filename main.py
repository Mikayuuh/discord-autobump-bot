import os
import selenium
from selenium import webdriver
import time
import json
from selenium.webdriver.common.keys import Keys
from json import load, dump


def login():
    with open('config.json') as f:
        config = json.load(f)
    
    email = config.get('email')
    password = config.get('password')
    guild = config.get('guild_id')
    channel = config.get('channel_id')
    print("""

YAPIMCILAR;

Morp Noface?#1468
Kerems#1295

""")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options = options, executable_path = 'chromedriver.exe')
    driver.get("https://discord.com/login")
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div").click()
    check_captcha = input("Doğrulama bekleniyor...")
    time.sleep(10)
    driver.get("https://discord.com/channels/" + (guild) + "/" + (channel))
    time.sleep(10)
    def bump():
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]").send_keys("!d bump" + Keys.ENTER)
        time.sleep(7220)
        bump()
    bump()


if __name__ == "__main__":
    login()