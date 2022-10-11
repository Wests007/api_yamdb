import csv

from reviews.models import (User, Genre, Category, Title,
                            GenreTitle, Review, Comment)
from api_yamdb.api_yamdb.settings import DATA_IMPORT_LOCATION


def users_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/users.csv',
        'r',
        encoding='utf-8'
    ) as users_csv:
        dataReader = csv.DictReader(users_csv)
        
        for row in dataReader:
            user = User()
            user.id = row['id']
            user.username = row['username']
            user.email = row['email']
            if User.objects.filter(id=user.id).exists():
                self.stdout.write(
                    f'В базе уже есть пользователь с id={user.id}.'
                )
            elif User.objects.filter(username=user.username).exists():
                self.stdout.write(
                    f'В базе уже есть пользователь с '
                    f'username={user.username}.'
                )
            elif User.objects.filter(email=user.email).exists():
                self.stdout.write(
                    f'В базе уже есть пользователь с email={user.email}.'
                )
            else:
                user.role = row['role']
                user.bio = row['bio']
                user.first_name = row['first_name']
                user.last_name = row['last_name']
                user.save()
                self.stdout.write(
                    f'Пользователь {user.username} внесен в базу.'
                )

def genres_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/genre.csv',
        'r',
        encoding='utf-8'
    ) as genre_csv:
        dataReader = csv.DictReader(genre_csv)
        
        for row in dataReader:
            genre = Genre()
            genre.id = row['id']
            genre.name = row['name']
            genre.slug = row['slug']
            if Genre.objects.filter(id=genre.id).exists():
                self.stdout.write(
                    f'В базе уже есть жанр с id={genre.id}.'
                )
            elif Genre.objects.filter(name=genre.name).exists():
                self.stdout.write(
                    f'В базе уже есть жанр с name={genre.name}.'
                )
            elif Genre.objects.filter(slug=genre.slug).exists():
                self.stdout.write(
                    f'В базе уже есть жанр со slug={genre.slug}.'
                )
            else:
                genre.save()
                self.stdout.write(
                    f'Жанр {genre.name} внесен в базу.'
                )

def categories_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/category.csv',
        'r',
        encoding='utf-8'
    ) as category_csv:
        dataReader = csv.DictReader(category_csv)
        
        for row in dataReader:
            category = Category()
            category.id = row['id']
            category.name = row['name']
            category.slug = row['slug']
            if Category.objects.filter(id=category.id).exists():
                self.stdout.write(
                    f'В базе уже есть категория с id={category.id}.'
                )
            elif Category.objects.filter(name=category.name).exists():
                self.stdout.write(
                    f'В базе уже есть категория с name={category.name}.'
                )
            elif Category.objects.filter(slug=category.slug).exists():
                self.stdout.write(
                    f'В базе уже есть категория со slug={category.slug}.'
                )
            else:
                category.save()
                self.stdout.write(
                    f'Категория {category.name} внесена в базу.'
                )

def titles_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/titles.csv',
        'r',
        encoding='utf-8'
    ) as titles_csv:
        dataReader = csv.DictReader(titles_csv)
        
        for row in dataReader:
            try:
                title = Title()
                title.id = row['id']
                title.name = row['name']
                category_id = row['category']
                title.category = Category.objects.get(id=category_id)
                if Title.objects.filter(id=title.id).exists():
                    self.stdout.write(
                        f'В базе уже есть произведение с id={title.id}.'
                    )
                elif Title.objects.filter(
                    name=title.name,
                    category=title.category
                ).exists():
                    self.stdout.write(
                        f'В базе уже есть произведение с name={title.name} '
                        f'в категории category={title.category}.'
                    )
                else:
                    title.year = row['year']
                    title.save()
                    self.stdout.write(
                        f'Произведение {title.name} внесено в базу.'
                    )
            except Category.DoesNotExist:
                self.stdout.write(
                    f'Категории с id={category_id} нет в базе. '
                    f'Сначала добавьте данную категорию в базу!'
                )

def genres_titles_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/genre_title.csv',
        'r',
        encoding='utf-8'
    ) as genre_title_csv:
        dataReader = csv.DictReader(genre_title_csv)
        
        for row in dataReader:
            try:
                genre_title = GenreTitle()
                genre_title.id = row['id']
                title_id = row['title_id']
                genre_id = row['genre_id']
                genre_title.title = Title.objects.get(id=title_id)
                genre_title.genre = Genre.objects.get(id=genre_id)
                if GenreTitle.objects.filter(id=genre_title.id).exists():
                    self.stdout.write(
                        f'В базе уже есть связка жанр-произведение '
                        f'с id={genre_title.id}.'
                    )
                elif GenreTitle.objects.filter(
                    title=genre_title.title,
                    genre=genre_title.genre
                ).exists():
                    self.stdout.write(
                        f'В базе уже есть связка жанр-произведение '
                        f'для произведения {genre_title.title} '
                        f'и жанра {genre_title.genre}.'
                    )
                else:
                    genre_title.save()
                    self.stdout.write(
                        f'Связка жанр-произведение с id={genre_title.id} '
                        f'внесена в базу.'
                    )
            except Title.DoesNotExist or Genre.DoesNotExist:
                self.stdout.write(
                    f'Произведения с id={title_id} '
                    f'или жанра с id={genre_id} нет в базе. '
                    f'Сначала добавьте их в базу!'
                )

def reviews_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/review.csv',
        'r',
        encoding='utf-8'
    ) as review_csv:
        dataReader = csv.DictReader(review_csv)
        
        for row in dataReader:
            try:
                review = Review()
                review.id = row['id']
                title_id = row['title_id']
                author_id = row['author']
                review.title = Title.objects.get(id=title_id)
                review.author = User.objects.get(id=author_id)
                if Review.objects.filter(id=review.id).exists():
                    self.stdout.write(
                        f'В базе уже есть отзыв с id={review.id}.'
                    )
                elif Review.objects.filter(
                    title=review.title,
                    author=review.author
                ).exists():
                    self.stdout.write(
                        f'В базе уже есть отзыв автора {review.author} '
                        f'к произведению {review.title}.'
                    )
                else:
                    review.text = row['text']
                    review.score = row['score']
                    review.pub_date = row['pub_date']
                    review.save()
                    self.stdout.write(
                        f'Отзыв к произведению {review.title} '
                        f'от автора {review.author} добавлен в базу.'
                    )
            except Title.DoesNotExist or User.DoesNotExist:
                self.stdout.write(
                    f'Произведения с id={title_id} '
                    f'или пользователя c id={author_id} нет в базе. '
                    f'Сначала добавьте их в базу!'
                )

def comments_to_db(self):
    with open(
        f'{DATA_IMPORT_LOCATION}/comments.csv',
        'r',
        encoding='utf-8'
    ) as comments_csv:
        dataReader = csv.DictReader(comments_csv)
        
        for row in dataReader:
            try:
                comment = Comment()
                comment.id = row['id']
                review_id = row['review_id']
                author_id = row['author']
                comment.review = Review.objects.get(id=review_id)
                comment.author = User.objects.get(id=author_id)
                comment.text = row['text']
                if Comment.objects.filter(id=comment.id).exists():
                    self.stdout.write(
                        f'В базе уже есть комментарий с id={comment.id}.'
                    )
                elif Comment.objects.filter(
                    review=comment.review,
                    author=comment.author,
                    text=comment.text
                ).exists():
                    self.stdout.write(
                        f'В базе уже есть комментарий с таким текстом '
                        f'к отзыву {comment.review} '
                        f'от автора {comment.author}.'
                    )
                else:
                    comment.pub_date = row['pub_date']
                    comment.save()
                    self.stdout.write(
                        f'Комментарий к отзыву {comment.review} '
                        f'от автора {comment.author} добавлен в базу.'
                    )
            except Review.DoesNotExist or User.DoesNotExist:
                self.stdout.write(
                    f'Отзыва с id={review_id} '
                    f'или пользователя c id={author_id} нет в базе. '
                    f'Сначала добавьте их в базу!'
                )
