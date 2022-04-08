# --- External Imports ---
import habanero

# --- STL Imports ---
import difflib


class Article:
    def __init__(self, DOI: str):
        pass

    @staticmethod
    def findByName(name: str, minSimilarity: float=0.9) -> "Article":
        nameLower = name.lower()

        # Query the crossref database and sort the hits in descending order
        # of their titles' similarity to the input name.
        client = habanero.Crossref()
        hits = sorted(
            [(item, difflib.SequenceMatcher(None, item["title"][0].lower(), nameLower).ratio()) for item in client.works(query = name)["message"]["items"]],
            key = lambda item: 1.0-item[1]
        )

        # Check whether there's a hit that satisfies all criteria
        hit = None
        if hits:
            if minSimilarity <= hits[0][1]:
                hit = hits[0][0]

        return hit
