# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *  # noqa: F401, F403

ROOT_URLCONF = "helloworld.service.welcome.urls"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "helloworld.greet",
    "helloworld.translate",
]

set_up_database("greetings")  # noqa: F405
