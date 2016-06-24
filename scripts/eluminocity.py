import urllib2
import time, threading

STATE_FILEPATH = "state.txt" 

# downloads a url and returns a list with it's contents
def getStateFile(url):
    response = urllib2.urlopen(url)
    html = response
    return html

def parse(timestamp, url):
    entry = timestamp
    header = "timestamp"
    state_file = getStateFile(url)
    for line in state_file:
        line_arr = line.rstrip().split(':')
        state = line_arr[0]
        value = line_arr[1]
        header += ','+state
        entry += ',' + value
    entry += '\n'
    header += '\n'
    return entry, header

def initFile(filename, header):
    try:
        fp = open(filename)
    except IOError:
        # If not exists, create the file
        fp = open(filename, 'w+')
        fp.write(header)
        fp.close()

def saveLine(filename, csv):
    f = open(filename, 'a')
    f.write(csv)
    f.close()

def main():
    timestamp = time.ctime()
    csv, header = parse(timestamp, "http://192.168.123.123/rest/full_state")
    saveLine(STATE_FILEPATH, csv)
    threading.Timer(1, main).start() # periodically calls main every 60 seconds
    
if __name__ == '__main__':
    csv, header = parse('',"http://192.168.123.123/rest/full_state")
    initFile(STATE_FILEPATH, header)
    main()