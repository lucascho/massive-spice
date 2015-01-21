import numpy, scipy
from scipy import stats
import json, datetime, collections, pprint

INPUT_TIMEFORMAT = "%Y-%m-%d"
BACKUP_INPUT_TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
OUTPUT_TIMEFORMAT = "%Y-%m"


"""
data = {
  
  status1 : {
    field1.1 : [
      {type:type1, values:[]}
    ]
    field1.2 : []
  }
  status2 : {
    field2.1
    field2.2
  }
}
"""
def main(debug=True):
  output = {}
  DATATYPEMAP = {
    "string":process_text,
    "numeric":process_numerics,
    "date":process_date
  }
  f = open('../data/dump.json')
  out = open('../data/output.json', 'w')
  data = json.load(f)
  for status in data:
    output[status] = dict()
    for field in data[status]:

      if field == "count":
          output[status]['count'] = data[status][field]
          continue
      field_data = data[status][field]
      data_type = field_data["type"]
      values = field_data["values"]

      functionToRun = None
      try:
        functionToRun = DATATYPEMAP[data_type]
      except KeyError:
        print "Data type %s is not valid" % (data_type)
        exit()
      output[status][field] = functionToRun(values)
      """
      if data_type=="string":
        out.write(process_text(values))
      
      elif data_type=="numeric":
        out.write(process_numerics(values))
      
      else: 
        out.write(process_date(values))
      """
  jsonString = json.dumps(output)
  out.write(jsonString)
  if debug:
      pp = pprint.PrettyPrinter(indent=2)
      pp.pprint(output)
  out.close()
  f.close()

# return an array of numeric values indicating similarity between two fields
def process_text(values):
  dic = {}
  for phrases in values:
    if phrases is None:
        continue
    for w in phrases.split():
      if w not in dic:
        dic[w] = 1
      else: 
        dic[w] += 1

  #return sorted(dic, key=dic.get)
  return sorted(dic.items(), key=lambda x: x[1], reverse=True)

# return True if the field value matches 
def run_text_matching(values):
  return


# return a numeric summary of the values
def process_numerics(values):
  cleanedList = []
  for value in values:
    if value is not None:
        cleanedList.append(float(value))
  values = cleanedList
  if len(values) == 0:
      return {'mean':0, 'variance':0, 'skewness':0, 'mode':0, 'median':0}
  result = {}
  dstats = stats.describe(values)
  result['mean'] = dstats[2]
  result['variance'] = dstats[3]
  result['skewness'] = dstats[4]
  result['mode'] = stats.mode(values)[0][0]
  result['median'] = numpy.median(values)

  return result


# return a sorted 
def process_date(values):
    outputDict = {}
    for value in values:
        if not value:
            try:
              outputDict['null']
            except KeyError:
                outputDict['null'] = 0
            outputDict['null'] += 1
            continue
        if value.find("0000") == 0:
            try:
              outputDict['null']
            except KeyError:
                outputDict['null'] = 0
            outputDict['null'] += 1
            continue
        dateObj = None
        try:
          dateObj = datetime.datetime.strptime(value, INPUT_TIMEFORMAT)
        except ValueError:
          dateObj = datetime.datetime.strptime(value, BACKUP_INPUT_TIMEFORMAT)
        nearestMonth = datetime.datetime.strftime(dateObj, OUTPUT_TIMEFORMAT)
        try:
            outputDict[nearestMonth]
        except KeyError:
            outputDict[nearestMonth] = 0
        outputDict[nearestMonth] += 1     
    return sorted(outputDict.items())


if __name__ == "__main__":
    main()


