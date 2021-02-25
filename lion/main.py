from settings import year_deadline
from settings import speeds
from settings import zebra_count
from zebra_array import ZebraArray
zeb = ZebraArray()
while zeb.years_passed < year_deadline:
    if zeb.years_passed % 100 == 0:
        print(f"run number {zeb.years_passed}")
        print(f"yearly fails {zeb.failed_year}")
        print(f"total fails {zeb.failed_total}")
        zeb.print_stats()
    zeb.killer()
    zeb.breeder()
zeb_zpeeds = speeds