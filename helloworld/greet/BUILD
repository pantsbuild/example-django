# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "helloworld/greet/migrations",
    ]
)

python_tests(name = 'tests',
    dependencies = [
        "helloworld",  # For settings.py.
    ]
)
