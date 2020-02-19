import re
print(re.search('\w\w\w\w','ab_cd efgh'))
print(re.findall('\w\s\w\w\w','ab_cd efgh'))
print(re.findall('\w\w\w','ab.bcd'))
print(re.findall('\w\w\W','ab.bcd'))

