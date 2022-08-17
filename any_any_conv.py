 def checkalpha(digit):
    if digit<10:
        return digit
    elif digit==10:
        return "A"
    elif digit==11:
        return "B"
    elif digit==12:
        return "C"
    elif digit==13:
        return "D"
    elif digit==14:
        return "E"
    elif digit==15:
        return "F"
def convert(num,a,b):
     con_table={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
     prev=0
     res=""
     j=-1
     if(a==8 and b!=10):
        r=convert(num, a, 10)
        s=convert(r,10,b)
        return s 
     elif(b==16):
         while num>0:
             rem=num%b
             num=num//b
             res=str(checkalpha(rem))+res
         return res
     elif(a==16):
         if b==10:
             j=len(num)-1
             for i in num:
                 prev+=con_table[i]*(16**j)
                 j-=1
             return prev
         elif(b==8 or b==2):
            ans=convert(num,a,10)
            b=convert(ans,10,b)
            return b
     elif(a==10):
        while num>0:
            rem=num%b
            j=j+1
            prev=rem*(10**j)+prev
            num=num//b
        return prev    
     elif(b==10):
        while num>0:
            rem=num%10
            j=j+1
            prev=rem*(a**j)+prev
            num=num//10
        return prev
    
h=int(input("if your conversion is from hexa decimal to any other decimal enter 1 otherwise enter 0:"))
if(h==0):
    
    num=int(input("enter number:"))
    a=int(input("enter base of entered number:"))
    b=int(input("enter base of convertion number:"))
else:
    num=str(input("enter number:"))
    a=int(input("enter base of entered number:"))
    b=int(input("enter base of convertion number:"))
    
res=convert(num,a,b)
print(res)