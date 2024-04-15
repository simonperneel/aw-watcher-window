aw-watcher-window
=================

Cross-platform window-Watcher for Linux (X11), macOS, Windows.
[SLIGHTLY MODIFIED VERSION] to disable window tracking by default.

## Modified version

To disable window tracking by default, changes have been made in the `aw-watcher-window` code. The changes are located in [./aw_watcher_window/](./aw_watcher_window/)

More specifically:
 - [lib.py](./aw_watcher_window/lib.py) has been modified to disable window tracking by default.
- [util.py](./aw_watcher_window/util.py) has been added to provide these functions. These functions provide the mapping from certain sites to their category
- [macos.swift](aw_watcher_window/macos.swift) has been modified to do the mapping from certain sites to their category for *macOS users*

## How to install

To install the pre-built application, go to https://activitywatch.net/downloads/

To build your own packaged application, run `make package`

To install the latest git version directly from github without cloning, run
`pip install git+https://github.com/ActivityWatch/aw-watcher-window.git`

To install from a cloned version, cd into the directory and run
`poetry install` to install inside an virtualenv. You can run the binary via `aw-watcher-window`.

If you want to install it system-wide it can be installed with `pip install .`, but that has the issue
that it might not get the exact version of the dependencies due to not reading the poetry.lock file.

## Usage

In order for this watcher to be available in the UI, you'll need to have a Away From Computer (afk) watcher running alongside it.

### Note to macOS users

To log current window title the terminal needs access to macOS accessibility API.
This can be enabled in `System Preferences > Security & Privacy > Accessibility`, then add the Terminal to this list. If this is not enabled the watcher can only log current application, and not window title.

