import csv
# def csf_file(name,email):
#     with open("class/csv.txt", mode="a") as f:
#         reader = csv.writer(f, delimiter = ",")
#         reader.writerow([name,email])

# def write():
#     name= input("Enter the name")
#     email = input('Enter the mail: ')
#     return name, email
# for i in range(5):
#     name, email = write()
#     print(name)
#     csf_file(name,email)

# def read_csv():
#     with open("class/csv.txt") as f:
#         csv_reader = csv.reader(f,delimiter=",")
#         for data in csv_reader:
#             print(data)
# read_csv()


def dict_csv():
    with open("datas.csv") as r:
        csv_reader = csv.DictReader(r , delimiter = "-")
        print(csv_reader)
        for data in csv_reader:
            print(data)
dict_csv()
