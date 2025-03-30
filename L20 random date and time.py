import random 
import time

def getRandomDate(starDate , endDate):
    print("printing random date between", starDate, "and", endDate)
    ramdomGenerator = random.random()

    dateFormat = "%m/%d/%Y" 
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))

    ramdomTime = starttime + ramdomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(ramdomTime))


    return randomDate


result = getRandomDate("1/1/2025", "12/31/2025")
print("ramdom date = ", result)