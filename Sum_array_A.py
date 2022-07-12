# Problem
# You are given an array A consisting of N integers. 

# Task

# Print the sum of the elements in the array. 

# Note: Some of the integers may be quite large.

# Input Format

# The first line contains a single integer N denoting the size of the array.  
# The next line contains space-separated integers denoting the elements of the array.
# Output format

# Print a single value representing the sum of the elements in the array.

# Constraints

# 1<=N<=10

# 0<=a[i]<=10^10

# Sample Input
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Sample Output
# 5000000015


N = int(input())
while N < 1 or N > 10:
    N = int(input("Enter integer N(between 1 and 10, inclusive): "))
A = list(map(int, input().split()))
i =int()
while N != len(A) and (A[i] < 0 or A[i] > 10^10):
    A = list(map(int, input("Enter space-separated " + str(N) + " integers , between 0 and 10^10 : ").split()))
#Sum = int()
print(sum(A))