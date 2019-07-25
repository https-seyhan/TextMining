import re
s='my age is 25. I have 55.000 percent marks and 9764135408 is my number'
re.findall('\d+[.]\d\d',s)
if len(re.findall('\d+[.]\d\d+',s)) > 0:
    print("Two Digit Found")
else:
    print("Not Found")
        