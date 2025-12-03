
import re
# def extract_data():
with open("reviews.txt", "r", encoding="utf-8") as f:
    text = f.read()

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"

emails = re.findall(email_pattern, text)
phone_numbers = re.findall(phone_pattern, text)
 
with open("emails.txt", "w", encoding="utf-8") as f:
    for email in emails:
        f.write(email + "\n")

with open("phone_numbers.txt", "w", encoding="utf-8") as f:
    for phone in phone_numbers:
        f.write(phone + "\n")

print("emails and phone numbers successfully extracted and saved!")

# if __name__ == "__main__":
    # extract_data()