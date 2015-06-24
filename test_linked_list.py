
import linked_list

@pytest.fixture
def full_list():
    list = LinkedList()
    list.insert(5)
    list.insert(10)
    return list


def test_empty_list():
    list = LinkedList()
    assert isinstance(list, LinkedList)


def test_insert():
    list = LinkedList()
    list.insert(5)
    assert list.head.value == 5


def test_pop(full_list):
    assert full_list.pop() == 10


def test_size(full_list):
    assert full_list.size == 2


def test_search(full_list):
    assert full_list.search(5).value == 5


def test_remove(full_list):
    node = full_list.search(5)
    full_list.remove(node)
    assert full_list.search(5) is None


def test_display(full_list):
    assert full_list.display() = (10, 5)
