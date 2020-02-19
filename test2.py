import re


string="Hello brother we are indians we should love our country.Am i right. yes u are right"
print(re.search('\w{3}[\s]',string))
print(re.findall('\w{3}[\s]',string))
print(re.findall('\w?r\s',string))


