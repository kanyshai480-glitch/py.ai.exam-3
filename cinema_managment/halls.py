def add_hall(halls):
    name = input("Введите название зала: ").strip()

    if not name:
        print("Ошибка: название зала не должно быть пустым.")
        return

    try:
        rows = int(input("Введите количество рядов: "))
        seats = int(input("Введите количество мест в каждом ряду: "))

        if rows <= 0 or seats <= 0:
            print("Ошибка: количество рядов и мест должно быть положительным числом.")
            return

    except ValueError:
        print("Ошибка: введите целое число.")
        return

    hall_id = max((hall["id"] for hall in halls), default=0) + 1

    new_hall = {
        "id": hall_id,
        "name": name,
        "rows": rows,
        "seats_per_row": seats
    }

    halls.append(new_hall)
    print(f"Зал '{name}' успешно добавлен!")


def show_halls(halls):
    if not halls:
        print("Список залов пока пуст.")
        return

    print("\nСписок доступных залов:")

    for hall in halls:
        capacity = hall["rows"] * hall["seats_per_row"]

        print(
            f"ID: {hall['id']} | "
            f"Название: {hall['name']} | "
            f"Вместимость: {capacity} мест"
        )
        
