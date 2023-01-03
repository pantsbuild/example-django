# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *  # noqa: F401, F403

ROOT_URLCONF = "helloworld.service.frontend.urls"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "helloworld.ui",
]

MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = "static/"
STATIC_ROOT = "/tmp/static_root"
