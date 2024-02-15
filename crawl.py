import os
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

FILE_NAME = 'lottery.csv'

current_date = datetime(2005, 1, 1).date()

is_mod = False

if os.path.isfile(FILE_NAME):
    is_mod = True
    current_date = pd.to_datetime(pd.read_csv(FILE_NAME)['Date'].iloc[-1]).date() + timedelta(days=1)

data = []

options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('chromedriver_path')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

xpath_list = ['/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/div',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[3]/td[2]/div',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[3]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[4]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[5]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[5]/td[2]/div[6]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[6]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[6]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[6]/td[2]/div[3]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[6]/td[2]/div[4]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[3]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[4]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[5]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[7]/td[2]/div[6]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[8]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[8]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[8]/td[2]/div[3]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[9]/td[2]/div[1]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[9]/td[2]/div[2]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[9]/td[2]/div[3]',
              '/html/body/div[1]/div/center/div/div/div[3]/div/div/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[9]/td[2]/div[4]']

with webdriver.Chrome(options=options) as browser:
    while current_date != datetime.now().date():
        day = current_date.day
        month = current_date.month
        year = current_date.year

        print(f'Processing {day}-{month}-{year}...')

        browser.get(f'https://www.minhngoc.net.vn/tra-cuu-ket-qua-xo-so.html?mien=2&thu=0&ngay={day}&thang={month}&nam={year}')

        row = [current_date]
        row.extend([0] * 10)

        try:
            for xpath in xpath_list:
                for digit in browser.find_element(By.XPATH, xpath).text:
                    if digit.isdigit():
                        row[int(digit) + 1] += 1
        except:
            print(f'{day}-{month}-{year} data has been lost!')
        
        data.append(row)
        current_date += timedelta(days=1)

df = pd.DataFrame(data, columns=['Date', 'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'])

if is_mod:
    df.to_csv(FILE_NAME, mode='a', header=False, index=False, lineterminator='\n')
else:
    df.to_csv(FILE_NAME, index=False)