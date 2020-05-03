import os
# part add a new line
text = os.popen('dir /b').read()
print (text)

def test(a, b):
    print(a+b)

if __name__ == '__main__':
    test("a", "b")
