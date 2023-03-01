# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys
from pathlib import PurePath

from helloworld.util.discovery import get_dev_port


class Service:
    def __init__(self, name_or_file: str):
        if os.path.sep in name_or_file:
            # This is the __file__ of the caller, so compute the service name.
            rparts = list(reversed(PurePath(name_or_file).parts))
            self._name = ".".join(reversed(rparts[1 : rparts.index("helloworld") + 1]))
        else:
            self._name = name_or_file

    def run_gunicorn(self):
        # If no args were provided, fill them in for convenience.
        if len(sys.argv) == 1:
            sys.argv.extend(
                ["--config", "python:helloworld.gunicorn_conf", "helloworld.wsgi"]
            )
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._name}.settings")
        from gunicorn.app.wsgiapp import run

        sys.exit(run())

    def run_manage(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._name}.settings")
        args = sys.argv
        if len(sys.argv) == 2 and sys.argv[1] == "runserver":
            # We rely on Pants's reloading, so turn off Django's (which doesn't interact
            # well with Pex: Pex's re-exec logic causes Django's re-exec to misdetect its
            # entry point, see https://code.djangoproject.com/ticket/32314).
            # TODO: Some way to detect that we're in a `pants run`, and only set --noreload
            #  in that case, so that users can run manage.py directly if they want to.
            args += ["--noreload"]
            # If no port was provided, use the dev port for this service.
            dev_port = get_dev_port(self._name)
            args += [f"{dev_port}"]
        from django.core.management import execute_from_command_line

        execute_from_command_line(args)
