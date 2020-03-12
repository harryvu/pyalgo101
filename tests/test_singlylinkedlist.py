from ds.SinglyLinkedList import SinglyLinkedList

def test_insert_new_node_to_an_empty_list():
    words = SinglyLinkedList()
    words.insert('hello')

    assert words.head.data == 'hello'
    assert words.tail.data == 'hello'
    assert words.count == 1

def test_append_new_node_to_an_empty_list():
    words = SinglyLinkedList()
    words.append('hello')

    assert words.head.data == 'hello'
    assert words.tail.data == 'hello'
    assert words.count == 1
    