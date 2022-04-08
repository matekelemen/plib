# --- External Imports ---
import pdfrw

# --- STL Imports ---
import pathlib


def getPDFTitle(filePath: pathlib.Path) -> str:
    return pdfrw.PdfReader(filePath).Info.Title.strip("()")


