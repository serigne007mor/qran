from utils import getDaysPages
import datetime


def diff_dates(date1, date2):
    """[summary]

    Args:
        date1 ([type]): [description]
        date2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    if (date1 < date2):
        return -1

    return abs(date2-date1).days


def createButton():
    head = open("./templates/createButton.html", "r")
    shead = ""
    for line in head:
        # print(line)
        shead = shead+line
    return (shead)
