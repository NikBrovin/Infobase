def taskmanager(fname):

# калькулятор
  '''есть калькулятор которому подается 2 числа после чего совершается 1 из 4 мат.операций
  при лююом другом действии выдает ошибку как и при делении на 0'''
 if fname == "cal":
     a = int(input("введите число\n"))
     b = int(input("введите число\n"))
     c = input("введите операцию\n")
     if b == 0 and c == "/":
         print("на ноль делить нельзя")
     elif c == "+":
      print(a+b)
     elif c == "-":
      print(a - b)
     elif c == "*":
      print(a * b)
     elif c == "/":
         print(a / b)
     else :
      print("некоректноя операция ")

# гонка спидстеров
'''есть 2 супергероя и один из них хочет проверить победит ли он в гонке надо
сравнить их скорости и узнать выйграет он или нет'''
 if fname == "speed":
     a = int(input("n\n"))
     b = int(input("k\n"))
     if a > b:
         print("no")
     if a < b:
         print("yes")
     if a == b:
         print("dont know")

# вид треугольника
'''по вводиммым данным надо узнать каким является треугольник'''
 if fname == "treu":
   a = int(input("1 сторона\n"))
   b = int(input("2 сторона\n"))
   c = int(input("3 сторона\n"))
   if a == b == c:
       print("Равносторонний")
   elif a == b or b == c or a == c:
       print("Равнобедренный")
   else:
       print("Разносторонний")

# Среднее число
'''написать код для нахождения среднего числа из 3 вводимых'''
 if fname == "sred":
   a = int(input("1 число\n"))
   b = int(input("2 число\n"))
   c = int(input("3 число\n"))
   if a < b < c or c < b < a:
     print (b)
   elif b < a < c or c < a < b:
     print (a)
   else:
     print (c)

# Количество дней
'''написать код для определения количества дней в том или ином месяце'''
 if fname == "mou":
   a = int(input("введите месяц(числом)\n"))
   if a == 2:
       print(28)
   elif a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
       print (31)
   else:
       print (30)

# Церемония взвешивания
'''написать код для определения в каку весовую категорию попадет участник соревнований '''
 if fname == "wei":
   a = int(input("введите вес\n"))
   if a < 60:
       print("легкий вес")
   elif a < 64:
       print ("первый полусредний вес")
   else:
       print ("полусредний вес")

# цветовой микшер
'''написать код для определения получаемого цвета при смешивании 2 из 3 '''
 if fname == "color":
    a = input("1 цвет\n")
    b = input("2 цвет\n")
    if a == "Желтый" and b == "Красный":
         print ("оранжевый")
    if a == "Красный" and b == "Желтый":
         print ("оранжевый")
    if a == "Синий" and b == "Желтый":
         print("зеленый")
    if a == "Желтый" and b == "Синий":
         print ("зеленый")
    if a == "Красный" and b == "Синий":
         print ("фиолетовый")
    if a == "Синий" and b == "Красный":
         print ("фиолетовый")
    else:
      ("Ошибка цвета")

# цвета колеса рулетки
'''написать код который при введении номера в диапозоне от 0 до 36
выведит нам цвет кармана ну или ошибку при несоответствии с условием задачи'''
 if fname == "rul":
     a = int(input("номер кармана\n"))
     if a == 0:
         print("зеленый")
     elif 1 <= a <= 36:
         if 1 <= a <= 10 or 19 <= a <= 28:
             if a % 2 == 0:
                 print("черный")
             else:
                 print("красный")
         else:
             if a % 2 == 1:
                 print("черный")
             else:
                 print("красный")
     else:
         print("ошибка ввода")

# пересечение отрезков
 if fname == "ot":
    a1,b1,a2,b2 = int(input()),int(input()),int(input()),int(input())
    if a2 < a1 :
     if b2 < a1:
        print("пустое множество")
     elif b2 == a1:
         print(b2)
     elif a1 < b2 <= b1:
         print(a1,b2)
     elif b2 > b1:
         print(a1,b1)
     elif a2 == a1:
      if b2 <= b1:
         print(a2,b2)
      else:
          print(a2,b1)
     elif a2 < b1:
      if b2 <= b1:
          print(a2,b2)
      else:
          print(a2,b1)
     elif a2 == b1:
          print(a2)
     else:
          print("пустое множество")
# контрольная
#1 "print()"
#2. print('Поэма "Мертвые души" одна из самых интересных')
    print("I'm a math teacher and a programmer!")
    print("3.1415")
#3  print("раз","два","три")
    print('Python','is the best','!!')
#4  print("The World's a little blury", "Or maybe it's my eyes", end='!!!', sep=' :)')
    print("Honey, what's your hurry", end='?')
    print("Told you not to worry", "But maybe that's a lie", sep=')')
#5  "input()"
#6 "n = int(input())" считывает число в переменную n
#7 Имя переменной может начинаться с символа подчеркивания(_)
    Имя переменной не может начинаться с цифры
    Имя переменной не может совпадать с ключевым(зарезервированным) словом
#8  60
#9  56
#10 Данный код создат прямоугольник из звездочек 17 на 4
for i in range (4):
    print('*'*17)

#11 Данный код выведет квадрат суммы и сумму квадратов двух чисел
a = int(input())
b = int(input())
print("Квадрат суммы",a,"и",b,"равен",(a+b)**2)
print("Сумма квадратов",a,"и",b,"равна",a**2+b**2)

#12 Данный код выведет значение выражения a^b+c^d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b)+(c**d))

#13. Данный код выведет число в виду n+nn+nnn
a = int(input())
if 1<=a<=9:
    print(a,a+1,a+2, sep='')
else:
    print('Число вне диапозона')

# площадь треугольника
'''написать код и формулу которая выведет нам площадь треугольника'''
if fname == "1":
  a = int(input())
  b = int(input())
  print(1/2*a*b)

#  две старушки
'''написать код котоый определяет скорость старушек и за какую единицу времени они встретятся'''
if fname == "2":
  v1  = int(input())
  v2  = int(input())
  s  = int(input())
  v = v1+v2
  v = s/v
  print(v)

# обратное число
'''написать код который выводит обратное число вводимому числу'''
if fname == "3":
  a = float(input())
  print(1/a)
  
  # 451 градус по фаренгейту
  '''написать код который переводит цельсий в фаренгейт'''
  if fname == "4":
  a = int(input())
  print((5/9)*(a-32))

# год собаки
'''написать код который переводит возраст собаки в человеческий возраст'''
if fname == "5":
  a = int(input())
  b = 0
  if a > 2:
      b=b+(10.5*2)
      a = a - 2
      b=b + (a*4)
  else:
      b = a*10.5
  print(b)

# первая цифра после точки
'''написать код который выводит первое число после точки'''
if fname == "6":
  a = float(input())
  a = a%1
  a = (a*10)//1
  print(a)

# дробная часть
'''написать код который выводит все числа после точки'''
if fname == "7":
  a = float(input())
  a = a%1
  print(a)

# наибольшее и наименьшее
'''написать код который выводит наибольшее и наименьшее число из 5'''
if fname == "8":
  list1 = list()
  min = 999999999
  max = 0
  for i in range(5):
      a = int(input())
      list1.append(a)
  for i in list1:
      if min>i:
          min = i
      if max<i:
          max = i
  print('max = ', max)
  print('min = ', min)

# сортировка трех
'''написать код который сортирует от наибольшего числа к наименьшему'''
if fname == "9":
  a = int(input())
  b = int(input())
  c = int(input())
  if a > b >c:
      print(a)
      print(b)
      print(c)
  elif a > c >b:
      print(a)
      print(c)
      print(b)
  elif b>a>c:
      print(b)
      print(a)
      print(c)
  elif b>c>a:
      print(b)
      print(c)
      print(a)
  elif c>a>b:
      print(c)
      print(a)
      print(b)
  elif c>b>a:
      print(c)
      print(b)
      print(a)

# интересное число
'''написать код который должен выводить является ли число интересным или нет
в зависимости от того является ли среднее число разность между 1 и 3 '''
if fname == "10":
  list1=list(input())
  list2= list()
  for i in list1:
      i = int(i)
      list2.append(i)
  if list2[0]-list2[2] == list2[1] or list2[2]-list2[0] == list2[1]:
      print('число интересное')
  else:
      print('скучное')

# абсолютная сумма
'''написать код который суммирует по модулю вводимые 5 чисел'''
if fname == "11":
  a = 0
  w = 0
  b = list()
  while a!=5:
      c = float(input())
      b.append(c)
      a+=1
  for i in b:
      if i < 0:
          i = i*(-1)
      w+=i
  print(w)

# манхэттенское расстояние
'''написать код который вычесляет кротчайший путь из точки а в б'''
if fname == "12":
  p1 = int(input())
  p2 = int(input())
  q1= int(input())
  q2= int(input())
  w = p1-p2
  d = q1-q2
  if w < 0:
      w = w*-1
  if d < 0:
      d = d*-1
  print(w+d)

# Python is a great language
'''написать код который должен вывести Python is a great language '''
if fname == "13":
  print('"Python is a great language", Said Fred. "I don',"'t ever remeber having this much fun before.",'"', sep="")

# как твое имя?
'''напсать код которому на входе подается только имя и фамилия и он вставляет их в предложение'''
if fname == "14":
  a = input()
  b = input()
  print("Hello",a,b,"! You have just delved into Python")

# футбольная команда
'''написать код который выводит название фут.команды и считывает количество символов в названии команды'''
if fname == "15":
  a = input()
  print("Футбольная команда",a,"имеет длину",len(a),"символов")

# три города
'''написать код который при введении названий трех городов выводит только самое длинное и короткре название'''
if fname == "16":
  a = input()
  b = input()
  c = input()
  if len(a)>len(b)>len(c) or len(c)>len(b)>len(a):
      print(a)
      print(c)
  elif len(a)>len(c)>len(b) or len(b)>len(c)>len(a):
      print(a)
      print(b)
  else:
      print(b)
      print(c)

# арифмитические строки
'''написать код который выесняет можно ли из длин введеных данных составить арифмитическую прогресию'''
if fname == "17":
  a = input()
  b = input()
  c = input()
  if len(a)+len(b)==len(c) or len(a)+len(c)==len(b) or len(b)+len(c)==len(a):
      print('yes')
  else:
      print('no')

# цвет настроения синий
'''написать код который ищет слово синий в предложении и если оно есть то выводит да в противном случае нет'''
if fname == "18":
  a = input()
  if "синий" in a:
      print('о да тут есть синий')
  else:
      print('синий отсутствует')

# отдыхаем ли?
'''написать код который ищет слово воскресенье или суббота в предложении и если оно есть то выводит да в противном случае нет'''
if fname == "19":
  a = input()
  if "воскресенье" in a or "суббота" in a:
      print('долгожданные выходные')
  else:
      print('опять работа')

# коректный емаил
'''написать код который ищет символы "@." в предложении и если оно есть то выводит да в противном случае нет'''
if fname == "20":
  a = input()
  if "." in a and "@" in a:
      print('email верный')
  else:
      print('ошибка попробуйте еще раз')

# евклидово растояние
'''написать код который находит растояние между двумя точками'''
if fname == "21":
  x1 = float(input())
  x2 = float(input())
  y1 = float(input())
  y2 = float(input())
  a = (((x1-x2)**2)+((y1-y2)**2))**0.5
  print(a)

# площадь и длина
'''написать код который расчитывает площадь круга и длинну окружности по заданному радиусу'''
if fname == "22":
  import math
  a = float(input())
  print(math.pi*(a**2))
  print((math.pi*2)*a)

# средние значения
'''написать код который по 2 заданым числам находит средние числа'''
if fname == "23":
  a = float(input())
  b = float(input())
  c = 0.5
  print('Арифметик ',(a+b)/2)
  print('Геометрик ',(a*b)**c)
  print('гармоник ', (a*b*2)/(a+b))
  print('Квадрат', (((a**2)+(b**2))/2)**c)

# тригонометрическое вырожение
'''написать код вычесляющий тригонометрическое вырожение по заданному х'''
if fname == "24":
  import math
  x = float(input())
  sin1 = math.sin(x)
  cos1 = math.cos(x)
  tan1 = math.tan(x)**2
  print('sin x = ', sin1)
  print('cos x = ', cos1)
  print('tan^2 x = ', tan1)
  r = (x*math.pi)/180
  print('r = ',r)

# пол и потолок
''' '''
if fname == "25":
  print()

# квадратное уровнение
''''''
if fname == "26":
  print()

# правильный многоугольник
'''написать код который находит площадь правильного многоугольника'''
if fname == "27":
  import math
  a = float(input())
  b = float(input())
  s = (a*(b**2)/(4*math.tan(math.pi/a)))
  print(s)

taskname = input("Какую функцию запустить?\n")
taskmanager(taskname)
