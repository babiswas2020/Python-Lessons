import re
print(re.search('abcd','abcdefnc abcd'))
print(re.findall('abcd','abcdefnc abcd'))
print(re.findall('\w\w\w\w','abcdefnc abcd'))
