# Нечетные восьмиричные числа, не превышающие 409610, у которых вторая справа цифра равна 7.
# Выводит на экран цифры числа, исключая семерки.
# Вычисляется среднее число между минимальным и максимальным и выводится прописью.
import re
numbers = []


# перевод цифр пропись
def w(n):
    numeros = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return numeros.get(n)


with open('test.txt', 'r') as f:
    buff = f.read()
    if not buff:
        print('Файл пуст')
        quit()
    u = re.findall(r'[1234567]*7[1234567]{2}', buff)
    for i in u:
        if int(i, 8) < 4096 and int(i) % 2 != 0:
            numbers.append(int(i))
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        answers = []
        for i in numbers:
            answer = ''
            for j in str(i):
                if j != '7':
                    answer += j
            answers.append(answer)
        print('Цифры чисел без 7:', *answers)
        answer = ''
        for i in str((max(numbers) + min(numbers)) // 2):
            answer += w(int(i)) + ' '
        print('Среднее:', (max(numbers) + min(numbers)) // 2, answer)