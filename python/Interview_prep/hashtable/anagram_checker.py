"""
Two string are anagrams if the letters of one string can be used to form another

"""

def anagram_checker(s1: list, s2: list) -> bool:
    return [s1.count(x) for x in s1] == [s2.count(x) for x in s2]



if __name__ =="__main__":
    print(anagram_checker('boop', 'poob'))