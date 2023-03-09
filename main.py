n = int(input('Введите N'))
res = ''
for i in range(n):
    s = input()
    res = res + s + ''
print(res)

def zad2():
    a = input()
    res = ''
    while a!= 'stop':
        a = input()
        res = res + a + ''
    print(res)
zad2()

def zad3():
    slovo = input()
    if 'ф' in slovo:
        print('Ого, Это редкое слово')
    else:
        print('Эх...Это не очень редкое слово')
zad3()

def zad4():
    from random import randint
    m = 0
    r = 0
    while m < 3:
        a = randint(1,100)
        b = randint(1,100)
        res = int(input(str(a) + '+' + str(b) + '='))
        if res != a+b:
            print("Ответ не верный")
            m+=1
        else:
            print("Правильно")
            r+=1
    if m==3:
        print("игра окончена правильных ответов", r)
zad4()
