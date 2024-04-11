import sys
sys.path.append("C:\Code")

import functions as f
f.sum_list([10, 20, 30])

book = {}
print(book)
book['tom'] = {
    'name': 'tom',
    'address': '1 Stanley Street',
    'phone': 90834508
}
book['marley'] = {
    'name': 'marley',
    'address': '2 Stanley Street',
    'phone': 2989345
}
print(book)

import json
s = json.dumps(book)
print(s)

with open("C:/Code/book.txt","w") as f:
    f.write(s)