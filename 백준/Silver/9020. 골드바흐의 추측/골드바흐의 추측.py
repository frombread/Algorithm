import sys

def test(x):
  if x==1:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True


for _ in range(int(sys.stdin.readline())):
    num = int(int(sys.stdin.readline()))

    a, b = num//2, num//2
    for _ in range((num//2)+1):
       if test(a) and test(b):
          print(a,b)
          break
       else:
          a -= 1
          b += 1
