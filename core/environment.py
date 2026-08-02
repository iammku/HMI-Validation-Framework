import os
def get_environment():
    """Return the active framework environment
    Defaults to 'dev' if FRAMEWORK_ENV not set."""
    return os.getenv("FRAMEWORK_ENV", "dev").strip().lower()
