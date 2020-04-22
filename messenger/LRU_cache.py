import heapq
from datetime import datetime


class LRUCache:
    def __init__(self, capacity=10):
        self.hashTable = {}
        self.timeQueue = []
        self.capacity = capacity

    def get(self, key):
        try:
            current_time = datetime.now()
            value = self.hashTable[key]
            i = 0
            for item in self.timeQueue:
                if item[1] == key:
                    self.timeQueue.pop(i)
                    heapq.heappush(self.timeQueue, (current_time, key))
                    break
                i += 1

            return value
        except KeyError:
            return ""

    def set(self, key, value):
        current_time = datetime.now()
        try:
            old_value = self.hashTable[key]
            self.hashTable[key] = value

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


    def delete(self, key):
        try:
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


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse') 
    cache.delete('Walter')
    cache.get('Walter')