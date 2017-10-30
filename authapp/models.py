from django.db import models
from django.contrib.auth import models as auth_models, get_user_model


class CustomUser(auth_models.AbstractUser):
    pass