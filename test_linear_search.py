from unittest import TestCase
from linearsearch import lin_search

class TestLinear_search(TestCase):
    mylist = ["jaya", "lakshmi", "c"]
    myitem = "jaya"
    IsItFound = lin_search.linear_search(myitem, mylist)
    if IsItFound is True:
        print("Found the item in list:",myitem)
    else:
        print("Item nor found in the list:",myitem)
    pass
    myitem="sreejith"
    IsItFound = lin_search.linear_search(myitem, mylist)
    if IsItFound is True:
        print("Found the item in list:",myitem)
    else:
        print("Item nor found in the list:",myitem)
    pass
if __name__ == '__main__':
    unittest.main()