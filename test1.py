import re
string="Hello Brother What are you doing\n The body is er lying on the table\n How are you other dancer"
print(re.search('ot',string))
print(re.findall('ot',string))
print(re.findall('\w*er[\s]',string))






