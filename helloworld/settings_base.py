# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import os
from typing import Any

from helloworld.util.per_app_db_router import PerAppDBRouter

HELLOWORLD_MODE = os.environ.get("HELLOWORLD_MODE", "DEV")

SECRET_KEY = "DEV_SECURITY_KEY"

DEBUG = True

ALLOWED_HOSTS: list[str] = []

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

DATABASES: dict[str, Any] = {
    # Django chokes if 'default' isn't present at all. But it can be set to an empty dict, which
    # will be treated as a dummy db.
    "default": {}
}


def set_up_database(db_name: str):
    """Set a service up to connect to a named db."""
    # TODO: Consult HELLOWORLD_MODE to distinguish dev/staging/prod dbs.
    DATABASES[db_name] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": f"{db_name}.sqlite3",
    }


DATABASE_ROUTERS = [
    PerAppDBRouter(
        {
            "contenttypes": "users",
            "sessions": "users",
            "auth": "users",
            "admin": "users",
            "person": "users",
            "greet": "greetings",
            "translate": "greetings",
        }
    )
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = "helloworld.wsgi.application"
