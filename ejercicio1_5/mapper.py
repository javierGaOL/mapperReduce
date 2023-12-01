
#!/usr/bin/python
import sys

for line in sys.stdin:
    if ("\t") in line:
        data = line.strip().split("\t")
        date, time, store, item, cost, payment = data
        print(item+"\t"+cost)



