def personal_sum(numbers):
    sum = 0
    incorrect_data = 0

    for i in numbers:
        try:
            sum += i
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы: {i}')

    return (sum, incorrect_data)

def calculate_average(numbers):

    try:
        sum= personal_sum(numbers)
        result = sum[0] / (len(numbers) - sum[1])
    except ZeroDivisionError as exc:
        result = 0
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных.')
        result = None

    return result

if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка",3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')