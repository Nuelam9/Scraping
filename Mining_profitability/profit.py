import selenium
# selenium.__version__ == '4.6.1'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import List
import time as t
from dataclasses import dataclass


drive_type = selenium.webdriver.chrome.webdriver.WebDriver

@dataclass
class Profitability_calculator:
    driver_path: str
    url_profit: str
    time_range: List[str]
    
    @property
    def driver(self):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920, 1200")
        options.add_argument("user-agent=whatever you want")
        driver = webdriver.Chrome(options=options, executable_path=self.driver_path)
        # Browse the profitability calculator of nicehash
        driver.get(self.url_profit)
        t.sleep(10)
        # Gets the page's title and the current url
        print(f'{driver.title}, {driver.current_url}\n')
        return driver
        
    def get_button(self, driver: drive_type, time: str):
        """
        time:: ['1D', '1W', '1M']
        """
        objects = driver.find_elements(By.CLASS_NAME, "filter")
        return [obj for obj in objects if obj.text == time][0]
    
    def get_profit_values(self, driver: drive_type):
        objects = driver.find_elements(By.CLASS_NAME, "value")
        obj = objects[0]
        return obj.text 

    def get_results(self):
        driver = self.driver
        for time in self.time_range:
            button = self.get_button(driver, time)
            button.click()
            profit = self.get_profit_values(driver)
            print_text = 'AVG. PROFITABILITY FOR SELECTED TIME RANGE'
            print(f'\033[1m{print_text} ({time})  \033[0m')
            print(f'{profit}\n')
