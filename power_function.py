class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer


    def power(self,x, y): 

        if (y == 0): 
            if(x!=0):
                return 1
            return 0
        elif (int(y % 2) == 0): 
            return (self.power(x, int(y / 2)) *self.power(x, int(y / 2))) 
        else: 
            return (x * self.power(x, int(y / 2)) *self.power(x, int(y / 2))) 



    def pow(self, x, n, d):
        a=self.power(x,n)
        return a%d
