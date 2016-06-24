import urllib2
import time, threading

STATE_FILEPATH = "state.txt"
EOF = 10

reset_file = 0
last_line_written = 1

# downloads a url and returns a list with it's contents
def getStateFile(url):
    response = urllib2.urlopen(url)
    html = response
    return html

# this is a stub function for testing, use getStateFile instead
def openStateFile(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
    return contents

# converts the file to csv format
def parse(timestamp, url):
    entry = timestamp
    header = "timestamp"
    #state_file = getStateFile(url)
    state_file = openStateFile(url)
    for line in state_file:
        line_arr = line.rstrip().split(':')
        state = line_arr[0]
        value = line_arr[1]
        header += ','+state
        entry += ',' + value
    entry += '\n'
    header += '\n'
    return entry, header

# if the file does not exist, write the header
def initFile(filename, header):
    try:
        fp = open(filename)
    except IOError:
        fp = open(filename, 'w+')
        fp.write(header)
    finally:
        fp.close()

# append a single csv line to state.txt
def saveLine(filename, csv):
    f = open(filename, 'a')
    f.write(csv)
    f.close()

# get the length of a file
def length(filename):
    i = 0
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def rewriteFile(filename, csv):
    global last_line_written
    import fileinput
    for line in fileinput.input(filename, inplace=True):
        if fileinput.lineno() == last_line_written:
            print csv,
            continue
        print line,

def main():
    global reset_file
    global last_line_written

    timestamp = time.ctime()
    #csv, header = parse(timestamp, "http://192.168.123.123/rest/full_state")
    csv, header = parse(timestamp, "full_state")
    initFile(STATE_FILEPATH, header) # only writes once if the file doesn't exist    
    
    reset_file = length(STATE_FILEPATH) # I need to know the number of line in the file in case of a crash
    last_line_written += 1
    if last_line_written == EOF:
        last_line_written = 2

    if (reset_file + 1) == EOF:
        rewriteFile(STATE_FILEPATH, csv)
    else:
        saveLine(STATE_FILEPATH, csv)

    threading.Timer(1, main).start() # periodically calls main every 60 seconds
    
if __name__ == '__main__':
    main()

