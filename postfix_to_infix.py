def postfix_to_infix(expression):

    class Element:
        def __init__(self,expression,operation=None):
            self.exp = expression
            self.opr = operation
   
    expression = expression.strip()
    expression = expression.replace(' ','')
    priority = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    
    for x in list(expression):
        if x.isalpha() or x.isdigit():
            stack.append(Element(x))
            
        elif x in '+-*/^':
            try:
                right = stack.pop()
                left  = stack.pop()
            except:
                return "invalid"
            
            if left.opr is not None and priority[left.opr] < priority[x]:
                left.exp = '(' + left.exp + ')'
            if right.opr is not None and priority[right.opr] < priority[x]:
                right.exp = '(' + right.exp + ')' 
  
            exp_new = left.exp + x + right.exp
            stack.append(Element(exp_new,x))
        else:
            return "invalid"
        
    if len(stack) == 1:
        return stack.pop().exp
    else:
        return "invalid"
        
print(postfix_to_infix('abc-+de-fg-h+/*'))
