import pytest

from app.core import greet


def test_greet_returns_greeting_for_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")
