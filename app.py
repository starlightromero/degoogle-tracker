"""Import and run app."""
from degoogle_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
