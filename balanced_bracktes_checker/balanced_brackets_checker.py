class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if  not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items)==0
    
def is_balanced(expression):
    stack=Stack()
    bracket_pair={')':'(',']':'[','}':'{'}

    for i in expression:
        if i in "([{" :
            stack.push(i)
        
        elif i in ")]}":
            top=stack.pop()
            if top != bracket_pair[i]:
                return False
        
        else:
            continue
    return stack.is_empty()

def main():
    expression=input("enter expression :")
    if is_balanced(expression):
        print("Balanced")
    else:
        print("Not Balanced")

main()