import threading
from tkinter import *
def cryptho_chifr(text, key):
    alf = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
    key = alf.index(f'{key}')
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

    spltxt = to_lat(text.strip().upper())
    result = add_spaces(spltxt)
    return result

# Полученный ключи путем взлома
emp = []
def vzlom(text):
    global emp
    alf = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
    for key in alf:
        key = alf.index(f'{key}')
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

        spltxt = to_lat(text.strip().upper())
        res = add_spaces(spltxt)
        emp.append(res)

def window(emp):
    import tkinter as tk
    # Создаем окно
    root = tk.Tk()
    root.title("Варианты открытого текста")
    # Выводим элементы списка в столбик
    for item in emp:
        label = tk.Label(root, text=item)
        label.pack()
    # Запускаем главный цикл обработки событий
    root.mainloop()

spltxt1 = input("Enter your text: ").strip().upper()
key = input("Введите ключ: ").upper()
result = cryptho_chifr(spltxt1, key)
print(result)

chifr = input("Введите текст для взлома: ").strip().upper()
analize = vzlom(chifr)
window = window(emp)

