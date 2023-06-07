import random

def mini_calculator():
    count_questions, correct_answers = 0, 0
    print("Which level do you want? Enter a number:\n"
          "1 - simple operations with numbers 2-9\n"
          "2 - integral squares of 11-29")
    finished = False
    while not finished:
        choice = input()
        if choice == "1":
            level = "1"
            while count_questions < 5:
                result = int()
                a_number, operator, b_number = random.randint(2, 9), random.choice(["+", "*", "-"]), random.randint(2,
                                                                                                                    9)
                if operator == "+":
                    result = a_number + b_number
                elif operator == "-":
                    result = a_number - b_number
                elif operator == "*":
                    result = a_number * b_number
                print(f"{a_number} {operator} {b_number}")
                while True:
                    try:
                        answer = int(input())
                        break
                    except:
                        print("Incorrect format.")
                        continue
                if answer == result:
                    print("Right!")
                    count_questions += 1
                    correct_answers += 1
                else:
                    print("Wrong!")
                    count_questions += 1
            finished = True
        elif choice == "2":
            while count_questions < 5:
                number = random.randint(11, 29)
                square_number = number ** 2
                print(number)
                while True:
                    user_input = input()
                    if not user_input.isdigit():
                        print("Incorrect format.")
                        continue
                    else:
                        break
                if user_input == str(square_number):
                    print("Right!")
                    count_questions += 1
                    correct_answers += 1
                else:
                    print("Wrong!")
                    count_questions += 1
            finished= True
        else:
            print("Incorrect format.")
    print(f"Your mark is {correct_answers}/5. "
          f"Would you like to save your result to the file? Enter yes or no.")
    save_input = input().lower()
    if save_input == "yes" or save_input == "y":
        print("What is your name?")
        name_input = input()
        level = "1 (simple operations with numbers 2-9)" if choice == "1" else "2 (integral squares of 11-29)"
        with open("results.txt", "a") as write_file:
            write_file.write(f"{name_input}: {correct_answers}/5 in level {level}.\n")
        print('The results are saved in "results.txt".')
    elif save_input == "no" or save_input == "n":
        return None
    else:
        print("Incorrect format.")

mini_calculator()