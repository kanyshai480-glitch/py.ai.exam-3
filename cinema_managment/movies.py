def add_movie(movies):
    name = input("Введите название фильма: ").strip()
    if not name:
        print("Название не может быть пустым!")
        return

    genre = input("Введите жанр фильма: ").strip()

    try:
        duration = int(input("Введите продолжительность (минуты): "))
    except ValueError:
        print("Ошибка! Введите число.")
        return

    if duration <= 0:
        print("Продолжительность должна быть положительной!")
        return

    movie = {
        "id": len(movies) + 1,
        "name": name,
        "genre": genre,
        "duration": duration
    }

    movies.append(movie)
    print("Фильм успешно добавлен!")
    
def show_movies(movies):
    if not movies:
        print("Список фильмов пуст.")
        return
    for movie in movies:
        print(
            f"ID: {movie['id']} | "
            f"Название: {movie['name']} | "
            f"Жанр: {movie['genre']} | "
            f"Продолжительность: {movie['duration']} мин."
    )
def delete_movie(movies):
    try:
        movie_id = int(input("Введите ID фильма для удаления: "))
    except ValueError:
        print("Ошибка! ID должен быть числом.")
        return
    for movie in movies:
        if movie["id"] == movie_id:
           movies.remove(movie)
           print("Фильм успешно удалён!")
           return

    print("Фильм с таким ID не найден.")