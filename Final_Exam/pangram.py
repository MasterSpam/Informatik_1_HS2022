
def is_perfect_pangram(string, alphabet=None):
    if not alphabet:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    short_string = ''.join(e.lower() for e in string if e.isalpha())
    for char in short_string:
        if char.lower() not in alphabet:
            return False
        alphabet= alphabet.replace(char.lower(), "")

    if not alphabet:
        return True
    return False

print( is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx") )
print( is_perfect_pangram("a b c", "abc") )
print( is_perfect_pangram("azbzc", "abc") )
print( is_perfect_pangram("abc", "abcd") )
print( is_perfect_pangram("abb", "abc") )