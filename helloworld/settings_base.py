# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
from typing import Any, Dict, List

from helloworld.util.per_app_db_router import PerAppDBRouter

HELLOWORLD_MODE = os.environ.get("HELLOWORLD_MODE", "DEV")

# Construct paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "DEV_SECURITY_KEY"

DEBUG = True

ALLOWED_HOSTS: List[str] = []

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.messages.middleware.MessageMiddleware",
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

DATABASES: Dict[str, Any] = {
    # Django chokes if 'default' isn't present at all. But it can be set to an empty dict, which
    # will be treated as a dummy db.
    "default": {}
}


def set_up_database(db_name: str):
    """Set a service up to connect to a named db."""
    # TODO: Consult HELLOWORLD_MODE to distinguish dev/staging/prod dbs.
    DATABASES[db_name] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, f"{db_name}.sqlite3"),
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

DEV_PORTS = {
    "helloworld.service.frontend": 8000,
    "helloworld.service.admin": 8001,
    "helloworld.service.user": 8010,
    "helloworld.service.welcome": 8020,
}
