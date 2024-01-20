alf = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
key = alf.index(input("Введите ключ: ").upper())
t = dict.fromkeys(alf)
d = 0
for i in range(key, len(alf)):
    t[alf[d]] = alf[i]
    d += 1
    n = 29 - key
# Цикл для смещения списка символов по ключу
for i in range(0, key):
    t[alf[n]] = alf[i]
    n += 1


# Функция для перестановки символов
def to_lat(text):
    text1 = [t.get(i, i) for i in text]
    newtext = ''.join(text1)
    spltxt = newtext.replace(' ', '')
    return spltxt


def add_spaces(spltxt, chunk_size=5):
    spltxt = spltxt.replace(',', 'ЗПТ')
    spltxt = spltxt.replace('.', 'ТЧК')
    res = ' '.join([spltxt[i:i + chunk_size] for i in range(0, len(spltxt), chunk_size)])
    return res

spltxt1 = input().strip().upper()
spltxt = to_lat(spltxt1)
result = add_spaces(spltxt)
print(result)

#Полученный ключи путем взлома
tetx = spltxt1.replace(' ','')
tsts = result.replace(' ','')
kord = tetx.index('А')
if spltxt1.count(tetx[kord]) == result.count(tsts[kord]):
    print(f'Взломанный ключ:{tsts[kord]}')

while True:
    sym = input().upper().strip()
    print(f'В открытом тексте:{spltxt1.count(sym)}', f'В закрытом тексте:{result.count(sym)}')
