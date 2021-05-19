# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models

from helloworld.greet.models import Greeting


class Translation(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["greeting", "lang"], name="greeting_lang")
        ]

    greeting = models.ForeignKey(Greeting, on_delete=models.CASCADE)
    lang = models.CharField(max_length=2)
    translation = models.CharField(max_length=20)
