from dataclasses import dataclass
from datetime import datetime


now = datetime(2022,8,20,10,00,00,00)
print(now)
print(type(now))
now2 = datetime.now()
print(now2)
print(type(now))