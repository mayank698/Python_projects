#!/usr/bin/env python
import os
import subprocess
import sys
import traceback

def main():
    """Run migrations and start the Django development server."""
    print("Django Password Manager")
    print("======================")
    print("\nFeatures:")
    print("- User authentication (register, login, logout)")
    print("- Store website credentials (website, username, password)")
    print("- One password per website (duplicate prevention)")
    print("- Password generator for secure passwords")
    print("- Search functionality to quickly find passwords")
    
    # Check Django installation
    print("\n[0/4] Checking Django installation...")
    try:
        import django
        print(f"Django {django.get_version()} is installed.")
    except ImportError:
        print("Error: Django is not installed. Please run: pip install -r requirements.txt")
        return
    
    # Make migrations
    print("\n[1/4] Making migrations...")
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "makemigrations", "vault"], 
            check=False,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error: Failed to make migrations.\n{result.stderr}")
            return
        print(result.stdout)
    except Exception as e:
        print(f"Exception during makemigrations: {str(e)}")
        traceback.print_exc()
        return
    
    # Apply migrations
    print("\n[2/4] Applying migrations...")
    try:
        result = subprocess.run(
            [sys.executable, "manage.py", "migrate"], 
            check=False,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error: Failed to apply migrations.\n{result.stderr}")
            return
        print(result.stdout)
    except Exception as e:
        print(f"Exception during migrate: {str(e)}")
        traceback.print_exc()
        return
    
    # Check if superuser exists
    print("\n[3/4] Checking for superuser...")
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(is_superuser=True).exists():
            print("No superuser found. Creating one now...")
            from django.db import DEFAULT_DB_ALIAS
            from django.contrib.auth.management.commands.createsuperuser import Command
            Command().handle(
                interactive=True,
                database=DEFAULT_DB_ALIAS,
                username=None,
                email=None,
                verbosity=1
            )
    except Exception as e:
        print(f"Warning: Could not check for superuser. {str(e)}")
        traceback.print_exc()
    
    # Start the development server
    print("\n[4/4] Starting development server...")
    print("Access the password manager at: http://127.0.0.1:8000/")
    print("Admin interface available at: http://127.0.0.1:8000/admin/")
    print("Press Ctrl+C to stop the server.\n")
    try:
        result = subprocess.run([sys.executable, "manage.py", "runserver"], check=False)
        if result.returncode != 0:
            print(f"Error: Failed to start development server. Return code: {result.returncode}")
            return
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Exception during runserver: {str(e)}")
        traceback.print_exc()
        return

if __name__ == "__main__":
    # Set up Django environment
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "passwordmanager.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            print("Django is not installed. Please install it with: pip install -r requirements.txt")
            sys.exit(1)
        else:
            print(f"Django {django.get_version()} is installed, but there was an error importing django.core.management.")
            print("This might be due to an incorrect Django installation or incompatible Python version.")
            sys.exit(1)
    
    main() 