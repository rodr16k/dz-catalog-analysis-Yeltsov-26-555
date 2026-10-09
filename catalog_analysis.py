import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# Этап 1. Разминка: переменные, числа, math


def average_rating(movies):
    """вычисляет среднюю оценку по каталогу"""
    total_rating = 0

    for movie in movies:
        total_rating += movie["rating"]

    return round(total_rating / len(movies), 1)


# print(average_rating(movies))


def catalog_age_stats(movies, current_year=2026):
    """возвращает кортеж (самый старый фильм в годах,
    самый новый фильм в годах, средний возраст фильма в каталоге)"""
    oldest = 2026
    newest = 0
    total_ages = 0
    for movie in movies:
        if movie["year"] < oldest:
            oldest = movie["year"]
        if movie["year"] > newest:
            newest = movie["year"]

        total_ages += current_year - movie["year"]

    return (oldest, newest, math.ceil(total_ages / len(movies)))


# print(catalog_age_stats(movies))


def duration_in_hours(minutes):
    """переводит минуты в формат '2ч 35м'"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# print(duration_in_hours(movies[0]['duration_min']))

# Этап 2. Условия и match


def rating_tier(rating):
    """возвращает категорию:
    "шедевр" (≥9), "хорошо" (7-8.9), "средне" (5-6.9), "слабо" (<5)"""

    if rating < 5:
        return "слабо"
    elif rating <= 6.9:
        return "средне"
    return "хорошо" if rating <= 8.9 else "шедевр"


# print(rating_tier(7))


def decade_label(year):
    """возвращает метку "новые" (после 2020), "недавние" (2015-2020)
    или "старые" (раньше 2015)"""
    match year:
        case year if year > 2020:
            return "новые"
        case year if year >= 2015:
            return "недавние"
        case year if year < 2015:
            return "старые"


# print(decade_label(2023))

# Этап 3. Циклы

# # Вывод фильмов, которые не относятся к жанру 'комедия'
# for movie in movies:
#     if 'comedy' in movie['genres']:
#         continue
#     print(movie['title'])

# # Вывод первого фильма с оценкой > 9
# i = 0
# while i < len(movies):
#     if movies[i]['rating'] > 9:
#         print(movies[i]['title'])
#         break
#     i += 1
# else:
#     print('Шедевров не найдено')


def count_long_movies(movies, threshold):
    """Считает количество фильмов с продолжительностью более x минут"""
    counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counter += 1
    return counter


# threshold = 120
# print(
#     f"Количество фильмов длиннее {threshold} минут: "
#     f"{count_long_movies(movies, threshold)}"
#     )


# Этап 4. Строки


def normalize_title(title):
    words = title.split()
    norm_title = ""
    for word in words:
        norm_title += word[0].upper() + word[1:] + " "
    return norm_title.strip()


# print(normalize_title('midnight in oslo'))


def make_slug(title):
    slug = title.lower().replace(" ", "-")
    return slug


# print(make_slug('The Dune Chronicles'))


def format_report_line(movie):
    """Создает отчет о фильме в формате:
    "Silent Hours (2016) — 6.4/10, 1ч 52м, жанры: drama, thriller
    """
    report = (
        f"{normalize_title(movie['title'])}"
        f" ({movie['year']}) — {movie['rating']}/10,"
        f" {duration_in_hours(movie['duration_min'])},"
        f" жанры: {', '.join(sorted(movie['genres'], key=str.lower))}"
    )
    return report


# print(format_report_line(movies[2]))

# Этап 5. Списки


def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга"""
    titles_w_rating = {}
    for movie in movies:
        titles_w_rating[movie["title"]] = movie["rating"]

    titles_sorted = sorted(
        titles_w_rating, key=lambda i: titles_w_rating[i], reverse=True
    )
    return titles_sorted


# print(titles_sorted_by_rating(movies))


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу"""
    titles_rating_list = [(movie["title"], movie["rating"])
                          for movie in movies]
    top_n = sorted(titles_rating_list, key=lambda i: i[1], reverse=True)
    return top_n[:n]


# print(top_n_by_rating(movies, 3))

# Этап 6. Словари


def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}"""

    genre_counts = {}

    for movie in movies:
        genres = movie.get("genres", [])
        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


# print(count_by_genre(movies))


def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}"""
    actor_films = {}
    for movie in movies:
        title = movie["title"]
        actors = movie.get("actors", [])
        for actor in actors:
            films_list = actor_films.get(actor, [])
            films_list.append(title)
            actor_films[actor] = films_list
    return actor_films


# print(actor_filmography(movies))

# Создаем словарь {title: rating}
# только для фильмов с рейтингом выше среднего
# с помощью генератора словаря
above_avg_movies = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_rating(movies)
}
# print(above_avg_movies)


# Этап 7. Множества


def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога"""
    genres_set = set()
    for movie in movies:
        genres_set.update(movie["genres"])
    return genres_set


# print(all_genres(movies))


def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах"""
    actors_set = set(movie1["actors"]) & set(movie2["actors"])
    return actors_set


# print(common_actors(movies[0], movies[5]))


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a,
    но не встречающиеся в movies_b"""
    genres_a = set()
    genres_b = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    for movie in movies_b:
        genres_b.update(movie["genres"])
    return genres_a - genres_b


# print(genres_only_in_one(movies[5:6], movies[:5]))

# Этап 8. Итераторы и генераторы


def iter_high_rated(movies, min_rating=8.0):
    """Отдает фильмы с рейтингом не ниже min_rating"""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))


total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
# print(total_duration)


# Этап 9. Итоговый отчет
def build_report(movies):
    """Выводит полный отчет по каталогу"""
    print("==========\nОТЧЕТ ПО КАТАЛОГУ ФИЛЬМОВ\n==========")
    print(
        f"Средняя оценка фильмов: {average_rating(movies)}\n"
        f"Самый старый фильм: {catalog_age_stats(movies)[0]}\n"
        f"Самый новый фильм: {catalog_age_stats(movies)[1]}"
    )

    print("\nТоп 3 фильма:")
    top_movies = top_n_by_rating(movies, n=3)
    movies_dict = {movie["title"]: movie for movie in movies}
    for title, rating in top_movies:
        movie_data = movies_dict.get(title)
        if movie_data:
            print(f"   {format_report_line(movie_data)}")

    print("\nФильмов по жанрам:")
    for genre, count in count_by_genre(movies).items():
        print(f"{genre}: {count}")

    print(f"\nВ каталоге представлены жанры: {', '.join(all_genres(movies))}")


if __name__ == "__main__":
    build_report(movies)
