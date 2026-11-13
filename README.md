# link-text-printer

Download the text behind a link and print it line by line to the console.

## Requirements

- Python 3.9+
- [`requests`](https://pypi.org/project/requests/)

```bash
pip install requests
```

## Usage

Run with the built-in default URL:

```bash
python link_text_printer.py
```

Or pass the link you want to print:

```bash
python link_text_printer.py https://example.com/notes.txt
```

The script prints every line of the downloaded document to standard output.
Errors (DNS failure, timeout, HTTP 4xx/5xx) are written to standard error and
the exit code is `1`.

## How it works

1. `fetch_text()` requests the URL with a 15-second timeout and a custom
   `User-Agent`, then raises on any HTTP error status.
2. `print_lines()` splits the body on line breaks and prints each line.
3. `main()` picks the URL from the command line or falls back to
   `DEFAULT_URL`.

## Notes

- The default link (`https://bit.ly/qwe`) currently resolves to an old
  backtype.com page that only returns a "lander" redirect, so the default run
  prints one line of HTML. Pass your own URL to print real content.
- The script prints the raw response body. If the URL points at an HTML page
  you will see the page source, not extracted article text.
- Update `DEFAULT_URL` in the script if you want a different default link.
