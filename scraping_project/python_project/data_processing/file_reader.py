def read_data(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name, age = line.strip().split(",")
            data.append((name, int(age)))
    return data