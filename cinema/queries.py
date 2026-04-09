import django, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema.settings')
django.setup()

from movies.models import Genre, Director, Movie, Review
from django.db.models import Count, Avg, Min, Max, Q, F

print("--- Базова вибірка ---")
titles = Movie.objects.values_list("title", flat=True)
print(list(titles))

print("\n--- Фільтрація за рейтингом ---")
top_movies = Movie.objects.filter(rating__gte=8.5).order_by("-rating")
for m in top_movies:
    print(f"{m.title}: {m.rating}")

print("\n--- Пошук по тексту з Q-об'єктами ---")
blade_or_dark = Movie.objects.filter(Q(title__icontains="Blade") | Q(title__icontains="Dark"))
print(list(blade_or_dark))

print("\n--- Фільтр через зв'язану таблицю ---")
nolan_films = Movie.objects.filter(director__last_name="Nolan")
print(f"Знайдено фільмів Нолана: {nolan_films.count()}")

print("\n--- Комбінована фільтрація ---")
scifi_recent = Movie.objects.filter(genre__name="Sci-Fi", year__gt=2015).order_by("year")
print(list(scifi_recent))

print("\n--- exclude() ---")
not_drama_comedy = Movie.objects.exclude(Q(genre__name="Drama") | Q(genre__name="Comedy"))
for m in not_drama_comedy:
    genre_name = m.genre.name if m.genre else "без жанру"
    print(f"{m.title} — {genre_name}")

print("\n--- Пагінація ---")
by_rating = Movie.objects.order_by("-rating")
page1 = by_rating[:4]
page2 = by_rating[4:8]
print("Сторінка 1:", list(page1))
print("Сторінка 2:", list(page2))

print("\n--- Кількість фільмів у кожному жанрі ---")
genres_stat = Genre.objects.annotate(movie_count=Count("movie")).order_by("-movie_count")
for g in genres_stat:
    print(f"{g.name}: {g.movie_count}")

print("\n--- Середній рейтинг ---")
total_avg = Movie.objects.aggregate(avg=Avg("rating"))
print(f"Загальний середній рейтинг: {total_avg['avg']}")
directors_avg = Director.objects.annotate(avg_rating=Avg("movie__rating")).values("last_name", "avg_rating").order_by("-avg_rating")
for d in directors_avg:
    print(f"{d['last_name']}: {d['avg_rating']}")

print("\n--- Фільми без відгуків ---")
no_reviews = Movie.objects.filter(review__isnull=True)
print("Фільми без відгуків:", [m.title for m in no_reviews])

print("\n--- Масовий UPDATE ---")
updated_count = Movie.objects.filter(rating__lt=7.8).update(is_public=False)
print(f"Оновлено: {updated_count} фільмів")

print("\n--- Оновлення через F() ---")
tarantino_update = Movie.objects.filter(director__last_name="Tarantino").update(rating=F("rating") + 0.2)
print(f"Оновлено рейтингів Тарантіно: {tarantino_update}")

print("\n--- Відгуки конкретного фільму ---")
try:
    inception = Movie.objects.get(title="Inception")
    reviews = inception.review_set.all()
    print(f"Відгуки до '{inception.title}':")
    for r in reviews:
        print(f"- {r.score}: {r.text}")
    avg_score = inception.review_set.aggregate(avg=Avg("score"))
    print(f"Середня оцінка відгуків: {avg_score['avg']}")
except Movie.DoesNotExist:
    print("Фільм 'Inception' не знайдено")

print("\n--- Найкращий режисер за середнім рейтингом ---")
best_director = Director.objects.annotate(avg=Avg("movie__rating")).order_by("-avg").first()
if best_director:
    print(f"Найкращий режисер: {best_director.first_name} {best_director.last_name} (Рейтинг: {best_director.avg})") 

print("\n--- Власний запит ---")
#Тут я хочу вивести кількість фільмів тривалість яких більше за 150 хв
long_movies = Movie.objects.filter(duration__gt=150).order_by("-duration")
print(f"Фільми тривалість яких більше за 150 хв - {long_movies.count()} / {Movie.objects.count()}")
