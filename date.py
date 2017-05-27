from datetime import datetime
now = datetime.today()
ny = datetime(2018,1,1)
razn = ny - now
print('До нового года осталось ' + str(razn))

