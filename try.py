database = open('cerita_publick.txt', 'r')
count = 0
# Using for loop
for data in database:
    count += 1
    print(str(data.strip()))

import time
time.sleep(999)