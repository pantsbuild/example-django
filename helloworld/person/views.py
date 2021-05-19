# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import Http404, HttpResponse

from helloworld.person.models import Person


def index(request, slug):
    try:
        person_to_greet = Person.objects.get(slug=slug)
        return HttpResponse(person_to_greet.full_name)
    except Person.DoesNotExist:
        raise Http404(f"No such person: {slug}")
