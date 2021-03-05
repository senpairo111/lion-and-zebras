from settings import year_deadline
from settings import SPEEDS
import matplotlib.pyplot as plt
import numpy as np
from settings import zebra_count
from zebra_array import ZebraArray

zeb = ZebraArray()

PRINT_STATS = False
YEARS_TO_MEASURE = 1


def main():
    while zeb.years_passed < year_deadline:
        if zeb.years_passed % YEARS_TO_MEASURE == 0:
            if PRINT_STATS:
                print(f"run number {zeb.years_passed}")
                print(f"yearly fails {zeb.failed_year}")
                print(f"total fails {zeb.failed_total}")
            zeb.print_stats(PRINT_STATS)
        zeb.killer()
        zeb.breeder()
    xpoints_zeb = np.array(range(len(zeb.total_speeds)))
    ypoints_zeb = np.array(zeb.total_speeds)

    plt.plot(xpoints_zeb, ypoints_zeb)
    plt.show()


if __name__ == '__main__':
    main()
