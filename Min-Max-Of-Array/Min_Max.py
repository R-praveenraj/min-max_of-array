#Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

def min_max(array):
    maxi=-float('inf')
    mini=float('inf')
    for i in array:
        if maxi<i:
            maxi=i
        elif mini>i:
            mini=i
    
    return maxi+mini




array = [-2, 1, -4, 5, 3]
print(min_max(array))