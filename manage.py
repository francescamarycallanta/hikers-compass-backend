#!/usr/bin/env python
# This line tells the computer to run this file with the Python interpreter

import os  # Used to interact with the system's environment (like setting variables)
import sys  # Access command-line arguments (like `runserver`, `migrate`, etc.) !!

# This block only runs if this file is run directly
if __name__ == "__main__":
    """
    This is the main entry point for Django's command-line utility.

    Why is it important???
    - It lets you control the Django backend by running commands like:
        - `runserver` to start the API server
        - `migrate` to create/update database tables
        - `createsuperuser` to add an admin login
    - It's a bridge between your terminal and the Django framework.
    - Without this file, you'd have no way to interact with the backend system from the command line.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appBackend.settings")
    
    try:
        # Try to import Django's command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django isn't installed, prints an error
        raise ImportError(
            "Couldn't import Django. It's nottt installed and on your PYTHONPATH?"
        ) from exc

    # Pass command-line arguments to Django (like runserver, migrate, etc.) !!
    execute_from_command_line(sys.argv)
