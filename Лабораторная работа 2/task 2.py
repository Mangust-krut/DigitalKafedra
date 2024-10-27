money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
total = money_capital+salary
month = 1
while True:
    if month == 1:
        total -= spend
    total += salary
    spend *= 1.05
    total -= spend
    if total < 0: break
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
