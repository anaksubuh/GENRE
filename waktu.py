import time
import datetime

print('hello world')

while True:
    current_time = datetime.datetime.now()
    now = current_time.strftime('%H:%M:%S')
    date = current_time.strftime('%d/%m/%Y')
    print()
    print(f'[+] {now} {date}')
    time.sleep(1)
    time.sleep(1)