# https://leetcode.com/problems/stock-price-fluctuation/
# tags: #data_stream, #design, #google, #hash_table, #heap, #ordered_set
#
# Solution: Heap + Dictionary
# Designing the class we will initialize the following variables:
# * current_timestamp: Latest timestamp based on the data stream.
# * timestamp_price: Dictionary which will store the latest value per timestamp coming from the data stream.
# * min_prices, max_prices: min/max heaps respectively to store (price, timestamp) tuples sorted by price.
# In the update function, we will update the timestamp price and insert (price, timestamp) in both
# the min and max heap to keep track of the min/max values
# Eventually, when minimum or maximum method is called we will retrieve the first value
# of the heap accordingly, if the value is not the latest value that came from the stream
# then we remove that value from the heap.
# Time complexity : O(n*log(n)), Space complexity: O(n)
import heapq


class StockPrice:

    def __init__(self):
        self.current_timestamp = None
        self.timestamp__price = dict()
        self.min_prices = []  # heap
        self.max_prices = []  # heap

    def update(self, timestamp: int, price: int) -> None:
        if not self.current_timestamp or self.current_timestamp < timestamp:
            self.current_timestamp = timestamp

        heapq.heappush(self.min_prices, (price, timestamp))
        heapq.heappush(self.max_prices, (-price, timestamp))

        self.timestamp__price[timestamp] = price

    def current(self) -> int:
        return self.timestamp__price.get(self.current_timestamp, 0)

    def minimum(self) -> int:
        price, timestamp = self.min_prices[0]

        while price != self.timestamp__price[timestamp]:
            heapq.heappop(self.min_prices)
            price, timestamp = self.min_prices[0]

        return price

    def maximum(self) -> int:
        price, timestamp = self.max_prices[0]

        while -price != self.timestamp__price[timestamp]:
            heapq.heappop(self.max_prices)
            price, timestamp = self.max_prices[0]

        return -price


if __name__ == '__main__':
    sp = StockPrice()
    sp.update(1, 10)
    sp.update(2, 5)
    print(sp.current())  # 5
    print(sp.maximum())  # 10
    sp.update(1, 3)
    print(sp.maximum())  # 5
    sp.update(4, 2)
    print(sp.minimum())  # 2
