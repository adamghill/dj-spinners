import pytest
from django.utils.safestring import SafeString

from dj_spinners.templatetags.dj_spinners import _load_svg, spinner


def test():
    result = spinner("3-dots-bounce")

    assert isinstance(result, SafeString)
    assert "<svg" in result
    assert "</svg" in result

    expected = '<svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><style>.spinner_qM83{animation:spinner_8HQG 1.05s infinite}.spinner_oXPr{animation-delay:.1s}.spinner_ZTLf{animation-delay:.2s}@keyframes spinner_8HQG{0%,57.14%{animation-timing-function:cubic-bezier(0.33,.66,.66,1);transform:translate(0)}28.57%{animation-timing-function:cubic-bezier(0.33,0,.66,.33);transform:translateY(-6px)}100%{transform:translate(0)}}</style><circle class="spinner_qM83" cx="4" cy="12" r="3"/><circle class="spinner_qM83 spinner_oXPr" cx="12" cy="12" r="3"/><circle class="spinner_qM83 spinner_ZTLf" cx="20" cy="12" r="3"/></svg>'  # noqa: E501
    assert expected == result


def test_extension():
    without_ext = spinner("3-dots-bounce")
    with_ext = spinner("3-dots-bounce.svg")

    assert without_ext == with_ext


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        spinner("definitely-not-a-real-spinner-name-xyz")


def test_cache():
    # Clear the cache
    _load_svg.cache_clear()
    info_before = _load_svg.cache_info()

    assert info_before.misses == 0
    assert info_before.hits == 0

    _ = _load_svg("3-dots-bounce")
    info_after_first = _load_svg.cache_info()

    # Second call with same key should be a cache hit
    _ = _load_svg("3-dots-bounce")
    info_after_second = _load_svg.cache_info()

    # One miss for the first load, then one hit for the second load
    assert info_after_first.misses - info_before.misses == 1
    assert info_after_second.hits - info_after_first.hits == 1
