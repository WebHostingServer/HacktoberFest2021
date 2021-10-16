def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print("List after selection sorting",a)
  
n=input("Enter comma separated values eg. 1,2,3 :")
a=list(eval(n))
print("List before sorting:",a)
selectionsort(a)
