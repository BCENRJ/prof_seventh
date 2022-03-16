class Stack:
    def __init__(self, stack: str):
        self.stack_list = [i for i in stack]

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def push(self, value) -> None:
        self.stack_list.insert(0, value)

    def pop(self):
        if not self.is_empty():
            item = self.stack_list[0]
            self.stack_list.remove(item)
            return item
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack_list[0]
        return None

    def size(self):
        return len(self.stack_list)

    def check(self):
        if self.size() % 2 != 0:
            return 'Несбалансированно'
        cursor = ''
        index = 0
        for i in range(len(self.stack_list)):
            if self.stack_list[i] in {'(', '{', '['}:
                cursor = self.stack_list[i]
                index = i
                continue
            elif self.stack_list[i] in {')', '}', ']'}:
                if (cursor == '(' and self.stack_list[i] == ')') or (cursor == '{' and self.stack_list[i] == '}') or \
                        (cursor == '[' and self.stack_list[i] == ']'):
                    del self.stack_list[i]
                    del self.stack_list[index]
                    if not self.is_empty():
                        return self.check()
                    else:
                        return 'Сбалансированно'
                else:
                    return 'Несбалансированно'


if __name__ == '__main__':
    t = Stack('(((([{}]))))')
    t1 = Stack('[([])((([[[]]])))]{()}')
    t2 = Stack('{{[()]}}')
    t3 = Stack('}{}')
    t4 = Stack('{{[(])]}}')
    t5 = Stack('[[{())}]')
    assert t.check() == 'Сбалансированно'
    assert t1.check() == 'Сбалансированно'
    assert t2.check() == 'Сбалансированно'
    assert t3.check() == 'Несбалансированно'
    assert t4.check() == 'Несбалансированно'
    assert t5.check() == 'Несбалансированно'
