import sys
from os.path import join, dirname
import struct

assert(sys.platform.startswith('win'))

ARCH = "x%d" % (8 * struct.calcsize("P"))
PACKAGE_PATH = dirname(__file__)
LIB_PATHS = [
    (join(PACKAGE_PATH, "lib", ARCH, "win32"), "win32"),
    (join(PACKAGE_PATH, "lib", ARCH, "win32", "lib"), "win32/lib"),
    (join(PACKAGE_PATH, "lib", ARCH), "win32com"),
    (join(PACKAGE_PATH, "lib", ARCH, "win32comext"), "win32comext")
]

for lib in LIB_PATHS:
    if lib[0] not in sys.path:
        sys.path.append(lib[0])
        print("Pywin32: Added '%s'" % lib[1])
