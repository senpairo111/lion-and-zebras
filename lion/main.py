from settings import year_deadline
from settings import speeds
from settings import zebra_count
from zebra_array import ZebraArray
zeb = ZebraArray()
while zeb.years_passed < year_deadline:
    zeb.killer()
    print("year passed")
    zeb.breeder()
zeb_zpeeds = speeds