from getpass import getpass
correct_pin = "1234"
attempt_n = 1
total_attempts = 3

while attempt_n <= total_attempts:
    supplied_pin = getpass("Enter your PIN: ")
    if supplied_pin == correct_pin:
        print('Pin accepted')
        break
    else:
        print('Pin incorrect, this is attempt no. ', attempt_n)
    attempt_n += 1



