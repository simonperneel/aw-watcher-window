# Slightly modified to disable window title, except for some websites (facebook, youtube, whatsapp,...), where
# the website is mapped to their broad category (social media, video, chat,...) and the title is not shown.
# Adaptations are commented with "Custom added"

import sys
from typing import Optional

# own module
from .util import alter_window_info
from .exceptions import FatalError

def get_current_window_linux() -> Optional[dict]:
    from . import xlib

    window = xlib.get_current_window()

    if window is None:
        cls = "unknown"
        name = "unknown"
    else:
        cls = xlib.get_window_class(window)
        name = xlib.get_window_name(window)

    return {"app": cls, "title": name}


def get_current_window_macos(strategy: str) -> Optional[dict]:

    # jxa is the default & preferred strategy. It includes the url + incognito status
    if strategy == "jxa":
        from . import macos_jxa

        active_window = macos_jxa.getInfo()
        # Custom added
        altered_window = alter_window_info(active_window)
        return altered_window
    elif strategy == "applescript":
        from . import macos_applescript
        # Custom added
        active_window = macos_applescript.getInfo()
        altered_window = alter_window_info(active_window)
        return altered_window
    else:
        raise FatalError(f"invalid strategy '{strategy}'")


def get_current_window_windows() -> Optional[dict]:
    from . import windows

    window_handle = windows.get_active_window_handle()
    try:
        app = windows.get_app_name(window_handle)
    except Exception:  # TODO: narrow down the exception
        # try with wmi method
        app = windows.get_app_name_wmi(window_handle)

    title = windows.get_window_title(window_handle)

    if app is None:
        app = "unknown"
    if title is None:
        title = "unknown"

    active_window = {"app": app, "title": title}
    # Custom added
    altered_window = alter_window_info(active_window)

    return {"app": altered_window.get("app"), "title": altered_window.get("title")}


def get_current_window(strategy: Optional[str] = None) -> Optional[dict]:
    """
    :raises FatalError: if a fatal error occurs (e.g. unsupported platform, X server closed)
    """

    if sys.platform.startswith("linux"):
        return get_current_window_linux()
    elif sys.platform == "darwin":
        if strategy is None:
            raise FatalError("macOS strategy not specified")
        return get_current_window_macos(strategy)
    elif sys.platform in ["win32", "cygwin"]:
        return get_current_window_windows()
    else:
        raise FatalError(f"Unknown platform: {sys.platform}")
