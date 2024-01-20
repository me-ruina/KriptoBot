alf = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
key = alf.index(input("Введите ключ: ").upper())
t = dict.fromkeys(alf)
d = 0
for i in range(key, len(alf)):
    t[alf[d]] = alf[i]
    d += 1
    n = 29 - key
#Цикл для смещения списка символов по ключу
for i in range(0, key):
    t[alf[n]] = alf[i]
    n += 1
#Функция для перестановки символов
def to_lat(text):
   text1 = [t.get(i, i) for i in text]
   newtext = ''.join(text1)
   newtext = newtext.replace(' ','')
   spltxt = newtext
   return spltxt

def add_spaces(spltext, chunk_size=5):
    return ' '.join([spltxt[i:i+chunk_size] for i in range(0, len(spltxt), chunk_size)])

spltxt = to_lat(input().strip().upper())
result = add_spaces(spltxt)
print(result)