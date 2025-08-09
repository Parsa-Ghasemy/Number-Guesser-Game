def input_validator(start, end):
    while True:
        try:
            user_input=int(input("Enter a number:"))
            if start<=user_input<=end:
                return user_input
            else:
                    print(f'invalid number please enter a number between {start} and {end}')

        except ValueError:
             print('invalid, Enter a number')


if __name__ == "__main__":
     input_validator(2,10)