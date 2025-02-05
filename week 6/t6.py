import csv


def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")


def run_task2():
    extract("exported_items.csv")


if __name__ == "__main__":
    run_task2()