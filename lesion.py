a = input("Введите алгебраическое выражение: ")
alg_vyr1 = list(a)
result = []
num = ""
for char in alg_vyr1:
  if "0" <= char <= "99":
    num = num + char
    if num != "":
      result.append(int(num))
      result.append('*')
      num = ''
  elif char.isalpha() or "+":
    result.append(char)

if result[-1] == ")":
  result.pop(-2)

str1 = ""
for el in result:
  str1 += str(el)
print(str1)