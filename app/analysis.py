import numpy, scipy
from scipy import stats
import json, datetime, collections, pprint

INPUT_TIMEFORMAT = "%Y-%m-%d"
OUTPUT_TIMEFORMAT = "%Y-%m"


def main():
  f = open('../data/opportunities.json')
  data = json.load(f)

  for s in data["status"]:
    for field in data["status"][s]:
   
      field_data = data["status"][s][field]
      data_type = field_data["type"]
      values = field_data["values"]

      if data_type=="string":
        print process_text(values)
      
      elif data_type=="numeric":
        print process_numerics(values)
      
      else: 
        print process_date(values)


# return an array of numeric values indicating similarity between two fields
def process_text(values):
  dic = {}
  for phrases in values:
    for w in phrases.split():
      if w not in dic:
        dic[w] = 1
      else: 
        dic[w] += 1
  return dic


# return True if the field value matches 
def run_text_matching(values):
  return


# return a numeric summary of the values
def process_numerics(values):
  result = {}
  dstats = stats.describe(values)
  result['mean'] = dstats[2]
  result['variance'] = dstats[3]
  result['skewness'] = dstats[4]
  result['mode'] = stats.mode(values)[0][0]
  result['median'] = numpy.median(values)

  return json.dumps(result)


# return a sorted 
def process_date(values):
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


if __name__ == "__main__":
    main()


