# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
