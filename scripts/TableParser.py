'''
  This script needs BeautifulSoup 3 and Python 2.x in order to work.
  Python 3.x and BeautifulSoup 4 are not supported!
'''

from BeautifulSoup import BeautifulSoup

class TableParser:
    '''
        Class to parse the index.html from eluminocity charging station. 
        This will return a file much like the one in rest/full_state which
        can then be used with the main script. 
    '''
    def __init__(self, html):
        self._soup = BeautifulSoup(html)
        self._contents = ""

    def convert_to_var(self, inp):
        return '_'.join(inp.lower().split(' '))

    def parse(self):
        for tr in self._soup.findAll("tr"):
            td_list = tr.findAll("td")
            if len(td_list) == 2:
                name = td_list[0].text
                value_tag = td_list[1]
                line = ""
                if value_tag.findAll():
                    for tag in value_tag.findAll(recursive=False):
                        opts = tag.find("option", selected=True)
                        if opts is not None:
                            line = name+":"+opts.text
                        elif tag.name == 'input' and tag["type"] == "radio":
                            if tag.has_key('checked'):
                                if tag.has_key('value'):
                                    line = name+":"+tag['value']
                        elif tag.name == 'input' and tag["type"] == 'text':
                            if tag.has_key('value'):
                                line = name+":"+tag['value']
                else:
                    line = name+":"+value_tag.text
                self._contents += self.convert_to_var(line) + '\n'
        return self._contents

if __name__ == '__main__':
    with open("index.html", 'r') as f:
        ifile = f.read()
    tp = TableParser(ifile)
    print tp.parse()