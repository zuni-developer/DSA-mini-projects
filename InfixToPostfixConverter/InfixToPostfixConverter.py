import re

class InfixToPostfix:
    def __init__(self):
        self.stack=[]
        self.output=[]
        self.precedence={
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1
        }

    # Check if character is an operator
    def is_operator(self, ch):
        for i in self.precedence:
            if ch==i:
                return True
        return False

    # Return precedence of an operator
    def precedence_of(self, op):
        for i in self.precedence:
            if op==i:
                return self.precedence[i]
        return 0

    # Main method to convert infix to postfix
    def convert(self, expression):
        expression = re.findall(r'\d+|[a-zA-Z]+|[()+\-*/^]', expression)
        for i in expression:
            if self.is_operator(i):
                while (self.stack and self.precedence_of(self.stack[-1])>=self.precedence_of(i)):
                    self.output.append(self.stack.pop())
                self.stack.append(i)
            elif i=='(':
                self.stack.append(i)
            elif i==')':
                while self.stack and self.stack[-1]!='(':
                    self.output.append(self.stack.pop())
                self.stack.pop()
            else:
                self.output.append(i)
        while self.stack:
            self.output.append(self.stack.pop())

    # Return the final postfix expression as a string
    def get_postfix(self):
        return ''.join(self.output)