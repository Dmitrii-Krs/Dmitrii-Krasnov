salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
k =0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for k in range(10):
    if k > 0:
        spend = spend * (1 + increase)

    money_capital = money_capital + salary - spend
    if k == 9:
        money_capital = round(- money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

