alf = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
key = alf.index(input("Введите ключ: ").upper())
t = dict.fromkeys(alf)
d = 0
for i in range(key, len(alf)):
    t[alf[d]] = alf[i]
    d += 1
    n = 30 - key
for i in range(0, key):
    t[alf[n]] = alf[i]
    n += 1


def to_lat(text):
    text1 = [t.get(i, i) for i in text]
    newtext = ''.join(text1)
    print(newtext)
