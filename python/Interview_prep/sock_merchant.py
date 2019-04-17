"""
This fucntion wlll count the numer of pairs of socks in an array that denotes colors
"""

def sock_counter(sock_list:list) -> list:
    sock_dict = {}
    for sock in sock_list:
        if sock not in sock_dict:
            sock_dict[sock] = 0
        sock_dict[sock] += 1

    return [sock for sock in sock_dict if sock_dict[sock] == 2 ]

if __name__ == "__main__":
    print(sock_counter([1,2,1,2,1,4,5,6,3]))