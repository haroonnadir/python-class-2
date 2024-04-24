#This is a comment
print("Hello, World!")
print("Hello, World!")

x = 5
y = "John"
print(x)
print(y)


x = 0
y = bool(x)  # y will be False
print(y)

x = "hello"
y = list(x)    # y will be ['h', 'e', 'l', 'l', 'o']
z = tuple(x)   # z will be ('h', 'e', 'l', 'l', 'o')
w= set(x)     # w will be {'h', 'e', 'l', 'o'}
print(y)
print(z)
print(w)


x = [("a", 1), ("b", 2)]
y = dict(x)  # y will be {'a': 1, 'b': 2}
print(y)


x = 3
y = 4
z = complex(x, y)  # z will be 3+4j
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)




x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello, World!"
print(len(a))







b = "Hello, World!"
print(b[2:])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))









