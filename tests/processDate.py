import json
from app.processDate import processDate

TESTFILE = "/tmp/dump.json"

def main():
    fh = open(TESTFILE, 'r')
    jsonData = json.load(fh)
    fh.close()
    status = 'Closed Won'
    field = 'date_closed'
    print jsonData.keys()
    print "type is %s" % (jsonData[status][field]['type'])
    counts = processDate(jsonData[status][field]['values'])
    print counts

if __name__ == "__main__":
    main() 
