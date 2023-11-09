def sparse_search(data, search_val):
    print("Data: " + str(data)) #"str" converts a variable to an data string(it's nessesary in python)
    print("Search Value: " + str(search_val))
   
    first = 0 #Cero stablish the first position 
    last = len(data) - 1 # To set the last one

    while first <= last:
        mid = (first + last) // 2 #Getting the mid value 
        if not data[mid]:#First, Conditional to check if 'theres no' data or 'fake' data
            left = mid - 1
            right = mid + 1
            while True:
                if left < first and right > last:
                    print("{0} is not in the dataset".format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                right += 1
                left -= 1
        if data[mid] == search_val:#Second. Conditional to check if the target value is in middle
            print("{0} found at position {1}".format(search_val, mid))
            return
        if search_val < data[mid]: #Thirth. check if target if less than our database
            last = mid - 1
        if search_val > data[mid]: #Fourth. Check if target if more than .....
            first = mid + 1

    print("{0} is not in the dataset".format(search_val))




                



