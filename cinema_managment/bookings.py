
def add_booking(bookings, sessions, halls):
    print("\n--- Бронирование места ---")

    if len(sessions) == 0:
        print("Сначала создайте сеанс!")
        return

    print("\n--- Список сеансов ---")
    for session in sessions:
        print(
            f"ID: {session['id']} | "
            f"Дата: {session['date']} | "
            f"Время: {session['time']}"
        )

    try:
        session_id = int(input("Введите ID сеанса: "))
    except ValueError:
        print("Ошибка! Введите число.")
        return

    selected_session = None

    for session in sessions:
        if session["id"] == session_id:
            selected_session = session
            break

    if selected_session is None:
        print("Сеанс не найден!")
        return

    selected_hall = None

    for hall in halls:
        if hall["id"] == selected_session["hall_id"]:
            selected_hall = hall
            break

    if selected_hall is None:
        print("Кинозал не найден!")
        return

    customer_name = input("Введите имя клиента: ").strip()

    if customer_name == "":
        print("Имя клиента не может быть пустым!")
        return

    try:
        row = int(input("Введите номер ряда: "))
        seat = int(input("Введите номер места: "))
    except ValueError:
        print("Ошибка! Введите целые числа.")
        return

    if row < 1 or row > selected_hall["rows"]:
        print("Такого ряда нет!")
        return

    if seat < 1 or seat > selected_hall["seats_per_row"]:
        print("Такого места нет!")
        return

    for booking in bookings:
        if (
            booking["session_id"] == session_id
            and booking["row"] == row
            and booking["seat"] == seat
        ):
            print("Это место уже забронировано!")
            return

    booking_id = max(
        [booking["id"] for booking in bookings],
        default=0
    ) + 1

    booking = {
        "id": booking_id,
        "session_id": session_id,
        "customer_name": customer_name,
        "row": row,
        "seat": seat
    }

    bookings.append(booking)

    print("Место успешно забронировано!")


def show_bookings(bookings, sessions):
    print("\n--- Список бронирований ---")

    if len(bookings) == 0:
        print("Бронирований пока нет.")
        return

    for booking in bookings:
        print(f"\nID бронирования: {booking['id']}")
        print(f"Клиент: {booking['customer_name']}")
        print(f"ID сеанса: {booking['session_id']}")
        print(f"Ряд: {booking['row']}")
        print(f"Место: {booking['seat']}")

        for session in sessions:
            if session["id"] == booking["session_id"]:
                print(f"Дата сеанса: {session['date']}")
                print(f"Время сеанса: {session['time']}")
                break

        print("------------------------")


def cancel_booking(bookings):
    print("\n--- Отмена бронирования ---")

    if len(bookings) == 0:
        print("Бронирований пока нет.")
        return

    try:
        booking_id = int(input("Введите ID бронирования: "))
    except ValueError:
        print("Ошибка! Введите число.")
        return

    for booking in bookings:
        if booking["id"] == booking_id:
            bookings.remove(booking)
            print("Бронирование отменено!")
            return

    print("Бронирование с таким ID не найдено!")
