from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL3dpc2UtbWFlc3Ryby9OYW5kYVBlZGlhUHlybw==").decode("utf-8"),
)
