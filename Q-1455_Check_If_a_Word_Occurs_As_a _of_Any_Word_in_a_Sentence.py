sentence = "i love eating burger"
searchWord = "burg"

def isPrefixOfWord(sentence, searchWord):
    value = 0
    for word in sentence.split():
        print(word)
        value += 1
        if searchWord in word:
            if atStart(word, searchWord):
                return value
        
def atStart(word, searchWord):
    word = word[:len(searchWord)]
    if word == searchWord:
        print(True)
        return True
    else: 
        print(False)
        return False
        
