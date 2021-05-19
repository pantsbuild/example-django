# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models


class Person(models.Model):
    slug = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
