# Chapter : 3 - item : 3 - Postfix Calculator

# จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix

# โดยให้แสดงผลลัพธ์ตามตัวอย่าง

#  ***Postfix expression calcuation***
# Enter Postfix expression : 6 5 2 3 + 8 * - 3 + *
# Answer :  -192.00

#  ***Postfix expression calcuation***
# Enter Postfix expression : 4 22 * 89 / 98 * 21 - 32 2 / 4 * 10 / 23 * + 23 -48 * -
# Answer :  1327.10

#  ***Postfix expression calcuation***
# Enter Postfix expression : 5 8 * 5 6 * 6 6 4 * - 5 6 * 6 / + - -
# Answer :  -3.00

#  ***Postfix expression calcuation***
# Enter Postfix expression : 3 8 2 / 6 * 5 6 - + 6 6 -5 5 * 2 - - + + +
# Answer :  65.00

class Stack():
    def __init__(self, ls = None):
        if ls is None:
            self.__stack = []
        else:
            self.__stack = ls

    def push(self,i):
        self.__stack.append(i)

    def pop(self):
        return self.__stack.pop()

    def isEmpty(self):
        return bool(self.__stack)

    def size(self):
        return len(self.__stack)

def postFixeval(tokens):
    stack = Stack()
    EXPRESSIONS_TOKEN = '+-*/'
    for token in tokens:
        if token in EXPRESSIONS_TOKEN:
            n1 = stack.pop()
            n2 = stack.pop()
            if token == '+':
                token = n2 + n1
            elif token == '-':
                token = n2 - n1
            elif token == '*':
                token = n2 * n1
            elif token == '/':
                token = n2 / n1
        stack.push(float(token))
    return stack.pop()



print(" ***Postfix expression calcuation***")
input_tokens = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(input_tokens)))