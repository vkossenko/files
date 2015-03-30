__author__ = 'Vasiliy'

import os
import argparse
import matplotlib.pyplot as plot

def params():
    """Import parameters from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-rd', '--root_dir', required=True, dest='root_dir',
                        help='Enter directory to scan')
    parser.add_argument('-kw', '--keyword', required=True, dest='keyword',
                        help='Enter keyword to search')
    args = parser.parse_args()
    location = args.root_dir
    pattern = args.keyword
    return location, pattern

where = (params()[0])
what = (params()[1])

def search(filename, what):
    """Read file and search string, return True if found"""
    with open(filename, 'r') as inFile:
        for line in inFile:
            if what in line:
                inFile.close()
                return True
    return False

def traverse(where):
    "Search directory&files,return dictionary with key = directory,value = number of files that include searched string"
    result = {}
    for dirName, subdirList, fileList in os.walk(where):
#        print('Found directory: %s' % dirName)
        for fname in fileList:
#            print('\t%s' % fname)
            count = 0
            filepath = (os.path.join(dirName, fname))
            found = search(filepath, what)
            if found:
                if result.has_key(dirName):
                    newcount = result.get(dirName)
                    newcount += 1
                    result.update({dirName: newcount})
                else:
                    count += 1
                    result.update({dirName: count})
    return result

results = traverse(where)
print results

"Build output graph with a plot with X as subdir name string, Y as count values"
plot.bar(range(len(results)), results.values(), align='center')
plot.xticks(range(len(results)), results.keys())
plot.show()
