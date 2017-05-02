import re
import os


def ignorepattern(line,value):
    if value == 'ctx' or value == 'base':
        return True
    if re.match('.*time', value, flags=re.IGNORECASE):
        return True
    if re.search('items=',line):
        return True
    if re.search('formatNumber',line):
        return True
    return False;


def scapexml(line):
    while re.search('(.*?\$\s*\{(?!\s*fn:escapeXml\())(.*?)(\}.*?)', line):
        l = re.search('(?P<left>.*?\$\s*\{(?!\s*fn:escapeXml\())(?P<value>.*?)(?P<right>\}.*)', line)
        value = l.group('value')
        if ignorepattern(line,value):
            return line
        left = l.group('left')
        right = l.group('right')
        line = '{left}fn:escapeXml({value}){right}'.format(left=left, value=value, right=right)
    return line


def getJsps():
    list_dirs = os.walk('/Users/xuwuqiang/Documents/workspace/cards/src', )
    for root, dirs, files in list_dirs:
        for f in files:
            if f.endswith(".jsp"):
                yield (os.path.join(root, f))


if __name__ == '__main__':
    for file in getJsps():
        try:
            lines = [];
            with open(file) as f:
                print(f.name)
                for line in f:
                    lines.append(scapexml(line))
            with open(file, 'w') as fw:
                for l in lines:
                    fw.write(l)
                    fw.write('\r')
        except Exception as e:
            print(e)
