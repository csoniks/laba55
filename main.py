from random import randint
def z11():
    spisok = ["6", "2", "1", "3", "7"]
    a = input("введите число")
    if a in spisok:
        print("Подравляю, вы угадали!")
        print("исходный список:", *spisok)
        print("Ваше число", a)
    else:
        print("Нет такого числа в этом списке")
        print("исходный список:", *spisok)
        print("Ваше число", a)


def z1():
    spisok = [randint(1, 1000) for i in range(5)]
    a = input("Введите число")
    if a in spisok:
        print("Подравляю, вы угадали!")
        print("исходный список:",*spisok)
        print("Ваше число", a)
    else:
        print("Нет такого числа в этом списке")
        print("исходный список:",*spisok)
        print("Ваше число", a)

def z2():

    slovarik = {}
    spisok = [randint(1, 10) for i in range(10)]
    for i in spisok:
        if i in slovarik:
            slovarik[i] += 1
        else:
            slovarik[i] = 1
    for i in slovarik:
        if slovarik[i] > 1:
            print("цифра", i, ";", "кол-во повторений:", slovarik[i])
    print(slovarik)
    print(spisok)



def z3():
    k = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    vyhodnoy = int(input("сколько выходных вы хотите?"))
    for i in k:
        print("ваши выходные:", *k[-vyhodnoy:])
        print("ваши рабочие дни:", *k[:-vyhodnoy])
        break


def z4():
    s1 = ["Smirnov", "Ivanov", "Kozlov", "Petrov"]
    s2 = ["Lebedeva", "Jdanova", "Novikova", "Sidorova"]
    k = tuple(s1[:2] + s2[:2])
    spisok = list(k)
    spisok.sort()
    sortk = tuple(spisok)
    print("весь список", *s1, *s2)
    print("спорт тим", k)
    print("длина:", len(k))
    print("отсортированный кортеж:", sortk)
    cnt = 0
    if "Ivanov" in k:
        print("Иванов в команде")
    else:
        print("такого нет")
    for i in k:
        if i == "Ivanov":
            cnt += 1
    print("фамилия встретилась", cnt, "раз")


z11()
z1()
z2()
z3()
z4()