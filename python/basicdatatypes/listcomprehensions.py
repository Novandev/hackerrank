
'''

Problem: Given n as a hard uper limit, print the number of cuboid sides n number of times with a,b,c sides of the cuboid being no bigger than n itself
'''

def cuboidFunction(x,y,z,n):
    '''Thus function takes  4 inputs, one from each side of the cuboid and the scalar limit of  each of the inputs defined by n'''
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    # this returns a matrix(list of lists) where each element i the top level list is a list that contains the cuboid deminsions
    return [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ]