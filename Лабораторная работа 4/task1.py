# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    ...  # TODO считать содержимое csv файла
    data = []
    with open('input.csv',newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            data.append(i)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open('output.json','w',encoding='utf-8') as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False,indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
