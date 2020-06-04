import json
from fractions import Fraction

class chapter:
    def __init__(self, name, chapterNum, numVerse, numPage):
        self.name = name 
        self.chapterNum = chapterNum
        self.numVerse = numVerse
        self.numPage = numPage
    
    def __repr__(self):
        return "This is surat "+ self.name

def getDays():
    pass
if __name__ == '__main__':
    qran = open('qran.json',) 
    data = json.load(qran)
    surahList = data.get("surahs").get("references")
    totalAyahs = 0
    
    for surah in surahList:
        totalAyahs = totalAyahs + surah.get("numberOfAyahs")
    
    print(totalAyahs)