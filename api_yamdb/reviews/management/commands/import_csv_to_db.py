from django.core.management.base import BaseCommand

from reviews import utils


class Command(BaseCommand):
    help = 'Импортирует в базу данных объекты моделей из csv.'

    def handle(self, *args, **options):
        utils.users_to_db(self)
        utils.genres_to_db(self)
        utils.categories_to_db(self)
        utils.titles_to_db(self)
        utils.genres_titles_to_db(self)
        utils.reviews_to_db(self)
        utils.comments_to_db(self)
