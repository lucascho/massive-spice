from scipy import stats
import json
import numpy

def numericJson(values):
	result = {}
	dstats = stats.describe(values)
	result['mean'] = dstats[2]
	result['variance'] = dstats[3]
	result['skewness'] = dstats[4]
	result['mode'] = stats.mode(values)[0][0]
	result['median'] = numpy.median(values)

	return json.dumps(result)
