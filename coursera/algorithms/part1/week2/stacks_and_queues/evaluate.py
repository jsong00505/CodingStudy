class Evaluate:
    def evaluate(self, s):
        ops = []
        vals = []

        for c in s:
            if c == '(' or c == ' ':
                continue
            elif c == '+' or c == '*':
                ops.append(c)
            elif c == ')':
                op = ops.pop()
                a = int(vals.pop())
                b = int(vals.pop())
                if op == '+':
                    vals.append(a+b)
                else:
                    vals.append(a*b)
            else:
                vals.append(c)
        return vals.pop()
