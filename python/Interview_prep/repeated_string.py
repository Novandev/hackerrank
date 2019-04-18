

def repeatedString(s, n):
    number_of_a =0
    sentinel = len(s) -1
    str_check = 0
    long_str = ''
    
    # for i in range(n):
    #     if str_check > sentinel:
    #         str_check = 0
    #     if s[str_check] =='a':
    #         number_of_a += 1
    #     long_str += s[str_check]
    #     str_check +=1
    # return number_of_a
    return sum(x == 'a' for x in s) * (n//len(s)) + sum(x == 'a' for x in s[:n%len(s)])
if __name__ == "__main__":
    print(repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
, 7367789))