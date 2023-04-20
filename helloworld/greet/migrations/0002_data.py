# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

from datetime import time

from django.db import migrations


def create_greetings(apps, schema_editor):
    Greeting = apps.get_model("greet", "Greeting")

    def create(
        slug: str, salutation: str, start_time: str | None, end_time: str | None
    ) -> None:
        Greeting(
            slug=slug,
            salutation=salutation,
            start_time=time.fromisoformat(start_time) if start_time else None,
            end_time=time.fromisoformat(end_time) if end_time else None,
        ).save()

    create("hello", "Hello", None, None)
    create("howareyou", "How are you", None, None)
    create("goodmorning", "Good morning", "05:00:00", "11:59:59")
    create("goodevening", "Good evening", "17:00:00", "20:59:59")
    create("goodnight", "Good night", "21:00:00", "23:59:59")


class Migration(migrations.Migration):
    dependencies = [
        ("greet", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_greetings),
    ]
