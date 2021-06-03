
def linear_search(arr, search_item):

    # Iterate through each element of the array
    for i in range(len(arr)):

        # Check if element matches with search item
        if arr[i] == search_item:
            return i   
    return -1

if __name__ == "__main__":
    test_arr = [2, 3, 6, 10]
    x = 6    
    res = linear_search(test_arr, x)
    if res != -1:
        print(f"Element is present at index {res}")
    else:
        print("Element NOT found")
