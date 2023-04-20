# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import migrations


def create_greetings(apps, schema_editor):
    Greeting = apps.get_model("greet", "Greeting")
    Translation = apps.get_model("translate", "Translation")

    def create(slug: str, lang: str, translation: str) -> None:
        greeting = Greeting.objects.get(slug=slug)
        Translation(greeting=greeting, lang=lang, translation=translation).save()

    create("hello", "en", "Hello")
    create("goodmorning", "en", "Good morning")
    create("goodevening", "en", "Good evening")
    create("goodnight", "en", "Good night")

    create("hello", "es", "Hola")
    create("goodmorning", "es", "Buenos días")
    create("goodevening", "es", "Buenas tardes")
    create("goodnight", "es", "Buenas noches")

    create("hello", "fr", "Allo")
    create("goodmorning", "fr", "Bonjour")
    create("goodevening", "fr", "Bonsoir")
    create("goodnight", "fr", "Bonne nuit")

    create("hello", "de", "Hallo")
    create("goodmorning", "de", "Guten Morgen")
    create("goodevening", "de", "Guten Abend")
    create("goodnight", "de", "Gute Nacht")


class Migration(migrations.Migration):
    dependencies = [
        ("translate", "0001_initial"),
        ("greet", "0002_data"),
    ]

    operations = [
        migrations.RunPython(create_greetings),
    ]
