class lin_search:
    def linear_search(item,list):
        found=False
        position=0
        searchvalue=0
        while(position<len(list) and found==False):
            searchvalue = searchvalue+1
            if(list[position]== item):
                found=True
            else:
                position=position+1
        if (found is False):

            list.append(item)
            found_add= True
            position=position+1
        return found,position,searchvalue,found_add

#test
if __name__ == "__main__":
    mylist = ["jaya","lakshmi","c"]
    myitem = input("what item do you want to find\n")
    IsItFound,position,count,found_add= lin_search.linear_search(myitem,mylist)

    print("searched for ",count,"counts")
    if IsItFound is True:
        print("Found the item in list")
    elif found_add is True:
        print("item not found in the list\n wait ! we added it to the list\n")
    else:
        print("Item nor found in the list")
    print("position is : ", position)
    print("Thank you !!")