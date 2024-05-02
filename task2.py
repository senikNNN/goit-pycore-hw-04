from pathlib import Path

file_path = Path("./file_task2.txt")

def get_cats_info(path) -> list:
    """
        Reads the attributes of cats from a file and returns them as a list of dictionaries
    """
    data = list()
    try:
        with open(path, "r") as file:
            while True:
                line = file.readline()
                if line:
                    text = line.split(",")
                    data.append({"id": text[0], "name": text[1], "age": text[2].strip("\n")})
                else:
                    break
    except FileNotFoundError:
        print(f"File {file_path} not found")
    return data

print(get_cats_info(file_path))