class balance_check:
    def __init__(self,s):
        self.s = s

    def check(self):
        start = set('{[(')
        closing = set('}])')
        matches = set([('(',')'),('{','}'),('[',']')])
        stack = []
        for i in self.s:
            if i in start:
                stack.append(i)
            elif i in closing:
                last = stack.pop()
                if (last,i) in matches:
                    pass
                elif (last,i) not in matches:
                    return self.s.index(i)
        return "Success"

str_check = balance_check("foo(ba]r);")
print(str_check.check())