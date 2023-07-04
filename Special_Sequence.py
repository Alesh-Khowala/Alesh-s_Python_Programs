import re 

txt = "The brain is in pain"

# x = re.search("\Abrain", txt)
# x = re.search(r"\bpai", txt)
# x = re.search("\d", txt)
x = re.findall("\D", txt)
print(x)