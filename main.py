import json
from fractions import Fraction
from datetime import date
from math import ceil
import data
import utils


if __name__ == '__main__':
    d1 = date(2020, 1, 31)
    d2 = date(2021, 1, 30)
    numberOfDays = utils.diff_dates(d2, d1)
    returnValue = utils.getDaysPages(numberOfDays, 114,1)
    dailyPageGoal = returnValue[0]
    surahFinishDay = returnValue[1]
    print(surahFinishDay )
