# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.greet.models import Greeting
from helloworld.translate.models import (  # noqa: F401 (so fk related name works).
    Translation,
)


@pytest.mark.django_db
def test_database_is_seeded():
    hello = Greeting.objects.get(slug="hello")
    translations = {tr.lang: tr.translation for tr in hello.translation_set.all()}
    assert {
        "en": "Hello",
        "es": "Hola",
        "fr": "Allo",
        "de": "Hallo",
    } == translations
