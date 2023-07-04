import re

txt = "hello and, Welcome to python, cool and care"
# x = re.search("[a-b]", txt)
# x = re.search("c..e", txt)
# x = re.search("python", txt)
# x = re.search("care$", txt)
# x = re.search("c.{2}]", txt)
x = re.search("and|hello", txt)
print(x)
