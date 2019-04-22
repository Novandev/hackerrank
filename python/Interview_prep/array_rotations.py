"""
Array rotations are all about shifting elements down from  the end to the beginning. I ahve a feeling i should start at the back

Example  4 rotations
Beginning : [1,2,3,4,5]
After 1st rotation: [2,3,4,5,1]
After rotation :[5,1,2,3,4]

"""

def array_rotation(a_list: list,  n: int) -> list:
    for i in range(n):
        for i in range(1,len(a_list)):
            a_list[i -1], a_list[i] = a_list[i],a_list[i -1]
    return(a_list)




if __name__ == "__main__":
    print(array_rotation([1, 2, 3, 4, 5], 4))