import json
from utils import chapter

qran = open('qran.json',)
data = json.load(qran)
surahList = data.get("surahs").get("references")
totalAyahs = 0
allChapters = []
for surah in surahList:
    totalAyahs = totalAyahs + surah.get("numberOfAyahs")
    currShapter = chapter(surah.get("englishName"), surah.get("number"), surah.get("numberOfAyahs"), surah.get("numberOfPages"))
    allChapters.append(currShapter)

# print(allChapters[0])