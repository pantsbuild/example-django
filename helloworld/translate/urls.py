# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.urls import path

from helloworld.translate import views

urlpatterns = [
    path("<str:slug>/<str:lang>/", views.index, name="index"),
]
