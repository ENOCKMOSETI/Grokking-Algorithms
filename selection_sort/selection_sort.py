# selection sort searches a list of items, finds the smallest value, removes it and appends it to another
# list, the end result is a sorted list

def find_smallest(arr):
    smallest_index = 0
    smallest_value = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_index = i
            smallest_value = arr[i]
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

if __name__ == '__main__':
    print(selection_sort([3, 4, 6, 2, 90, -1]))