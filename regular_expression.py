# password checker
# 8 charachters long at least
# containy any letters, numbers and '$%#@'

import re

pattern = re.compile(
    r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%  # @!])[A-Za-z\d$%#@!]{8,}$')

string = '!Jimmos5!%'
badstring = '!@#$@%(_^)&_!@#'

find1 = pattern.search(string)
find2 = pattern.search(badstring)

print(find1.group())

if find2 == None:
    print('please input a good password')
