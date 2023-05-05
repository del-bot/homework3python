#задача 16
#n = int(input('input number of element'))
#A = input('input element of massiv through a space').split()
#x = (input('input find number'))
#print(A.count(x))

#Задача18
# a=[int(i) for i in input().split()]
# b=int(input())
# number=0
# for i in range(len(a)):
#     if (b-a[i])<b-number and b-a[i]>0:
#         number=i
#     elif b == a[i]:
#        a[number] = b
# print(a[number])

#задача 20
import re
def kind(taxt):
    return bool(re.search('[a-z]', text))
dic_eng = {
        1: 'A, E, I, O, U, L, N, S, T, R',
        2: 'D, G',
        3: 'B, C, M, P',
        4: 'F, H, V, W, Y',
        5: 'K',
        8: 'J, X',
        10: 'Q,Z'
    }
dic_rus = {
        1: 'А, В, Е, И, Н, О, Р, С, Т',
        2: 'Д, К, Л, М, П, У',
        3: 'Б, Г, Ё, Ь, Я',
        4: 'Й, Ы',
        5: 'Ж, З, Х, Ц, Ч',
        8: 'Ш, Э, Ю',
        10: 'Ф, Щ, Ъ'
    }
text = input().upper()
if kind(text):
    print(sum([k for i in text for k, v in dic_eng.items() if i in v]))
else:
    print(sum([k for i in text for k, v in dic_rus.items() if i in v]))

