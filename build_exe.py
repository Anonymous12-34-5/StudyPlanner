import os
import subprocess
import sys

def build():
    print("Starting build process...")
    
    # Ensure icons directory exists
    if not os.path.exists('icons'):
        os.makedirs('icons')
        print("Created icons directory.")

    # Main build command
    command = [
        "py", "-m", "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name=CBSE_Study_Planner",
        "main.py"
    ]
    
    # Add icon if it exists
    if os.path.exists("icons/app_icon.ico"):
        command.append("--icon=icons/app_icon.ico")
        print("Using custom icon.")
    else:
        print("No icon found, building with default...")

    # Run PyInstaller
    try:
        subprocess.check_call(command)
        print("\nBuild Successful!")
        print(f"Executable is located in: {os.path.join(os.getcwd(), 'dist')}")
    except subprocess.CalledProcessError as e:
        print(f"\nBuild failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build()
