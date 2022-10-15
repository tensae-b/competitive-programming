class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        check= False
        
        for x in range(len(s)):
            p= s[x]
            if len(s)%2 ==0:
                if p== '(' or p== '[' or p== '{':
                    stack.append(p)

                else:

                    if stack:
                        y= stack.pop()
                        if p== ')':
                            if y == '(':
                                check = True
                            else:
                                check = False
                                return(check)

                        elif p== ']':
                            if y == '[':
                                check = True
                            else:
                                check = False
                                return(check)
                        elif p== '}':
                            if y == '{':
                                check = True
                            else:
                                check = False
                                return(check)
                    else:
                        check= False
                        return(check)
            else:
                 return(check)
        if not stack:  
            return(check)
        else:
            return False
            
        
        
        
