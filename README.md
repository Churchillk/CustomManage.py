# Django Project with Background Requirements Installation

This project demonstrates how to start a Django server while simultaneously installing dependencies from `requirements.txt` using a background thread. This setup ensures that the server is operational even as packages are installed.

## Features

- **Concurrent Installation**: Runs dependency installation in a background thread.
- **Automated Setup**: Automatically installs packages from `requirements.txt` if it exists.
- **Robust Initialization**: Ensures the Django server starts regardless of the installation process.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- `pip` for package management

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    Ensure `requirements.txt` is present in the root directory of your project and install `python-dotenv`:

    ```bash
    pip install python-dotenv
    ```

4. **Run the Django Server**

    Use the following script to start the Django server and concurrently install dependencies if `requirements.txt` is found:

    ```python
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
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cococola.settings')
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
    ```

5. **Verify the Setup**

    Ensure that the Django server is running and dependencies are being installed. Look for output that indicates the progress of the requirements installation.

## Usage

- **Start the Server**: Use the following command to start the Django server. This will also handle the installation of requirements in the background.

    ```bash
    python manage.py runserver
    ```

- **Stop the Server**: Use `Ctrl+C` in your terminal to stop the server when needed.

## Contributing

Contributions are welcome! Please submit pull requests or open issues for any enhancements or bug fixes. Make sure your contributions adhere to the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django**: A high-level Python web framework that promotes rapid development and clean, pragmatic design.
