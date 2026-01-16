from typing import Dict, Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len = 0
        self.cache: Dict[int, Node] = {}
        self.head: Node = Node(-1, -1)
        self.tail: Node = Node(-1, -1)

        self.head.prev = self.tail
        self.tail.next = self.head

    def append_node(self, node: Node) -> None:
        self.cache[node.key] = node
        self.head.prev.next = node
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev = node

    def remove_node(self, node: Node) -> None:
        self.cache.pop(node.key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if node := self.cache.get(key):
            self.remove_node(node)
            self.append_node(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if node := self.cache.get(key):
            node.value = value
            self.remove_node(node)
            self.append_node(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            if self.len == self.capacity:
                assert self.tail.next is not None
                self.remove_node(self.tail.next)
                self.len -= 1
            self.append_node(node)
            self.len += 1


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.cache)
    print(cache.head.prev.key, cache.head.prev.value)
    print(cache.tail.next.key, cache.tail.next.value)
    print("")

    res = cache.get(1)
    print(cache.head.prev.key, cache.head.prev.value)
    print(cache.tail.next.key, cache.tail.next.value)
    print(cache.cache)
    print(res)
    print("")

    cache.put(3, 3)
    print(cache.head.prev.key, cache.head.prev.value)
    print(cache.tail.next.key, cache.tail.next.value)
    print(cache.cache)

    res = cache.get(2)
    print(res)
    cache.put(4, 4)
    res = cache.get(1)
    print(res)
    res = cache.get(3)
    print(res)
    res = cache.get(4)
    print(res)
