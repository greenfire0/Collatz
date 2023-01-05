#from prin import print_tree



class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def findval(self, lkpval):
        if lkpval == self.data:
            return True
        else:
            if self.left is not None: 
                  if self.left.findval(lkpval):
                      return True
            if self.right is not None:
                  if self.right.findval(lkpval):
                      return True
        return False
    def getval(self, lkpval):
        if lkpval == self.data:

            return self
            
        else:
            if self.left is not None: 
                a = self.left.getval(lkpval)
                if  a != False:
                        return a
            if self.right is not None:
                b = self.right.getval(lkpval)
                if b != False:
                    return b
        return False 

    def insert(self, data):
        count =0
        for a in data:
            if self.findval(a):
                if count == 0:
                    break
                nums_added = []
                y = self.getval(a).add(data[count-1])
                nums_added.append((data[count-1]))
            
                for num in range(count-2,-1,-1):  
                
                    y= y.add(data[num])
                    nums_added.append((data[num]))
                #print("The numbers added are"+str(nums_added) + " at location " +str(a))
                break
            count +=1

        
    def add(self, data):
       
        if data%2==0:
            if self.left is None:
                self.left = Node(data)
                return self.left
            else:
                return self.left.add(data)
        else:
            if self.right is None:
                self.right = Node(data)
                return self.right
            else:
                return self.right.add(data)


    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
            
    def traverse(self): 
     thislevel = [self]
     a = []
     while thislevel:
        q = []
        for u in thislevel:
            q.append(u.data)
   
        nextlevel = list()
        for n in thislevel:
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)
        thislevel = nextlevel

        a.append(q)
     return(a)