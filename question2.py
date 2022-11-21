def question2(a,b,p,q):
    if((p==0 and q==0) or q==0):
        return 1
    if(p==0):
        return 0
    if(a[p-1]==b[q-1]):
        return(question2(a,b,p-1,q-2)+ question2(a,b,p-1,q))
    else:
        return question2(a,b,p-1,q)
a=str(input())
b=str(input())
print(question2(a,b,len(a),len(b)))
