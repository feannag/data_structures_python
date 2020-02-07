import logging
from typing import List
from random import randint


def get_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    return logger


class HashTable:
    logger = get_logger()

    def __init__(self):
        self.list_size = 10
        self.items = [None] * self.list_size
        self.number_of_items = 0
        self.max_load_factor = 0.75

    def __rehash(self, factor):
        temp_list = self.__backup()

        self.list_size = int(self.list_size * factor)
        self.items = [None] * self.list_size
        self.number_of_items = 0

        for item in temp_list:
            self.add(item)

    def __backup(self):
        temp_list = []

        for item in self.items:
            if item is not None:
                temp_list.append(item)

        return temp_list

    def contains(self, item):
        index = hash(item) % len(self.items)

        while self.items[index] is not None:
            if self.items[index] == item:
                return [True, index]

            index = (index + 1) % len(self.items)

        return False

    def remove(self, item):
        item_info: List[bool, int] = self.contains(item)

        if item_info[0] is True:
            self.items[item_info[1]] = HashTable.__Placeholder()
            self.number_of_items -= 1
            print(f'removed {item}')

        load_factor = self.number_of_items / len(self.items)
        if load_factor < 0.25:
            self.__rehash(0.5)

    def add(self, item):
        load_factor = self.number_of_items / len(self.items)
        if load_factor <= self.max_load_factor:
            index = hash(item) % len(self.items)

            while self.items[index] is not None:
                if self.items[index] == item:
                    return False

                index = (index + 1) % len(self.items)

            self.items[index] = item
            self.number_of_items += 1
        else:
            self.__rehash(2)
            self.add(item)

    class __Placeholder:
        def __init__(self):
            pass


def main():
    # instantiate hash table and items
    hs = HashTable()
    items = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'indiana', 'juliet', 'kilo', 'lima', 'maverick', 'nancy', 'oscar', 'papa', 'quebeck', 'romeo', 'sierra', 'tango', 'uniform', 'victory', 'whiskey', 'xray', 'yankee', 'zulu']

    # add items to hash table
    for item in items:
        hs.add(item)

    # test presence of invalid items
    items.append('raptor')
    items.append('eagle')
    items.append('falcon')
    for item in items:
        if hs.contains(item):
            print(f"hashtable contains {item}")
        else:
            print(f"hashtable does not contain {item}")

    # remove items from hash table
    for item in items[0:20]:
        hs.remove(item)

    # instantiate hash table and items
    hs = HashTable()
    items = [randint(0, 200) for i in range(0, 30)]
    print(f"items: {items}")

    # add items to hash table
    for item in items:
        hs.add(item)

    # validate the hash table
    for item in items:
        if hs.contains(item):
            print(f"hashtable contains {item}")
        else:
            print(f"hashtable does not contain {item}")

    #  remove items from hash table
    for item in items[0:20]:
        hs.remove(item)


if __name__ == "__main__":
    main()
