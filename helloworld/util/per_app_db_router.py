# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations


class PerAppDBRouter:
    """A class for routing model queries for an entire app to a specific db.

    This makes it easy to enforce a partitioning of apps across multiple
    databases.
    """

    def __init__(self, app_to_db: dict[str, str]) -> None:
        self._app_to_db: dict[str, str] = dict(app_to_db)

    def db_for_read(self, model, **hints) -> str | None:
        return self._app_to_db.get(model._meta.app_label)

    def db_for_write(self, model, **hints) -> str | None:
        return self._app_to_db.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints) -> bool | None:
        # Only allow intra-db relations.
        return None

    def allow_migrate(
        self, db: str, app_label: str, model_name=None, **hints
    ) -> bool | None:
        return self._app_to_db.get(app_label) == db
