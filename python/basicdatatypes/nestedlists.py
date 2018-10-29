"""

The first line contains an integer n,  the number of students.
The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
Sample input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

n = int(input())


def input_helper(name,score):   # Using an input helper for making code modular

    return[name, score]


scores = [input_helper(input(), float(input())) for _ in range(n)]     # Takes the name and the score and puts them intp a list that is packed into a list

scores.sort()   # Sort the names and score matrix

second_lowest = [scores[1]]     # The second lowest will always be at index 1 for the first one no matter what

# This part checks for any scores after the lowest one and if ther are equal to the second lowest we put them into a list
for i in range(len(scores)-2):

    if scores[i][1] == second_lowest[0][1]:
        second_lowest.append(scores[i])

print(sorted(second_lowest))    # Sorts this list