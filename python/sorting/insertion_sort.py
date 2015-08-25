def list_swap(our_list, low, high):
    insIst[low], insIst[high] = insIst[high], insIst[low]
    return insIst
    pass
    

def insertion_sort(insIst):

    numbers = len(insIst)

    for each in range(numbers - 1): 

        start = each
        minimum = insIst[each]

    
    for index in range(1, len(insIst)):
        candidate = insIst[index]
        comparison_index = index - 1
        while index >= 0:
            if candidate < insIst[comparison_index]:
                list_swap(insIst, comparison_index, comparison_index + 1)
                comparison_index =- 1
            else: 
                break
    return insIst
    pass 



#This type of sort goes through the list and compares the two values that are next to each other. n and n+1. 
#If n+1 is smaller than n, then it swaps the values. Then it moves on to the next position. 

    #create an index of this list

    #iterate through the list while comparing each value in the list to the one before it

    #run the listSwap algorithm on each pair of values from the current to the first    



def insertSort(myList):

   for index in range(1, len(myList)):

     currentvalue = myList[index]
     position = index

     while position>0 and myList[position-1]>currentvalue:
         myList[position]=myList[position-1]
         position = position-1

     myList[position]=currentvalue

myList = [54,26,93,17,77,31,44,55,20]
insertSort(myList)
print(myList)

