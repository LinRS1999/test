import re

string1 = "b'101 103 101 '"
string2 = "b''"

pattern = re.compile(r'[0-9]+')
result = pattern.findall(string2)
print(result)


