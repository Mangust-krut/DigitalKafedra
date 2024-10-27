salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
#money_capital = ?
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
spend_10_month = spend
for i in range(9):
    spend *= 1.03
    spend_10_month += spend
salary_10_month = salary*10
money_capital = round(spend_10_month-salary_10_month)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
