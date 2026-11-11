"""Test backend defining the mandatory hooks and get_requires_for_build_wheel.

Don't use this for any real code.
"""
from buildsys_minimal import build_sdist, build_wheel  # noqa: F401


def get_requires_for_build_wheel(config_settings):
    return ["wheelwright"]
