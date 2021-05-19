# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from datetime import time

import pytest

from helloworld.greet.models import Greeting


@pytest.mark.django_db
def test_database_is_seeded():
    hello = Greeting.objects.get(slug="hello")
    assert "Hello" == hello.salutation


@pytest.mark.django_db
def test_for_time_of_day():
    assert (
        "goodmorning" == Greeting.for_time_of_day(time.fromisoformat("09:30:57")).slug
    )
    assert (
        "goodevening" == Greeting.for_time_of_day(time.fromisoformat("18:03:09")).slug
    )
    assert "goodnight" == Greeting.for_time_of_day(time.fromisoformat("23:47:45")).slug
    assert Greeting.for_time_of_day(time.fromisoformat("03:03:03")) is None
