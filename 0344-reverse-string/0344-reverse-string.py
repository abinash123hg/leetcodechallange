class Solution:
    def reverseString(self, s: list[str]) -> None:
        i ,j=0,len(s)-1
        rev=[]
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        """
        Do not return anything, modify s in-place instead.
        """
       
        
           
