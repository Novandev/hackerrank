

def repeatedString(s, n):
    number_of_a ={'a':0}
    sentinel = len(s) -1
    str_check = 0
    long_str = ''
    
    for i in range(n):
        if str_check > sentinel:
            str_check = 0
        if s[str_check] =='a':
            number_of_a['a'] += 1
        print(s[str_check])
        long_str += s[str_check]
        str_check +=1
        # print(str_check)
    print(long_str)
    return number_of_a['a']

if __name__ == "__main__":
    print(repeatedString('aba', 10))