def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run_task2():
    display_chars("exported_items.csv", 5)
    display_line("exported_items.csv")
    display_text("exported_items.csv")

if __name__ == "__main__":
    run_task2()