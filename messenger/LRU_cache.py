import heapq
from datetime import datetime


class LRUCache:
    def __init__(self, capacity=10):
        self.hashTable = {}
        self.timeQueue = []
        self.capacity = capacity

    def get(self, key):
        try:
            print("get key:{0}".format(key))
            current_time = datetime.now()
            value = self.hashTable[key]
            i = 0
            for item in self.timeQueue:
                if item[1] == key:
                    self.timeQueue.pop(i)
                    heapq.heappush(self.timeQueue, (current_time, key))
                    break
                i += 1

            print(self.hashTable)
            print(self.timeQueue)

            return value
        except KeyError:
            return ""

    def set(self, key, value):
        print("set key:{0}, value: {1}".format(key, value))
        current_time = datetime.now()
        try:
            old_value = self.hashTable[key]
            self.hashTable[key] = value
            print('key is already there')

            i = 0
            for item in self.timeQueue:
                if item[1] == key:
                    self.timeQueue.pop(i)
                    heapq.heappush(self.timeQueue, (current_time, key))
                    break
                i += 1

        except KeyError:
            if len(self.hashTable) < self.capacity:
                self.hashTable[key] = value
                heapq.heappush(self.timeQueue, (current_time, key))
            else:
                deleted_key = heapq.heappop(self.timeQueue)
                self.hashTable.pop(deleted_key)
                self.hashTable[key] = value
                heapq.heappush(self.timeQueue, (current_time, key))

        print(self.hashTable)
        print(self.timeQueue)


    def delete(self, key):
        try:
            print("delete key: {0}".format(key))
            self.hashTable[key]
            self.hashTable.pop(key)
            i = 0
            for item in self.timeQueue:
                if item[1] == key:
                    self.timeQueue.pop(i)
                    break
                i += 1
        except KeyError:
            pass
        print(self.hashTable)
        print(self.timeQueue)


if __name__ == "__main__":
    print("start")
    cache = LRUCache(3)
    print("init success")
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse') 
    cache.delete('Walter')
    cache.get('Walter')