import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print('data type of x', x)
print('data type of x', type(x))
# parse x:
y = json.loads(x)
print('data type of y', y)
print('data type of y', type(y))


# the result is a Python dictionary:
print(y["age"])