#!/usr/bin/python3

import os, time, random

from utils.http import HTTP
from utils.file import File

from apis.imgur import Imgur
from layout.layout import Layout

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Screenshot:

    @classmethod
    def generate_id(cls, size):
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for _ in range(0, size):
            random_string += str(
                random_str_seq[
                    random.randint(
                        0, len(random_str_seq) - 1
                    )
                ]
            )
            
        return random_string

    @classmethod
    def browser_chrome(cls, url, file):
        options = webdriver.ChromeOptions()
        
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        driver.save_screenshot(file)
        driver.quit()

    @classmethod
    def browser_firefox(cls, url, file):
        options = FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.get(url)
        driver.save_screenshot(file)
        driver.quit()

    @classmethod
    def run(cls, url, browser, upload, title):
        start_time = time.time()
        
        path = f"screenshots\\{HTTP.get_hostname(url)}\\"
        
        File.create_path(path)

        file = path + f"{cls.generate_id(12)}.png"
        
        if not browser or browser == 'chrome':
            cls.browser_chrome(url, file)
        elif browser == 'firefox':
            cls.browser_firefox(url, file)
        else:
            Layout.error("Browser is invalid", False, True)

        if os.path.exists(file):
            Layout.success("screenshot saved with successfully.")

            if not upload:
                File.open(file)
                Layout.time_taken(start_time)
            else:
                Imgur.upload(file, title)
