import csv

def get_csv_entries(file_input, file_output):
    with open(file_output, "a") as f:
        f.write("|numero|autore|titolo|\n")
        f.write("|-|-|-|\n")
    with open(file_input, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for i, row in enumerate(csv_reader):
                print(table(row[0], row[1], row[2]))
                with open(file_output, "a") as f:
                    f.write(table(row[0], row[1], row[2]))

def table(number, title, author):
    return "|"+number+"|"+title+"|"+author+"|"+"\n"

file_name = input("Enter the file path(without extension): ")
get_csv_entries(file_name+".csv", file_name+".md")
