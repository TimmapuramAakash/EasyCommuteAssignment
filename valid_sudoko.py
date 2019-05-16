class Solution:
    def check(self,b,c,d):                #b is column representation , c is row and d is each window cell/matrix of 3*3
        for i in b:
            if(len(set(i))!=len(i)):
                return 0
        for i in c:
            if(len(set(i))!=len(i)):
                return 0
        for i in d:
            if(len(set(i))!=len(i)):
                return 0
        return 1
        
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
      
        b=[[row[i] for row in A if row[i]!="."] for i in range(9)]          #Can also check b first here itself rather than separate function if false return 0 else check c followed by d.
        c=[[row[i]  for i in range(9) if row[i]!="."] for row in A ]
        i,j=0,0
        d=[]
        while(i!=9):
            l,m,n=[],[],[]
            for s in range(i,i+3):
                for t in range(j,j+3):
                    if(A[s][t]!="."):
                        l.append(A[s][t])
                for t in range(j+3,j+6):
                    if(A[s][t]!="."):
                        m.append(A[s][t])
                for t in range(j+6,j+9):
                    if(A[s][t]!="."):
                        n.append(A[s][t])
            d.append(l)
            d.append(m)
            d.append(n)
            i=i+3
        return self.check(b,c,d)
