import data
from math import ceil

class chapter:
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



def diff_dates(date1, date2):
    """[summary]

    Args:
        date1 ([type]): [description]
        date2 ([type]): [description]

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


def getDaysPages(numberOfDays, startSurah, endSurah=1):
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
    surahFinishDay = {}
    for i in (chaptersToLearn):
        pageGoal = pageGoal + i.numberOfPages

    dailyPageGoal = ceil(pageGoal/numberOfDays)

    dailySurah = []
    for surah in reversed(chaptersToLearn):
        learnSoFar += surah.numberOfPages
        dailySurah.append(surah)
        if (learnSoFar>dailyPageGoal):
            if (abs(learnSoFar-dailyPageGoal <0.25)):
                surahFinishDay[day] = dailySurah
            elif (abs(learnSoFar-dailyPageGoal >=0.25)):
                surahFinishDay[day] = dailySurah[:-1]

            learnSoFar = 0
            day+=1
            togo = dailySurah[len(dailySurah)-1]
            dailySurah = []
            dailySurah.append(togo)
    sortedDict = sorted(surahFinishDay)
    returnValue = [dailyPageGoal, surahFinishDay]
    return (returnValue)

