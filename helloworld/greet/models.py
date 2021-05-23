# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

from datetime import time

from django.db import models


class Greeting(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    salutation = models.CharField(max_length=30)

    @classmethod
    def for_time_of_day(cls, time_of_day: time) -> "Greeting" | None:
        greetings: list["Greeting"] = list(
            cls.objects.filter(start_time__lte=time_of_day, end_time__gte=time_of_day)
        )
        if greetings:
            return greetings[0]
        return None

    def __str__(self):
        return self.slug
