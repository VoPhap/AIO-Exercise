def count_chars(s):
  result = {}
  s = s.replace(" ", "")
  for char in s:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  
  print(result)

string = 'Happiness '
count_chars(string) 

string = 'smiles '
count_chars ( string )