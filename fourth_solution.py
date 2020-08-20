class stack():
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self,data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def max(self):
        return max(self.item)

obj = stack()
number_of_queries = int(input())
for i in range(number_of_queries):
    query = list(map(str,input().split()))
    if query == ["pop"]:
        obj.pop()
    elif query == ["max"]:
        print(obj.max())
    elif query[0] == "push":
        obj.push(query[1])