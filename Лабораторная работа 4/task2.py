import json
# TODO решите задачу
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as file:
        array = json.load(file)
    summa = 0
    for i in array:
        summa += i['score']*i['weight']
    summa = round(summa,3)
    return summa
print(task())
