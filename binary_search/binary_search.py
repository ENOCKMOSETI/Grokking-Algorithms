# binary search searches through a sorted list of items and returns the index of an item.
# it achieves this by repeatedly dividing the list in the half containing the item until
# it's narrowed down all possible locations to just one

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1,2,3,4,6,8,9,45,67, 111]

    print(binary_search(my_list, 110))
    print(binary_search(my_list, 45))