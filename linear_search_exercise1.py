def linear_search(item,list):
    found=False
    position=0
    while(position<len(list) and found==False):
        if(list[position]== item):
            found=True
        else:
            position=position+1
    return found

#test
if __name__ == "__main__":
    mylist = ["jaya","lakshmi","c"]
    myitem = input("what item do you want to find")
    IsItFound = linear_search(myitem,mylist)
    if IsItFound is True:
        print("Found the item in list")
    else:
        print("Item nor found in the list")