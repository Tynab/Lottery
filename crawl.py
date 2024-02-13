import os
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

current_date = datetime(2005, 1, 1).date()

is_mod = False

if os.path.isfile("head.csv") and os.path.isfile("tail.csv"):
    head_df = pd.read_csv("head.csv")
    last_head_date = pd.to_datetime(head_df['date'].iloc[-1]).date()

    tail_df = pd.read_csv("tail.csv")
    last_tail_date = pd.to_datetime(tail_df['date'].iloc[-1]).date()

    if last_head_date == last_tail_date:
        is_mod = True
        current_date = last_head_date + timedelta(days=1)
    else:
        os.remove("head.csv")
        os.remove("tail.csv")
else:
    if os.path.isfile("head.csv"):
        os.remove("head.csv")
    elif os.path.isfile("tail.csv"):
        os.remove("tail.csv")

head_data = []
tail_data = []

options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('chromedriver_path')
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

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

        try:
            for xpath in xpath_list:
                head_row = [current_date]
                head_row.extend([0] * 10)
                head_row[int(browser.find_element(By.XPATH, xpath).text[-2]) + 1] = 1

                tail_row = [current_date]
                tail_row.extend([0] * 10)
                tail_row[int(browser.find_element(By.XPATH, xpath).text[-1]) + 1] = 1

                head_data.append(head_row)
                tail_data.append(tail_row)
        except:
            print(f'{day}-{month}-{year} data has been lost!')

        current_date += timedelta(days=1)

head_df = pd.DataFrame(head_data, columns=['date', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
tail_df = pd.DataFrame(tail_data, columns=['date', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

if is_mod:
    head_df.to_csv("head.csv", mode='a', header=False, index=False, lineterminator='\n')
    tail_df.to_csv("tail.csv", mode='a', header=False, index=False, lineterminator='\n')
else:
    head_df.to_csv("head.csv", index=False)
    tail_df.to_csv("tail.csv", index=False)