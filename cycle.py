from parserr import Trade
import time

all_data = []
e = Trade()

while 1:
    a = e.parse_()
    print(a)
    all_data.append(a)
    time.sleep(60)
