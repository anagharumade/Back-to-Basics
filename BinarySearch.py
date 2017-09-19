def BinarySearch(arr, search):
    high = len(arr)
    low = 0
    index = ((high - low)//2)
    for i in range(len(arr)):
        if search > arr[index]:
            low = index
            index = index + ((high - low)//2)
            if i == (len(arr)-1):
                print("Number is not present in the input array.")
            else:
                pass
        elif search < arr[index]:
            high = index
            index = (high - low)//2
            if i == (len(arr)-1):
                print("Number is not present in the input array.")
            else:
                pass
        else:
            if arr[index] == search:
                print("Number found at position: ", index)
            break

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,12]
    BinarySearch(arr, 7)
            
