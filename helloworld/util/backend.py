# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.mode import Mode, get_mode


def get_backend_url(name: str) -> str:
    if get_mode() == Mode.DEV:
        from django.conf import settings

        return f"http://localhost:{settings.DEV_PORTS[name]}"
    else:
        raise ValueError(f"Mode {get_mode()} not supported yet.")
