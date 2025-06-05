from utilities import fetch_publications, add_missing_publications
import sys


def main(path="publications/"):
    # Replace accordingly
    scholar_url = "https://scholar.google.com/citations?user=bMwZVkAAAAAJ&hl=en"
    # Author name (for proper highlighting) Replace accordingly
    author_name = "Colton Botta"

    # Read publication from Google Scholar
    publications = fetch_publications(scholar_url, verbose = True)

    add_missing_publications(publications, path, author_name, verbose = True)

if __name__ == "__main__":
    """Allow the path to be passed as an argument when the script is executed directly"""
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path ="publications/"
    main(path)