Pywin32
=======

Pywin32 support for sublime (win32api etc)

Still evaluating what needs to be included and what doesn't, so if it is missing something important, please let me know.

# Using Pywin32
Pywin32 modules should be accessible as soon as Sublime loads up the Pywin32 plugin...but since there is no guarunteed way to ensure all plugins are loaded after Pywin32 gets loaded, you should include `Pywin32.setup` before including any pywin32 modules.  You can include it once in the top most level file, and all subsequent includes from that file should be guarunteed access.  It does not have to be included in all files that call pywin32 modules, just once in the top level file that is the entry point.  If I could guaruntee pywin32 to get loaded before all plugins, then even this requriement would not be necessary.

Example (show url path of all open explorer windows):

```python
import Pywin32.setup
from win32com.client.gencache import EnsureDispatch


def run():
    for w in EnsureDispatch("Shell.Application").Windows():
        print(w.LocationName + "=" + w.LocationURL)

run()
```
