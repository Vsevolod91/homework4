"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
personal_account = 0
purchase_history = {}

while True:
    print("Главное меню:")
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        refill = int(input("Введите сумму для пополнения"))
        personal_account += refill
        print("Счет пополнен. Состояние счета: {} рублей.".format(personal_account))

    elif choice == '2':
        budget_purchase = int(input("Введите сумму покупки: "))
        if budget_purchase > personal_account:
            print("Денег на покупку не хватает")

        else:
            purchase_name = input("Введите наименование покупки: ")
            purchase_history[purchase_name] = budget_purchase
            personal_account -= budget_purchase

    elif choice == '3':
        print(purchase_history)

    elif choice == '4':
        break

    else:
        print('Неверный пункт меню')
