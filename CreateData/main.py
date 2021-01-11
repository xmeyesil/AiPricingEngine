from datetime import date
from WeeksWeight import WeeksWeight

gunler = date.today().isocalendar()[1]
tarih = date(2020, 12, 5)
weeks = WeeksWeight(tarih)

print(tarih)

