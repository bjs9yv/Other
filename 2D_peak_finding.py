# return a local peak in a 2D array
def find_peak(a):
    if len(a) <= 3:
        return max(a) 
    middle = len(a)/2
    left_lower = a[middle] > a[middle-1]
    right_lower = a[middle] > a[middle+1]
    if left_lower and right_lower:
        # peak found
        return a[middle]
    elif left_lower and not right_lower:
        # upward sloping, peak to the right
        find_peak(a[middle:])
    elif not left_lower and right_lower:
        # downward sloping, peak to the left
        find_peak(a[:middle])
    else:
        # valley, peak on either side, pick right
        return find_peak(a[middle:])
    

if __name__ == "__main__":
    print find_peak([1,2,1,11,33])
