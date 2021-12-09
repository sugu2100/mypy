import re

data = '''
    kim 871212-1234567
    lee 770707-2345678
'''

p = re.compile("(\d{6})[-]\d{7}")
print(p.sub("\g<1>-*******", data))

