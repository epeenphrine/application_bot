from datetime import datetime
from datetime import timedelta
import time
x = datetime.now() + timedelta(days=1)
y = x.strftime('%m/%d/%Y')
print(y)