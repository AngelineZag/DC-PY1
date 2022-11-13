# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

myList = [
    {num: bin(num) for num in range(16)},
    {num: oct(num) for num in range(16)},
    {num: hex(num) for num in range(16)}
]

pprint(myList)


