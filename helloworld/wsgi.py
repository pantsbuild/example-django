# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os

from django.core.wsgi import get_wsgi_application

if "DJANGO_SETTINGS_MODULE" not in os.environ:
    raise ValueError("DJANGO_SETTINGS_MODULE must be set before creating a WSGI app.")

application = get_wsgi_application()
