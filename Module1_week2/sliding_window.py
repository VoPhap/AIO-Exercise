num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
start = list(range(0, len(num_list)-k+1))
end = list(range(k, len(num_list)+1))

result = []
for s,e in zip(start, end):
  window = num_list[s:e]
  result.append(max(window))

print(result)
