import os
# part add a new line
# aaaa
test = os.popen('dir /b').read()
print (test)

def test(a, b):
  print(a+b)

if __name__ == '__main__':
  test(1, 3)
