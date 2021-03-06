#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # settings = "demo.app.settings" # Uncomment to test demo.app
    settings = "yt_playlist.settings"  # Uncomment to test demo.app
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
