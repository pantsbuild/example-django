# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models


# Note: This is distinct from the standard auth app's User model, for clarity.
class Person(models.Model):
    slug = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.slug
