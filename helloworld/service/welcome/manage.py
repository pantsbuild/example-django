# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.service import Service

if __name__ == "__main__":
    Service(__file__).run_manage()
