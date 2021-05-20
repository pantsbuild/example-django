# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.person.models import Person


@pytest.mark.django_db
def test_database_is_seeded():
    sherlock = Person.objects.get(slug="sherlock")
    assert "Sherlock Holmes" == sherlock.full_name
