import json
# from utils import Chapter
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
qran = open('qran.json',)
data = json.load(qran)
surahList = data.get("surahs").get("references")
totalAyahs = 0
allChapters = []
for surah in surahList:
    totalAyahs = totalAyahs + surah.get("numberOfAyahs")
    currShapter = Chapter(surah.get("englishName"), surah.get("number"), surah.get("numberOfAyahs"), surah.get("numberOfPages"))
    allChapters.append(currShapter)

# print(allChapters[0])