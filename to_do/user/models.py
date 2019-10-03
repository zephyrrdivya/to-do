from django.contrib.auth.models import User, UserManager


class User(User):
    objects = UserManager()

    class Meta:
        proxy = True
        ordering = ('id', )
