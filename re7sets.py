import re
str1="hello 123"
print(re.findall('[a-z]', str1))
print(re.findall('[^a-z]', str1))
print(re.findall('[e|o]', str1))
print(re.findall('[012]', str1))
print(re.findall('[a-z0-9]', str1))
print(re.findall('[aeo]', str1))
print(re.findall('[0-9]', str1))
print(re.findall('[0-9][0-9][0-9]', str1))