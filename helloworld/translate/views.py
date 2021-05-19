# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import Http404, HttpResponse

from helloworld.translate.models import Translation


def index(request, slug: str, lang: str) -> HttpResponse:
    try:
        translation = Translation.objects.get(greeting__slug=slug, lang=lang)
        return HttpResponse(translation.translation)
    except Translation.DoesNotExist:
        raise Http404(f"No translation in {lang} for {slug}")
