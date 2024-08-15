#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading

def install_requirements():
    """Install requirements from requirements.txt in a separate thread."""
    if os.path.isfile('requirements.txt'):
        print("Installing requirements...")
        os.system('pip install -r requirements.txt')
        print("Requirements installed.")
    else:
        print("No requirements.txt file found.")

def main():
    """Run administrative tasks."""
    # Start the installation of requirements in a separate thread
    install_thread = threading.Thread(target=install_requirements)
    install_thread.start()

    # Run the Django management command
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # Optionally, wait for the installation thread to finish
    # install_thread.join()  # Uncomment this if you want to wait for installation to complete

if __name__ == '__main__':
    main()
