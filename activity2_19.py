import random 
import time
def getRandomDate(starDate, endDate):
    print("Printing random date between", starDate, "and", endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(starDate, dateFormat))
    endtime=time.mktime(time.strptime(starDate, dateFormat))
    randomTime=starttime+randomGenerator*(endtime-starttime)
    randomeDate=time.strftime(dateFormat, time.localtime(randomTime))
    return randomeDate
print("Random date=", getRandomDate("1/1/2020", "12/12/2024"))