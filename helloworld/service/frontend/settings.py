# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *  # noqa: F401, F403

ROOT_URLCONF = "helloworld.service.frontend.urls"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.staticfiles",
    "helloworld.ui",
]

STATIC_URL = "/static/"
STATIC_ROOT = "/tmp/static_root"
