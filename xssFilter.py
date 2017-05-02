import re


def scapeXml(line,ignoreFn):
    while re.search('(.*?\$\s*\{(?!\s*fn:escapeXml\())(.*?)(\}.*?)', line):
        l = re.search('(?P<left>.*?\$\s*\{(?!\s*fn:escapeXml\())(?P<value>.*?)(?P<right>\}.*)', line)
        value = l.group('value')
        left = l.group('left')
        right = l.group('right')
        line = '{left}fn:escapeXml({value}){right}'.format(left=left, value=value, right=right)
    return line


if __name__ == '__main__':
    line = 'abc${ das }$ {(abc)},${ fn:escapeXml(string1)},${haha}aaa'

    l = scapeXml(line,ignoreFn=lambda x : x == 'base')
    print(l)
