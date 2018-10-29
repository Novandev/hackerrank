"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array a[]  of n integers each separated by a space.
"""
n = int(input())    # Collect n as an input


arr = [input() for _ in range(n)]   # For each time that n runs collect an input


arr.sort()  # Sort the array

# print(arr)

runner_up = arr[len(arr)-2]

print(runner_up)