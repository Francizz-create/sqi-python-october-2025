from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

def main():
    # Read local file data
    file_data = read_data("data.txt")
    print("📂 Data from file:")
    for name, age in file_data:
        print(f"{name} — {age} years old")

    # Fetch web data
    web_data = fetch_user_data()
    print("\n Data from web (JSONPlaceholder users):")
    for user in web_data:
        print(user)

if __name__ == "__main__":
    main()