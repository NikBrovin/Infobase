def taskmanager(fname):
 if fname == "1":

    s = 0
    k = 15
    d = k - 10
    k = 4 * d
    s = k - 50
    print (s)

 if fname =="2":
     x = 3
     y = 4
     z = x+y
     z = z+1
     x = y
     y = 5
     x = z+y+7
     print(x)

 if fname =="3":
    e = int(input("введите цифру"))
    print(e, e + 1, e + 2,)

 if fname =="4":
    a = int(input("первое число:\n"))
    b = int(input("второе число:\n"))
    c = int(input("третье число:\n"))
    d = (a + b + c)
    print (d)

 if fname == "5":
    length = int(input("Введите длинну ребра\n"))
    print("Обьем куба: ",length**3," Площадь полной поверхности: ",length*length*6)

 if fname == "6":
     a = int(input("первое число:\n"))
     b = int(input("второе число:\n"))
     print(3*(a+b)**3+275*b**2-127*a-41)

 if fname == "7":
     a = int(input("целое:\n"))
     print(a+1, a-1, sep=" следущая за числом\n", end=" предыдущая за числом\n")

 if fname == "8":
    a = int(input("цена мыши:\n"))
    b = int(input("цена моника:\n"))
    c = int(input("цена компа:\n"))
    d = int(input("цена клавы:\n"))
    e = (a+b+c+d)*3
    print (e)

 if fname == "9":
    a = int(input("первое число\n"))
    b = int(input("второе число\n"))
    print(a+b,"\n", a-b,"\n",a*b,"\n",)

 if fname == "10":
    a = int(input("первое число:\n"))
    b = int(input("второе число:\n"))
    c = int(input("третье число:\n"))
    ar = (2*a+(b-1)*c)*b/2
    print(ar)

 if fname == "11":
    a = int(input("первое число\n"))
    print(a*1,"---",a*2,"---",a*3,"---",a*4,"---",a*5)
 if fname == "12":
     a = int(input("число:\n"))
     b = int(input("прогрессия:\n"))
     c = int(input("на прогрессию:\n"))
     print (a*(b**(c-1)))

 if fname == "12":
     a = int(input("число:\n"))
     print (a//100)

 if fname == "13":
     a = int(input("Мандарины\n"))
     b = int(input("Школьники\n"))
     print (a//b)
     print (a%b)
 if fname == "14":
     a = int(input("Количество человеков\n"))
     if a%2 == 1 :
         print(a//2+1)
     if a%2 == 0 :
         print(a//2)
 if fname == "15":
     a = int(input("номер места\n"))
     if a % 4 > 0:
        print(a // 4 + 1)
     if a % 4 == 0:
        print(a // 4)
 if fname == "16":
    a = int(input("время\n"))
    b = 60
    print("час",a//b,"минут",a%b)
 if fname =="17":
     a = int(input("введите число\n"))
     print ()
 if fname == "18":
     A = int(input("введите число\n"))
     a = str((A-A%100)/100)
     b = str((A%100-A%10)/10)
     c = str(A%10)
     print (a,b,c)
     print(a, c, b)
     print(b, a, c)
     print(b, c, a)
     print(c, a, b)
     print (c,b,a)
taskname = input("Какую функцию запустить?\n")
taskmanager(taskname)

