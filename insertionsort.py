class insertion_sort:
    def insetionSort(List):
        for i in range(1,len(List)):
            j=i
            while(j>0 and List[j-1]>List[j]):
                temp = List[j]
                List[j]=List[j-1]
                List[j-1]=temp
                j=j-1

        return List


#test
if __name__ == "__main__":
    mylist = [0,3,6,2,4,2,9]
    print (mylist)

    SortedList= insertion_sort.insetionSort(mylist)

    print("Sorted List ",mylist)
    print("Thank you !!")