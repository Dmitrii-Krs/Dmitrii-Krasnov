# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f_input:
        with open(OUTPUT_FILENAME, "w") as f_output:
            reader = csv.DictReader(f_input)
    # TODO Сериализовать в файл с отступами равными 4
            data =[row for row in reader]
            dict_json = json.dump(data, f_output, indent=4)
    return dict_json

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

