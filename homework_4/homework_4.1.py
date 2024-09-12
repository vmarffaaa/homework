# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)

with open('emails.txt', 'r') as file:
    emails = file.readlines()

with open('gmail_emails.txt', 'w') as new_file:
    for gmail in emails:
        email = gmail.split()[-1]
        if email.endswith('@gmail.com'):
            new_file.write(email + '\n')
