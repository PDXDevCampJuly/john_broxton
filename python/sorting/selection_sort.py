# Selection sorting a list
##########################

#This algorithm goes through the entire list and finds the smallest value. Then it compares
#that value to the indexed value in the for loop, and compares the two values. If the greater of the indexed
#values is smaller, then it swaps them out. 

# sort myList into ascending order


def selectSort(myList):

    n = len(myList)

    # For each position in the list (except the very last)

    for bottom in range(n-1):

    # find the smallest item in myList

        mp = bottom # bottom is smallest initially

        for i in range(bottom+1,n): # look at each position

            if myList[i] < myList[mp]: # this one is smaller

                mp = i # remember its index

                # swap smallest item to the bottom

        myList[bottom], myList[mp] = myList[mp], myList[bottom]

    return myList

print(selectSort([4, 6, 3, 8, 2, 0, 1]))