#ОПРЕДЕЛЕНИЕ ЗНАКА ЗОДИАКА

print(num:=int(input("Введите число: ")))
print(mon:=str(input("Введите месяц: ")))

x="Ваш знак зодиака: "

#Расчёт

if ((num >= 21) and (num <= 31) and (mon == 'январь') or (mon == 'Январь')):
    print(str(x)+"ВОДОЛЕЙ")
elif ((num >= 1) and (num <= 18) and (mon == 'февраль') or (mon == 'Февраль')):
    print(str(x)+"ВОДОЛЕЙ")
elif ((num >= 19) and (num <= 29) and (mon == 'февраль') or (mon == 'Февраль')):
    print(str(x)+"РЫБЫ")
elif (num >= 1) and (num <= 20) and (mon == 'март') or (mon == 'Март'):
    print(str(x)+"РЫБЫ")
elif (num >= 21) and (num <= 31) and (mon == 'март') or (mon == 'Март'):
    print(str(x)+"ОВЕН")
elif (num >= 1) and (num <= 20) and (mon == 'апрель') or (mon == 'Апрель'):
    print(str(x)+"ОВЕН")
elif (num >= 21) and (num <= 30) and (mon == 'апрель') or (mon == 'Апрель'):
    print(str(x)+"ТЕЛЕЦ")
elif (num >= 1) and (num <= 20) and (mon == 'май') or (mon == 'Май'):
    print(str(x)+"ТЕЛЕЦ")
elif (num >= 21) and (num <= 31) and (mon == 'май') or (mon == 'Май'):
    print(str(x)+"БЛИЗНЕЦЫ")
elif (num >= 21) and (num <= 30) and (mon == 'июнь') or (mon == 'Июнь'):
    print(str(x)+"БЛИЗНЕЦЫ")
elif (num >= 22) and (num <= 30) and (mon == 'июнь') or (mon == 'Июнь'):
    print(str(x)+"РАК")
elif (num >= 1) and (num <= 22) and (mon == 'июль') or (mon == 'Июль'):
    print(str(x)+"РАК")
elif (num >= 23) and (num <= 31) and (mon == 'июль') or (mon == 'Июль'):
    print(str(x)+"ЛЕВ")
elif (num >= 1) and (num <= 23) and (mon == 'август') or (mon == 'Август'):
    print(str(x)+"ЛЕВ")
elif (num >= 24) and (num <= 31) and (mon == 'август') or (mon == 'Август'):
    print(str(x)+"ДЕВА")
elif (num >= 1) and (num <= 23) and (mon == 'сентябрь') or (mon == 'Сентябрь'):
    print(str(x)+"ДЕВА")
elif (num >= 24) and (num <= 30) and (mon == 'сентябрь') or (mon == 'Сентябрь'):
    print(str(x)+"ВЕСЫ")
elif (num >= 1) and (num <= 23) and (mon == 'октябрь') or (mon == 'Октябрь'):
    print(str(x)+"ВЕСЫ")
elif (num >= 24) and (num <= 31) and (mon == 'октябрь') or (mon == 'Октябрь'):
    print(str(x)+"СКОРПИОН")
elif (num >= 1) and (num <= 22) and (mon == 'ноябрь') or (mon == 'Ноябрь'):
    print(str(x)+"СКОРПИОН")
elif (num >= 23) and (num <= 30) and (mon == 'ноябрь') or (mon == 'Ноябрь'):
    print(str(x)+"СТРЕЛЕЦ")
elif (num >= 1) and (num <= 21) and (mon == 'декабрь') or (mon == 'Декабрь'):
    print(str(x)+"СТРЕЛЕЦ")
elif (num >= 22) and (num <= 31) and (mon == 'декабрь') or (mon == 'Декабрь'):
    print(str(x)+"КОЗЕРОГ")
elif (num >= 1) and (num <= 20) and (mon == 'январь') or (mon == 'Январь'):
    print(str(x)+"КОЗЕРОГ")

print("Конец программы.🍨")