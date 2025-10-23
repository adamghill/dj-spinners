from functools import lru_cache
from importlib import resources

from django import template
from django.utils.safestring import SafeString, mark_safe

register = template.Library()


@lru_cache(maxsize=256)
def _load_svg(name: str) -> str:
    """Loads the svg HTML from a name for the file."""

    filename = name

    if not filename.endswith(".svg"):
        filename = f"{name}.svg"

    try:
        base = resources.files("dj_spinners") / "assets" / "svg" / filename

        if base.is_file():
            return base.read_text(encoding="utf-8")
    except Exception:  # noqa: S110
        pass

    raise FileNotFoundError(f"Spinner '{filename}' not found.")


@register.simple_tag
def spinner(name: str) -> SafeString:
    """Render an inline SVG spinner by name.

    Usage:
        `{% spinner "3-dots-bounce" %}`
    """

    svg = _load_svg(name)

    return mark_safe(svg)  # noqa: S308
