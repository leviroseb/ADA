import random

def bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux


f=open("please.txt","w")

def gen_arreglos2(n,tam):
    for i in range(n):
        A=[]
        for j in range(tam):
            A.append(random.randint(-tam,tam))
        #print(A)
        f.write(str(A))
        print()



gen_arreglos2(5,2)
f.close()




