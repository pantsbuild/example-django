# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.discovery import get_dev_port
from helloworld.util.mode import Mode, get_mode


def get_backend_url(name: str) -> str:
    if get_mode() == Mode.DEV:
        return f"http://localhost:{get_dev_port(name)}"
    else:
        raise ValueError(f"Mode {get_mode()} not supported yet.")
