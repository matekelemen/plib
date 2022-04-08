# --- STL Imports ---
import pathlib
import re


def convertToFileName(fileName: str) -> pathlib.Path:
    """Convert the input string into a valid file name with a uniform style."""
    regex = re.compile(r"([a-zA-Z0-9\.\-\_ ]+)")
    output = "_".join(regex.findall(fileName))

    if not output:
        raise ValueError("No valid file name can be constructed from '{fileName}'")

    return pathlib.Path(output)
