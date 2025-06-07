class PostfixEvaluator:
    def __init__(self):
        self.stack=[] 
        self.operators={'+','-',"*",'/','^'}
        self.output=[]

    def evaluate(self, expression):
        postfix=expression.split()
        for i in postfix:
            if i in self.operators:
                b=self.stack.pop()
                a=self.stack.pop()
                result = self.apply_operator(a, b, i)
                self.stack.append(result)
            else:
                self.stack.append(float(i)) 
        return self.stack.pop()  
                
    def apply_operator(self, a, b, operator):
        if operator=='+':
            return a+b
        elif operator=='-':
            return a-b
        elif operator=='*':
            return a*b
        elif operator=='/':
            return a/b 
        elif operator=='^':
            return a**b