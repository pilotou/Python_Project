import requests
from bs4 import BeautifulSoup
from sendEmail import sendEmail
import time

response = requests.get('https://www.boc.cn/sourcedb/whpj/')
all_html = response.content.decode()

soup = BeautifulSoup(all_html, "html.parser")

all_table = soup.find_all('table')[1]
au = all_table.find_all('tr')[2]
# get the exchange rate
exchange_rate = eval(au.find_all('td')[3].text)
print(exchange_rate)

expect_au_exchange_rate = 501.0
time_today = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

f = open("log.txt", 'a')

if exchange_rate <= expect_au_exchange_rate:
    sendEmail(exchange_rate)
    f.write(f'{time_today} | Au to RMB: {exchange_rate}  email sent\n')
else:
    f.write(f'{time_today} | Au to RMB: {exchange_rate} \n')

f.close()
