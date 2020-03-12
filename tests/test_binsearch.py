from ds.binsearch import binary_search

def test_binsearch():
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list,3) == 1
    assert binary_search(my_list,13) == None
    