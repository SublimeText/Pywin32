import sublime
import sys
from os.path import join

assert(sys.platform.startswith('win'))


def win32setup():
    if sublime.platform() == "windows":
        try:
            import win32api
        except:
            arch = sublime.arch()
            sys.path.append(join(sublime.packages_path(), "Pywin32", "lib", arch, "win32"))
            sys.path.append(join(sublime.packages_path(), "Pywin32", "lib", arch, "win32", "lib"))
