n = int(input())
arr = map(int, input().split())

arr = list(arr)

Max = max(arr)
print("la valeur max = ",Max)
print("la liste : ",arr)

while Max in arr:
    arr.remove(Max)

print("la liste apres le retrait de max : ",arr)

print("la valeur max : ",max(arr))

#code en local
n = int(input())
arr = map(int, input().split())

arr = list(arr)

Max = max(arr)
print("la valeur max = ",Max)
print("la liste : ",arr)

while Max in arr:
    arr.remove(Max)

print("la liste apres le retrait de max : ",arr)

print("la valeur max : ",max(arr))
