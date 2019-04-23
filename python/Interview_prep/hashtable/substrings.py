"""
This function wiill take two strings and see if one string is a substring of the other

"""
class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}

def substring_checker_no_set(s1: list,s2: list) -> str:
    s1_dict = {x.lower():s1.count(x) for x in s1}
    s2_dict = {x.lower():s2.count(x) for x in s2}
    for letter in s1:
        if letter in s2:
            print("YES")
            return
    print("NO")
def substring_checker_set(s1: list,s2: list) -> str:
    if set(s1) & set(s2):
        return("YES")
    return("NO")

        

if __name__ == "__main__":
    substring_checker_no_set('worldp','hio')
    print(substring_checker_set('boon','boom'))