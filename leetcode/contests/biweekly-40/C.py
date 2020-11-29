"""
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].


"""
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.q = deque([])

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        i = len(self.q) // 2
        # if len(self.q) % 2 == 0:
        #     i -= 1
        temp = list(self.q)[0:i] + [val] + list(self.q)[i:]
        # print(self.q, val, temp)
        self.q = deque(temp)
        # print(self.q)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if self.q:
            return self.q.popleft()
        else:
            return -1

    def popMiddle(self) -> int:
        if len(self.q) > 0:
            i = (len(self.q) // 2)
            if len(self.q) % 2 == 0:
                i -= 1
            p = list(self.q)[i]
            temp = list(self.q)[0:i] + list(self.q)[i+1:]
            # print(self.q, temp, p, i)
            self.q = deque(temp)
            return p
        else:
            return -1

    def popBack(self) -> int:
        if self.q:
            return self.q.pop()
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
