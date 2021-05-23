# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.contrib import admin

from helloworld.translate.models import Translation

admin.site.register(Translation)
