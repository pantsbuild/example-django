# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
from tempfile import mkdtemp
from typing import List

from django.conf import settings


def configure_settings(apps: List[str]) -> None:
    """Minimal settings for unittests."""
    settings.configure(
        TIME_ZONE="UTC",
        USE_TZ=True,
        INSTALLED_APPS=apps,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(mkdtemp(), "test.sqlite3"),
            }
        },
    )
