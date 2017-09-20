def BubbleSort(arr):
    swap = True
    while swap == True:
        count = 0
        for j in range(0, (len(arr)-1)):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            else:
                count += 1
                if count == (len(arr)-1):
                    swap = False
                else:
                    pass
        print(arr)

if __name__ == "__main__":
    arr = [23, 4, 51, 12, 1, 0, 9, 100]
    BubbleSort(arr)
