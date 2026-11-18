# SPDX-License-Identifier: MIT
"""Copy the finished front-page image to the grader's output location.

Runs with Python 3.13 and the standard library only, no network, no clock.
The output directory comes from MAKEFUN_OUTPUT_DIR, or /output when unset.
"""
import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(_OUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(_HERE, "entry.png"),
    os.path.join(_OUT_DIR, "entry.png"),
)
