#!/usr/bin/env bash
# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

PYTHON_BIN=python3.7

python_abi() {
  "${PYTHON_BIN}" <<EOF
import distutils.sysconfig
import distutils.util
import platform
import sys

impl = platform.python_implementation()  # EG: 'CPython'
ver = ''.join(platform.python_version_tuple()[:2])  # EG: '37'
malloc = 'm' if impl == 'CPython' and distutils.sysconfig.get_config_var('WITH_PYMALLOC') == 1 else ''
ucs = 'u' if sys.maxunicode > 2**16 else ''
plat = distutils.util.get_platform()  # EG: macosx-10.7-x86_64

print(f'{impl}{ver}{malloc}{ucs}-{plat}')
EOF
}

requirements_fingerprint() {
  ls *.txt | sort | xargs cat | git hash-object -t blob --stdin
}

# Setup the Python virtual environment in the directory passed as $1.
setup_venv() {
  local venv_dir="$1"
  local venv_fingerprint_file="$2"
  "${PYTHON_BIN}" -m venv "${venv_dir}" >&2
  local PIP="${venv_dir}/bin/pip"
  "${PIP}" install --upgrade "pip>=21.1"
  "${PIP}" install -r requirements.txt -c constraints.txt >&2
  touch "${venv_dir}/${venv_fingerprint_file}"
}

VENV_DIR=".venvs/$(uname -s)/${PYTHON_BIN}"
mkdir -p "$(dirname "${VENV_DIR}")"
REQUIREMENTS_FINGERPRINT="$(requirements_fingerprint)"
FINGERPRINT_BASE_NAME=".fingerprint-$(python_abi)-${REQUIREMENTS_FINGERPRINT}"
VENV_FINGERPRINT_FILE="${VENV_DIR}/${FINGERPRINT_BASE_NAME}"

if [ ! -e "${VENV_FINGERPRINT_FILE}" ]; then
  setup_venv "${VENV_DIR}" "${FINGERPRINT_BASE_NAME}"
fi

echo ${VENV_DIR}
