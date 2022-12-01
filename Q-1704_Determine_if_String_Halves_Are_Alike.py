s = "Uo"

lenght = len(s)


s1 = s[int(lenght/2):]
s2 = s[:int(lenght/2)]

def findVower(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    sentence = sentence.lower()
    vowelCount = 0
    
    for word in sentence:
        if word in vowels:
            vowelCount += 1
    return vowelCount

if findVower(s1) == findVower(s2):
    print(True)
else: print(False)