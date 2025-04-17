# 2025.04.15
# Muallif: Muhammadsodiq



reg_people = {

    "person1": "password1",

    "person2": "password2",

    "person3":"password3"

}



attempts_count = 0

max_amount = 3



while attempts_count < max_amount:

    input_name = input("Enter name: ")

    input_password = input("Enter password: ")



    if input_name in reg_people and reg_people[input_name] == input_password:

        print('Logged in!')

        break

    else:

        attempts_count += 1

    print(f"Bad name or password. Attempt {attempts_count} of {max_amount}")



if attempts_count == max_amount:

    print("Maximum login attempts reached. Try again later, bro!")