# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models

from helloworld.greet.models import Greeting


class TranslationManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("greeting")


class Translation(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["greeting", "lang"], name="greeting_lang")
        ]

    objects = TranslationManager()

    # NB: This Translation model share a database with the Greeting model, so this
    #  relation is allowed by our database router.
    greeting = models.ForeignKey(Greeting, on_delete=models.CASCADE)
    lang = models.CharField(max_length=2)
    translation = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.greeting} in {self.lang}"
