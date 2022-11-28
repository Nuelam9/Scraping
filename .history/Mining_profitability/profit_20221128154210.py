import selenium
# selenium.__version__ == '3.141.0'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import List
import time as t


drive_type = selenium.webdriver.chrome.webdriver.WebDriver

class Profitability_calculator:
    def __init__(self, driver_path: str,
                 url_to_profit: str, time_range: List[str]):
        self.url_profit = url_to_profit
        self.path_driver = driver_path
        self.time_range = time_range
    
    @property
    def driver(self):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920, 1200")
        options.add_argument("user-agent=whatever you want")
        driver = webdriver.Chrome(options=options,
                                  executable_path=self.path_driver)
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
        objects = driver.find_elements_by_class_name('filter')
        button = [obj for obj in objects if obj.text == time][0]
        return button
    
    def get_profit_values(self, driver: drive_type):
        objects = driver.find_elements_by_class_name('value')
        obj = objects[0]
        return obj.text 

    def get_results(self):
        driver = self.driver
        for time in self.time_range:
            button = self.get_button(driver, time)
            button.click()
            profit = self.get_profit_values(driver)
            print_text = 'AVG. PROFITABILITY FOR SELECTED TIME RANGE'
            print(f'\033[1m{print_text} ({time}) \033[0m')
            print(f'{profit}\n')


if __name__ == '__main__':
    driver_path = './chromedriver.exe'
    url_profit = 'https://www.nicehash.com/profitability-calculator/nvidia-gtx-1650-super'
    time_range = ['1D', '1W', '1M']

    Profit_calculator = Profitability_calculator(driver_path,
                                                 url_profit, time_range)
    Profit_calculator.get_results()
