import json
import sys
from collections import defaultdict
def main():
    file = open(sys.argv[1])
    bizToTupleDict = defaultdict(list)
    for line in file:
        review = json.loads(line)
        biz = review[u'business_id']
        date = review[u'date']
        votes = review[u'votes']
        bizToTupleDict[biz].append([date,votes])
    print bizToTupleDict.values()
    print [sorted(x, key=lambda tup:tup[0]) for x in\
                          bizToTupleDict.values()]
    return
    list_funny = map(lambda x: sum(x)/float(len(x)) , zip(lambda x: sorted(x, key=lambda tup:tup[0]),\
                                           bizToTupleDict.values()))
    print list_funny
if __name__=='__main__':
    main()
