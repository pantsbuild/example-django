# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_sources(
    dependencies=[
        "helloworld/person/migrations",
    ]
)

python_tests(
    name="tests",
    dependencies=[
        "helloworld",  # For settings.py.
    ],
)

python_test_utils(
    name="test_utils",
)
