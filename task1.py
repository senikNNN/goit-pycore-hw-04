from pathlib import Path

file_path = Path("./file_task1.txt")

def read_workers_file(path: Path) -> list:
    """
        Read the employee file at the specified path
    """
    data = list()
    with open(path, "r") as file:
        for line in file.readlines():
            text = line.split(",")
            data.append({"name": text[0], "salary": int(text[1])})
    return data


def total_salary(path: Path) -> tuple:
    """
        Returns the tuple with total and average salary of employees from the specified file
    """
    data = read_workers_file(path)
    sum = 0
    for developer in data:
        sum += developer["salary"]
    avg_sum = sum / len(data)
    return (sum, avg_sum)


total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати:\t{total}\nСередня заробітна плата:\t{average}")