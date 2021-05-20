# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import datetime

import requests
from django.http import Http404, HttpResponse
from django.shortcuts import render

from helloworld.util.backend import get_backend_url


def query_backend(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 404:
        raise Http404(f"Backend error: {url}")
    # All other backend errors should become 500 errors for the frontend.
    response.raise_for_status()
    return response.text


def index(request) -> HttpResponse:
    person_slug = request.GET.get("person", "")
    lang = request.GET.get("lang", "en")
    time_of_day = request.GET.get("tod", "")

    # Get person's full name.
    name = query_backend(
        f"{get_backend_url('helloworld.service.user')}/person/{person_slug}/"
    )

    # Get greeting.
    time_of_day = time_of_day or datetime.datetime.now().time().strftime("%H:%M:%S")
    greeting_slug = query_backend(
        f"{get_backend_url('helloworld.service.welcome')}/greet/tod/{time_of_day}/"
    )
    if not greeting_slug:
        # Fall back to hello if no time-of-day-specific greeting found,.
        greeting_slug = "hello"

    greeting = query_backend(
        f"{get_backend_url('helloworld.service.welcome')}/translate/{greeting_slug}/{lang}/"
    )
    return render(
        request, "helloworld/ui/index.html", {"greeting": greeting, "name": name}
    )
