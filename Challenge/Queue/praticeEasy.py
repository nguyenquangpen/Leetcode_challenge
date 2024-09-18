from collections import deque
import queue

class Solution_1700(object):
    def countStudents(self, students, sandwiches):
        qp = deque(students)
        cnt = 0
        turns = 0
        while len(qp) > 0 and turns < len(qp):
            value_x = qp[0]
            if value_x != sandwiches[cnt]:
                qp.append(qp.popleft())
                turns += 1
            else:
                qp.popleft()
                cnt += 1
                turns = 0
        return len(qp)


class Solution_2073(object):
    def timeRequiredToBuy(self, tickets, k):
        cnt, dem = 0, 0
        while tickets[k] != 0:
            if tickets[dem] > 0:
                cnt += 1
            tickets[dem] -= 1
            dem += 1
            if dem >= len(tickets):
                dem = 0
        return cnt


class MyQueue_232:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x):
        self.s1.append(x)
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
    def empty(self):
        return not self.s1 and not self.s2

class Solution_387(object):
    def firstUniqChar(self, s):
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        for i in range(len(s)):
            if tmp[s[i]] == 1:
                return i
        return -1


class MyStack_225(object):
    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
    def push(self, x):
        self.que1.append(x)
    def pop(self):
        while len(self.que1) > 0:
            self.que2.append(self.que1.popleft())
        self.que1, self.que2 = self.que2, self.que1
        return self.que1.pop()
    def top(self):
        while len(self.que1) > 1:
            self.que2.append(self.que1.popleft())
        top_element = self.que1.popleft()
        self.que2.append(top_element)
        self.que1, self.que2 = self.que2, self.que1

        return top_element
    def empty(self):
        return not self.que1

if __name__ == '__main__':
    s = MyQueue_232()
