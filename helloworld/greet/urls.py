# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.urls import path, re_path

from helloworld.greet import views

urlpatterns = [
    re_path(
        r"^tod/(?P<time_of_day>\d\d:\d\d:\d\d)/$", views.for_time_of_day, name="tod"
    ),
    path("<str:slug>/", views.index, name="index"),
]
