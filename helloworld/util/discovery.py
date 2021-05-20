# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


DEV_PORTS = {
    "helloworld.service.frontend": 8000,
    "helloworld.service.admin": 8001,
    "helloworld.service.user": 8010,
    "helloworld.service.welcome": 8020,
}


def get_dev_port(service: str) -> int:
    try:
        return DEV_PORTS[service]
    except KeyError:
        raise ValueError(f"No dev port found for service {service}")
