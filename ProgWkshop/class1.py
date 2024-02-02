#25/1/24
n = int(input("Input n:"))
resources = [0]*n
for i in range(n):
    resources[i] = int(input(f"Input the {i}th resource:"))
extraResources = int(input("Input the extraResource:"))
result = [False]*n
for i in range(len(resources)):
    temp = resources
    temp[i]+=extraResources
    if temp[i]==max(temp):
        result[i] = True
print(result)


