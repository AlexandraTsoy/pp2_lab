from datetime import date, timedelta
from time import time
yesterday = date.today() - timedelta(1)
today = date.today()
tomorrow = date.today() + timedelta(1)
print("yesterday was:", yesterday)
print("today is:", today)
print("tomorrow will be:", tomorrow) 