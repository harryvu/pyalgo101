from ds.SinglyLinkedList import SinglyLinkedList
import pytest

@pytest.fixture
def words():
    return SinglyLinkedList()

def test_insert_new_node_to_an_empty_list(words):
    words.insert('hello')

    assert words.head.data == 'hello'
    assert words.tail.data == 'hello'
    assert words.count == 1

def test_insert_new_nodes_to_an_empty_list(words):
    words.insert('world')
    words.insert('ALGO')
    words.insert('hello')

    assert words.count == 3
    assert words.head.data == 'hello'
    assert words.tail.data == 'world'

def test_append_new_node_to_an_empty_list(words):
    words.append('hello')

    assert words.head.data == 'hello'
    assert words.tail.data == 'hello'
    assert words.count == 1
    