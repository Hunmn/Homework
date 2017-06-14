from datetime import datetime


now = datetime.today()
def newy(year):
    ny = datetime(year,1,1)
    razn = ny - now
    return razn

print('До нового года осталось ' + str(newy(2019)))
