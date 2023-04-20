# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# Generated by Django 3.0 on 2020-06-17 22:09

from django.db import migrations


def create_people_to_greet(apps, schema_editor):
    Person = apps.get_model("person", "Person")

    def create(slug, full_name):
        Person(slug=slug, full_name=full_name).save()

    create("sherlock", "Sherlock Holmes")
    create("watson", "John Watson")
    create("lestrade", "Inspector G. Lestrade")
    create("hudson", "Mrs. Hudson")
    create("adler", "Irene Adler")
    create("moriarty", "James Moriarty")


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_people_to_greet),
    ]
