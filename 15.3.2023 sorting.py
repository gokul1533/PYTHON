n=int(input("enter the no.of elements,\n"))
arr=[]
print("enter the element")
for i in range(0,n):
    s=int(input())
    arr.append(s)
    print("before sorting")
    print(arr)
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
while j>=0 and key < arr[j]:
    arr[j+1]=arr[j]
    j=1
    arr[j+1]=key
print("after sorting")
print(arr)
    
