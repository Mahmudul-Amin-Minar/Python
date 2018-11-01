import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "av.settings")
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from blog.models import Post


def create_post(N):
    fake = Faker()

    for _ in range(N):
        id = User.objects.first()
        title = fake.name()
        status = 'published'
        Post.objects.create(title=title + 'post.!!',
                            author=id,
                            slug='-'.join(title.lower().split()),
                            body=fake.text(),
                            created=timezone.now(),
                            updated=timezone.now(),
                            )


create_post(10)
print("Posted successfully")
