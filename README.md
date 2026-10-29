# scripting

Small, single-purpose Python tools written from scratch while learning offensive and defensive security.

These are learning tools, not a framework. Each script does one thing, reads its arguments from the command line, and leans on the Python standard library alone — except the web scripts, which use `requests` and `beautifulsoup4`. Comments and output are in French.

They were built along a structured Python-for-security track, one block at a time: bytes and files, encoding and HMAC, process execution, sockets, HTTP, and concurrency.

## Requirements

- Python 3.10+
- For the web scripts only: `pip install -r requirements.txt`

## Foundations — bytes & files

| Script | What it does | Usage |
|---|---|---|
| `recon.py` | Echoes a target; with a second argument, shows its hex encoding and the difference between byte length and character length. | `python recon.py <target> [text]` |
| `pack.py` | Packs a 32-bit unsigned integer in big- and little-endian, prints the hex. Endianness in practice. | `python pack.py <integer>` |
| `hashit.py` | SHA-256 of a file, read as raw bytes. | `python hashit.py <file>` |
| `b64.py` | Base64-encodes a file and decodes it back — a reminder that encoding is not encryption. | `python b64.py <file>` |
| `compress.py` | zlib compress/decompress round-trip, printing both sizes. | `python compress.py <file>` |
| `gitblob.py` | Computes a file's Git blob SHA-1 — the same object id as `git hash-object`. | `python gitblob.py <file>` |

## Encoding & crypto

| Script | What it does | Usage |
|---|---|---|
| `urlenc.py` | Percent-encodes text (`quote`, `safe=''`), the way a value goes into a URL. | `python urlenc.py "<text>"` |
| `hmacsign.py` | Produces an HMAC-SHA256 tag from a shared key and a message. | `python hmacsign.py <key> <message>` |
| `hmacverify.py` | Verifies a tag in constant time with `compare_digest`. | `python hmacverify.py <key> <message> <tag_hex>` |

## Process execution

| Script | What it does | Usage |
|---|---|---|
| `runcmd.py` | Pings a host once through `subprocess` (`shell=False`, argument list), then parses the latency with a regex. | `python runcmd.py <host>` |

## Network — sockets

| Script | What it does | Usage |
|---|---|---|
| `banner.py` | Opens a TCP connection, optionally sends a request, and reads back the response. Banner grabbing. | `python banner.py <ip> <port> [request]` |
| `scan.py` | TCP connect scan over ports 20–100 (`connect_ex`). | `python scan.py <ip>` |
| `serveur.py` | A minimal TCP listener on `127.0.0.1:4444` that prints one received message — the receiving side of `nc -lvnp`. | `python serveur.py` |

## HTTP & web

| Script | What it does | Usage |
|---|---|---|
| `httpget.py` | GET request; prints the status code, the `Server` and `Content-Type` headers, and the first 300 characters of the body. | `python httpget.py <url>` |
| `extract.py` | Fetches a page and lists its title and every link (BeautifulSoup). | `python extract.py <url>` |
| `extract_forms.py` | Fetches a page and enumerates its forms — action, method, and each input. | `python extract_forms.py <url>` |
| `fuzz.py` | Tries a small wordlist of paths against a base URL and reports the status of each. | `python fuzz.py <base_url>` |

## Concurrency

The sequential scripts spend almost all their time waiting on the network. These versions run that waiting in parallel with a thread pool (`concurrent.futures.ThreadPoolExecutor`), turning minutes into seconds. Each worker is kept isolated so a single failed request cannot abort the whole run.

| Script | What it does | Usage |
|---|---|---|
| `scan_pool.py` | Concurrent port scan over ports 20–100 — the same check as `scan.py`, run across a thread pool. | `python scan_pool.py <ip>` |
| `fuzz_pool.py` | Concurrent version of `fuzz.py`; each worker returns a named result and handles its own network error. | `python fuzz_pool.py <base_url>` |

## A note on use

These scripts are for learning and for authorized testing only — lab machines, targets you own, or engagements you have written permission for.

## License

MIT — see [LICENSE](LICENSE).
