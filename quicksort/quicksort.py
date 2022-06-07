# quicksort is a sorting algorithm, much faster than selection sort 
# it uses divide and conquer technique
# d&c technique creates a pivot in a list dividing the list into 
# subparts that are sorted individually then finally combine the subparts

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    print(quicksort([12, 21, 34, 2, 3, 1, 5, -1]))