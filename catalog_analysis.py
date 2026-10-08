import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Разминка: переменные, числа, math


def average_rating(movies):
    ''' вычисляет среднюю оценку по каталогу'''
    total_rating = 0

    for movie in movies:
        total_rating += movie['rating']

    return round(total_rating / len(movies), 1)


# print(average_rating(movies))


def catalog_age_stats(movies, current_year=2026):
    '''возвращает кортеж (самый старый фильм в годах,
    самый новый фильм в годах, средний возраст фильма в каталоге)'''
    oldest = 2026
    newest = 0
    total_ages = 0
    for movie in movies:
        if movie['year'] < oldest:
            oldest = movie['year']
        if movie['year'] > newest:
            newest = movie['year']

        total_ages += current_year - movie['year']

    return (oldest, newest, math.ceil(total_ages / len(movies)))


# print(catalog_age_stats(movies))


def duration_in_hours(minutes):
    '''переводит минуты в формат '2ч 35м' '''
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# print(duration_in_hours(movies[0]['duration_min']))

# Этап 2. Условия и match

def rating_tier(rating):
    '''возвращает категорию:
    "шедевр" (≥9), "хорошо" (7-8.9), "средне" (5-6.9), "слабо" (<5)'''

    if rating < 5:
        return 'слабо'
    elif rating <= 6.9:
        return 'средне'
    return 'хорошо' if rating <= 8.9 else 'шедевр'


# print(rating_tier(7))

def decade_label(year):
    '''возвращает метку "новые" (после 2020), "недавние" (2015-2020)
    или "старые" (раньше 2015)'''
    match year:
        case year if year > 2020:
            return 'новые'
        case year if year >= 2015:
            return 'недавние'
        case year if year < 2015:
            return 'старые'


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
    '''Считает количество фильмов с продолжительностью более x минут'''
    counter = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            counter += 1
    return counter


# threshold = 120
# print(
#     f"Количество фильмов длиннее {threshold} минут: {count_long_movies(movies, threshold)}")


# Этап 4. Строки

def normalize_title(title):
    words = title.split()
    norm_title = ''
    for word in words:
        norm_title += (word[0].upper() + word[1:] + ' ')
    return norm_title.strip()


# print(normalize_title('midnight in oslo'))

def make_slug(title):
    slug = title.lower().replace(' ', '-')
    return slug


# print(make_slug('The Dune Chronicles'))

def format_report_line(movie):
    ''' Создает отчет о фильме в формате:
    "Silent Hours (2016) — 6.4/10, 1ч 52м, жанры: drama, thriller
    '''
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
    '''Возвращает список названий фильмов, отсортированных по убыванию рейтинга'''
    titles_w_rating = {}
    for movie in movies:
        titles_w_rating[movie['title']] = movie['rating']

    titles_sorted = sorted(
        titles_w_rating, key=lambda i: titles_w_rating[i], reverse=True)
    return titles_sorted


# print(titles_sorted_by_rating(movies))


def top_n_by_rating(movies, n=3):
    '''Возвращает список из n кортежей (title, rating) — топ по рейтингу'''
    titles_rating_list = [(movie['title'], movie['rating'])
                          for movie in movies]
    top_n = sorted(titles_rating_list,
                   key=lambda i: i[1], reverse=True)
    return top_n[:n]


# print(top_n_by_rating(movies, 3))

# Этап 6. Словари

def count_by_genre(movies):
    '''Возвращает словарь {жанр: количество фильмов}'''

    genre_counts = {}
    for movie in movies:
        genre_counts[] = movie['genres'].get()

    return genre_counts


# print(count_by_genre(movies))
