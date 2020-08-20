"""
I had to make a custom class because of the fact that we needed to support the sorting of the items by name in descending order as well and I had no idea how else to do it besides creating a class and overriding the less than comparator.
Anyway, this needs more test cases so feel free to test it out and leave feedback.
To me, it seems like an extremely annoying version of your run of the mill 'Top K' questions.
If anyone has a cleaner way to support the descending string order in heapq please let me know!

Time Complexity: Nlog(K) where N = # of items and K = (page_num+1)*items_per_page
Space Complexity: O(K) to store heap -- technically I guess you could say O(N) if you consider the item class nodes, but a lot of times I see these aren't considered on LC.
"""

import heapq

class Item:
    def __init__(self, name, relevancy, price, sort_parameter, sort_order):
        self.name = name
        self.relevancy = relevancy
        self.price = price
        self.sort_parameter = sort_parameter
        self.sort_order = sort_order

    def __lt__(self, other):
        if self.sort_parameter == 0:
            if self.sort_order == 0:
                return self.name < other.name
            else:
                return self.name > other.name
        elif self.sort_parameter == 1:
            return self.relevancy < other.relevancy
        else:
            return self.price < other.price


def items_per_page(num_of_items, items, sort_parameter, sort_order, items_per_page, page_number):
    ret = []
    k = (page_number + 1) * items_per_page
    heap = []

    # limit heap size to top k items
    for item in items:
        if sort_order == 1 and sort_parameter != 0:
            heapq.heappush(heap, Item(item[0], -item[1], -item[2], sort_parameter, sort_order))
        else:
            heapq.heappush(heap, Item(item[0], item[1], item[2], sort_parameter, sort_order))
        if len(heap) > k:
            heapq.heappop(heap)

    # pop off excess items
    for i in range(items_per_page * (page_number)):
        heapq.heappop(heap)

    # grab the target items in order
    # this is key, the example test case is misleading
    # remember that the page # provided is not necessary the last one
    # therefore there could still be products left over in the heap
    for i in range(k - (items_per_page * page_number)):
        if not heap:
            break
        curr = heapq.heappop(heap)
        ret.append([curr.name, abs(curr.relevancy), abs(curr.price)])

    return ret


print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 0, 2, 1))
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 1, 2, 1))
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 0, 2, 1))
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 1, 2, 1))
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 0, 2, 1))
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 1, 2, 1))

"""
Quickselect option:
Python Quickselect solution. My heap based NlogK solution has the best worstcase runtime of NLogK and Space of O(K), but quickselect is faster on average.
Time Complexity: O(N + KlogK)
Space Complexity: O(N)

import random
def quickselect(items, k, sort_order, sort_parameter):
    if not items:
        return []

    if len(items) == k:
        return items

    params = [item[sort_parameter] for item in items]
    pivot = random.choice(params)

    left, right, equal = [], [], []

    for item in items:
        if item[sort_parameter] < pivot:
            left.append(item)
        elif item[sort_parameter] > pivot:
            right.append(item)
        else:
            equal.append(item)

    if sort_order == 0:
        if len(left) == k:
            return [item for item in left]
        if len(left) + len(equal) == k:
            return [item for item in left] + [item for item in equal]
        if k < len(left):
            return quickselect(left, k, sort_order, sort_parameter)
        if len(left) + len(equal) > k:
            return left + equal[:k-len(left)]
        return [item for item in left] + [item for item in equal] + quickselect(right, k-len(left)-len(equal), sort_order, sort_parameter)
    else:
        if len(right) == k:
            return [item for item in right]
        elif len(right) + len(equal) == k:
            return [item for item in right] + [item for item in equal]
        elif k < len(right):
            return quickselect(right, k, sort_parameter, sort_parameter)
        elif len(right) + len(equal) > k:
            return right + equal[:k-len(right)]
        else:
            return [item for item in right] + [item for item in equal] + quickselect(left, k-len(equal)-len(right), sort_order, sort_parameter)


def items_per_page(num_of_items, items, sort_parameter, sort_order, items_per_page, page_number):
    k = (page_number+1)*items_per_page
    # O(n) quickselect average case to grab top k
    top_k = quickselect(items, k, sort_order, sort_parameter)
    # O(KlogK) to sort top k
    top_k.sort(key=lambda x: x[sort_parameter], reverse=sort_order)

    return [item[0] for item in top_k[page_number*items_per_page:]]

#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 0, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 1, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 0, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 1, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 0, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 1, 2, 1))
#print(items_per_page(5, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18], ['item4', 17, 20],['item5', 17, 21]], 1, 0, 2, 1))
#print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 0, 2, 0))
"""