from django.db import models


class PublishStateOptions(models.TextChoices):
        # CONSTANT = DB_VALUE, USER_DISPLAY_VAL
        PUBLISH = 'PU', 'Published'
        DRAFT = 'DR', 'Draft'