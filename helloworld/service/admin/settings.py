# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *  # noqa: F403

ROOT_URLCONF = "helloworld.service.admin.urls"

MIDDLEWARE += [  # noqa: F405
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "helloworld.greet",
    "helloworld.person",
    "helloworld.translate",
]

set_up_database("users")  # noqa: F405
set_up_database("greetings")  # noqa: F405

# The admin UI expects to auth against the "default" db, so we alias it here.
DATABASES["default"] = DATABASES["users"]  # noqa: F405

STATIC_URL = "static/"
