Word=input("Please write any english word  ")

vowel=0

for a in Word:
    for a in a:
        vowel=vowel+1

for i in Word:
    for i in i:
        vowel=vowel+1

for e in Word:
    for e in e:
        vowel=vowel+1

for o in Word:
    for o in o:
        vowel=vowel+1 
for u in Word:
     for u in u:
        vowel=vowel+1

print(vowel// Word(length))







string = input('Enter string: ')
string = string.lower()
vowelcount = 0
consonantcount = 0
for s in string :
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' :
        vowelcount += 1
    else: 
        consonantcount +=1 
print('number of vowels : ',vowelcount,'\nnumber of consonants : ',consonantcount)
