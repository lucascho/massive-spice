import datetime
import collections

#2015-01-21 07:57:15

INPUT_TIMEFORMAT = "%Y-%m-%d"
OUTPUT_TIMEFORMAT = "%Y-%m"

def processDate(values):
    outputDict = {}
    for value in values:
        dateObj = datetime.datetime.strptime(value, INPUT_TIMEFORMAT)
        nearestMonth = datetime.datetime.strftime(dateObj, OUTPUT_TIMEFORMAT)
        try:
            outputDict[nearestMonth]
        except KeyError:
            outputDict[nearestMonth] = 0
        outputDict[nearestMonth] += 1        
    return collections.OrderedDict(sorted(outputDict.items()))
