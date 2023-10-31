def TryConversionToInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def GetOnlyIntInput(text):
    nbr_str = input(f"\n{text} :")    
    while(TryConversionToInt(nbr_str)==False):
        nbr_str = input("\nInvalide!!\ nsaisie un chiffre entier :")
    return nbr_str

def isPalindrome(word):
    charList = list(word)
    charListReversed = charList[::-1]
    reversedWord = "".join(charListReversed)
    
    return word == reversedWord
