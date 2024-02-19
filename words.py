def printUpperWords(words):
    for word in words:
        print(word.upper())

def printUpperWords2(words):
    for word in words:
        if word.startsWith("e") or word.startsWith("E"):
            print(word.upper())

def printUpperWords3(words, mustStartWith):
    for word in words:
        for letter in mustStartWith:
            if word.startsWith(letter):
                print(word.upper())
                break