
mystring = "reset"
otherString = "sters"

characters = list(mystring)
anagramer = list(otherString)

def countChar(list:list, anagram:list):
    count = 0
    if len(list) != len(anagram):
        print("not anagrams")
        return 0
    else:
        for i in range(len(list)):
            item1 = list[i]
            for k in range(len(anagram)):
                print(item1, anagram[k])
                if item1 == anagram[k]:
                    count += 1
                    
                    break
                else:
                    pass
        if count == len(list):
            print("anagrams :)")
            return 0
        else:
            print("not anagrams")
            return 0

countChar(characters, anagramer)