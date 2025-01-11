import subprocess


def start_command():
    """Run the development server."""
    try:
        subprocess.run(
            [
                "uvicorn",
                "app._main:app",
                "--host",
                "0.0.0.0",
                "--port",
                "8000",
                "--reload",
            ]
        )
    except KeyboardInterrupt:
        print("\nServer stopped.")
