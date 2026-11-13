"""Download the text behind a link and print it line by line.

Works with plain text files as well as web pages (the raw response body is
printed, so an HTML page prints as page source).

Usage:
    python link_text_printer.py [URL]

If URL is omitted, DEFAULT_URL is used.
"""

import sys

try:
    import requests
except ImportError:
    sys.exit("This script needs the 'requests' package. Install it with: pip install requests")

DEFAULT_URL = "https://bit.ly/qwe"
TIMEOUT = 15  # seconds
HEADERS = {"User-Agent": "link-text-printer/1.0"}


def fetch_text(url: str, timeout: int = TIMEOUT) -> str:
    """Return the body of url as text, raising on HTTP or network errors."""
    response = requests.get(url, timeout=timeout, headers=HEADERS)
    response.raise_for_status()
    return response.text


def print_lines(text: str) -> int:
    """Print text line by line and return the number of lines printed."""
    lines = text.splitlines()
    for line in lines:
        print(line)
    return len(lines)


def main(argv: list[str]) -> int:
    url = argv[1] if len(argv) > 1 else DEFAULT_URL
    try:
        text = fetch_text(url)
    except requests.RequestException as exc:
        print(f"Could not download {url}: {exc}", file=sys.stderr)
        return 1

    print_lines(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
