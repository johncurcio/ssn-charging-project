import urllib2
import time, threading

# downloads a url and returns a list with it's contents
def getStateFile(url):
    response = urllib2.urlopen(url)
    html = response
    return html

def parse(timestamp, state_file):
    entry = timestamp
    for line in state_file:
        line_arr = line.rstrip().split(':')
        state = line_arr[0]
        value = line_arr[1]
        entry += ',' + value
    entry += '\n'
    return entry

def saveLine(filename, csv):
    f = open(filename, 'a')
    f.write(csv)
    f.close()

def main():
    timestamp = time.ctime()
    state_file = getStateFile("http://192.168.123.123/rest/full_state")
    csv = parse(timestamp, state_file)
    saveLine('state.txt', csv)
    threading.Timer(10, main).start() # periodically calls main every 60 seconds
    
if __name__ == '__main__':
    main()