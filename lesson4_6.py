from itertools import cycle, count
import sys
def numbersgen (start):
    for el in count(3):
        if el > 13:
            break
        yield el

for el in numbersgen(13):
    print(el)


text = "АБВГДЭЙКА"
circles = 0
for el in cycle(text):
    if el == text[0]:
        circles +=1
    if circles > 3:
        break
    else:
        print(el)




