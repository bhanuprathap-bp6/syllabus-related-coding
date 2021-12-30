wn=int(input("Enter the no.of elements in S: "))
W=[input().split() for i in range(wn)]

def inner_prod(w,v):
    x=0
    for i in range(0,len(w)):
        x += w[i]*v[i]
    return x

def norm(v):
    norm=0
    for i in range(0,len(v)):
        norm += v[i]**2
    return norm**0.5

def set_add(a,b):
    x=[0 for ax in range(len(a))]
    for i in range(len(a)):
        x[i]=round(a[i],2)+round(b[i],2)
    return x

def set_subt(a,b):
    x=[0 for ax in range(len(a))]
    for i in range(len(a)):
        x[i]=a[i]-b[i]
    return x

def set_mult(c,x):
    y=[]
    for i in x:
        y.append(c*i)
    return y


n=len(W)
V=[0 for i in range(n)]


V[0]=W[0]
for k in range(1,n):
    
    x=[0 for ax in range(len(W[0]))]
    for j in range(0,k):
        z= inner_prod(W[k],V[j])/ (norm(V[j])**2)
        x_temp = set_mult(z,V[j])
        x = set_add(x,x_temp) 
        
        if k==2 and j==0:
            print(W[k],V[j])
    
    V[k]=set_subt(W[k],x)

print(V)