# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    name="lib",
    dependencies = [
        "helloworld/greet",
        "helloworld/translate",
    ]
)

pex_binary(
    name = 'gunicorn',
    entry_point = 'gunicorn.py',
    dependencies = [
        ':lib',
    ],
)
