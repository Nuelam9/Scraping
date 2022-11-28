


if __name__ == '__main__':
    driver_path = './chromedriver.exe'
    url_profit = 'https://www.nicehash.com/profitability-calculator/nvidia-gtx-1650-super'
    time_range = ['1D', '1W', '1M']

    Profit_calculator = Profitability_calculator(driver_path,
                                                 url_profit, time_range)
    Profit_calculator.get_results()