#1/02/2024
n = int(input("Enter number of students: "))
m = int(input("Enter number of connections: "))
print("Enter the connections as two letters")
di = {}         #graph implementation using dictionary
for i in range(m):
    s = input()
    c = s.split()
    if c[0] not in di:
        di[c[0]] = [c[1]]
    else:
        di[c[0]].append(c[1])

    if c[1] not in di:
        di[c[1]] = [c[0]]
    else:
        di[c[1]].append(c[0])

group = []
num = 0
for i in di:
    if i not in group:
        num+=1
        for j in di[i]:
            for k in di[j]:
                if k not in di[i] and k not in group:
                    group.append(k)

def cycle_of_3(graph):
   def has_cycle(node, parent):
       visited.add(node)
       for neighbor in graph[node]:
           if neighbor == parent:
               continue
           if neighbor in visited or has_cycle(neighbor, node):
               return True
       return False

   visited = set()
   for node in graph:
       if node in visited:
           continue 
       if has_cycle(node, None):
           return True
   return False

if cycle_of_3(di):
    print(-1)
else:
    print(num)













    
    

