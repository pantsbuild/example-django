# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_sources(
    name="lib",
    dependencies=[
        "helloworld/ui",
    ],
    overrides={
        "manage.py": {
            "dependencies": ["helloworld/service/frontend/settings.py:lib"],
            "restartable": True,
        },
        "gunicorn.py": {"restartable": True},
    },
)

pex_binary(
    name="gunicorn",
    entry_point="gunicorn.py",
    dependencies=[
        ":lib",
    ],
)

pex_binary(
    name="manage",
    entry_point="manage.py",
    dependencies=[
        ":lib",
    ],
)
