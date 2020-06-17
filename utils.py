import data
from math import ceil, floor

class Chapter:
    """[summary]
    """
    def __init__(self, name, chapterNum, numberOfAyahs, numberOfPages):
        self.name = name
        self.chapterNum = chapterNum
        self.numberOfAyahs = numberOfAyahs
        self.numberOfPages = numberOfPages

    def __eq__(self, other):
        return self.chapterNum == other.chapterNum

    def __repr__(self):
        return  self.name


def getHeader():
    head = open("./templates/head", "r")
    shead = ""
    for line in head:
        # print(line)
        shead = shead+line
    return (shead)

def createButton():
    head = open("./templates/createButton.html", "r")
    shead = ""
    for line in head:
        # print(line)
        shead = shead+line
    return (shead)


def diff_dates(date1, date2):
    """[summary]

    Args:
        date1 (datetime.date): [description]
        date2 (datetime.date): [description]

    Returns:
        [type]: [description]
    """

    return abs(date2-date1).days


def getDaysAyah(numberOfDays, startSurah, endSurah=0):
    """[summary]

    Args:
        numberOfDays (int): [description]
        startSurah (chapter): [description]
        endSurah (chapter, optional): [description]. Defaults to 0.
    """
    endSurah -= 1
    ayahGoal = 0
    dailyAyahGoal = 0

    for i in (data.allChapters[endSurah:startSurah]):
        ayahGoal = ayahGoal + i.numberOfAyahs

    dailyAyahGoal = ceil(ayahGoal/numberOfDays)

    return (dailyAyahGoal)


def getDaysPages(numberOfDays, startSurah, endSurah=1, precision=0):
    """[summary]

    Args:
        numberOfDays (int): [description]
        startSurah (chapter): [description]
        endSurah (chapter, optional): [description]. Defaults to 1.
    """
    chaptersToLearn = data.allChapters[endSurah:startSurah]
    pageToDay = 0
    learnSoFar = 0
    # endSurah -= 1
    pageGoal = 0
    dailyPageGoal = 0
    day = 1
    numPagesTillSurah = {}
    for i in reversed(chaptersToLearn):
        pageGoal = pageGoal + i.numberOfPages
        numPagesTillSurah[i.name] = pageGoal

    dailyPageGoal = round(pageGoal/numberOfDays,precision)
    surahFinishDay = {}
    for i in reversed(chaptersToLearn):
        if(numPagesTillSurah[i.name] % dailyPageGoal > .2):
            surahFinishDay[i.name] = ceil(numPagesTillSurah[i.name]/dailyPageGoal)
        else:
            surahFinishDay[i.name] = floor(numPagesTillSurah[i.name]/dailyPageGoal)

    surahFinishDayS = sorted(surahFinishDay)
    returnValue = [dailyPageGoal, surahFinishDay, chaptersToLearn]
    return  returnValue

