def recognize_number(user_input):
    user_input = user_input.strip()

    if user_input == '0':
        return "Ви ввели нуль"

    if ',' in user_input:
        user_input = user_input.replace(',', '.')

    if user_input.replace('.', '', 1).lstrip('-').isdigit():
        number = float(user_input)
        if '.' in user_input:
            if user_input.startswith('-'):
                return f"Ви ввели негативне дробове число: {number}"
            else:
                return f"Ви ввели позитивне дробове число: {number}"
        else:
            number = int(user_input)
            if number < 0:
                return f"Ви ввели негативне ціле число: {number}"
            else:
                return f"Ви ввели позитивне ціле число: {number}"

    return "Ви ввели некоректне число"


while True:
    user_input = input("Введіть число або 'вихід', 'exit', 'quit', 'e' або 'q': ").lower()
    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        break
    else:
        print(recognize_number(user_input))
