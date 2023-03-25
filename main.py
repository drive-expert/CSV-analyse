import csv
import random


def csv_create(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id', f'name', 'age', 'gender'])
        any_list = ['свадьба', 'AVON', 'мужской', 'женский','качели']
        for num in range(256):
            a = random.randrange(0,4)
            b = random.randrange(0,4)
            c = random.randrange(0,4)
            d = random.randrange(0,4)
            any_num_list = [a,b,c,d]
            writer.writerow([1, f'John{num} {any_list[any_num_list[0]]}', 30,'male'])
            writer.writerow([2, f'Jane{num} {any_list[any_num_list[1]]}', 25, 'female'])
            writer.writerow([3, f'Mary{num} {any_list[any_num_list[2]]}', 30,'male'])
            writer.writerow([4, f'Mike{num} {any_list[any_num_list[3]]}', 25, 'female'])



def csv_analysis(filename): #убрать все строки если поле "name" содержит любое слово из списка words
    words = ["AVON", "мужской", "свадьба"]
    fine_dict = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ch = 1
        chx = 1
        for row in reader:
            print(f'{ch}-{row}')
            if any(map(row['name'].lower().__contains__, map(str.lower, words))) == False:
                fine_dict.update({chx: row['name']})
                chx += 1
            ch += 1
        print(fine_dict)

csv_create('data.csv')
csv_analysis('data.csv')
