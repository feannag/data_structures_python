class HashTable:
    def __init__(self):
        self.list_size = 10
        self.items = [None] * self.list_size
        self.number_of_items = 0
        self.max_load_factor = 0.75

    def __rehash(self):
        temp_list = self.__backup()

        self.list_size = self.list_size * 2
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
                return True

            index = (index + 1) % len(self.items)

        return False

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
            self.__rehash()
            self.add(item)


def main():
    hs = HashTable()

    items = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'indiana', 'juliet', 'kilo', 'lima', 'maverick', 'nancy', 'oscar', 'papa', 'quebeck', 'romeo', 'sierra', 'tango', 'uniform', 'victory', 'whiskey', 'xray', 'yankee', 'zulu']

    for item in items:
        hs.add(item)

    items.append('raptor')
    items.append('eagle')
    items.append('falcon')
    for item in items:
        if hs.contains(item):
            print(f"hashtable contains {item}")
        else:
            print(f"hashtable doesn't contains {item}")


if __name__ == "__main__":
    main()
