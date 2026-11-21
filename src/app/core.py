"""Example module so the template has something real to test. Delete when you add your own code."""


def greet(name: str) -> str:
    """Return a greeting for a non-empty name."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
