from collections import deque

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


if __name__ == '__main__':
    pass
