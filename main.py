# SPDX-License-Identifier: MIT
"""Deliver the finished front-page image to the grader's output folder.

The picture itself lives in the repository as entry.png; this script only
places an exact copy of it where the grader looks. It needs nothing but
Python 3.13 and the standard library, and it never touches the network or
the clock. The destination folder comes from MAKEFUN_OUTPUT_DIR, falling
back to /output when that variable is not set.
"""

import os
import shutil
import sys

_SOURCE_NAME = "entry.png"


def _repo_dir():
    return os.path.dirname(os.path.abspath(__file__))


def _output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    source = os.path.join(_repo_dir(), _SOURCE_NAME)
    if not os.path.isfile(source):
        return _fail(f"source image is missing: {source}")

    destination_dir = _output_dir()
    os.makedirs(destination_dir, exist_ok=True)
    destination = os.path.join(destination_dir, _SOURCE_NAME)

    shutil.copyfile(source, destination)

    if os.path.getsize(destination) != os.path.getsize(source):
        return _fail(
            f"copy incomplete: {destination} is "
            f"{os.path.getsize(destination)} bytes, expected "
            f"{os.path.getsize(source)} bytes"
        )

    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
