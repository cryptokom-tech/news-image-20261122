# The World in One Day — news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cryptokom-tech/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/cryptokom-tech/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up Sunday 22 November 2026 — the whole day, all in
a single newspaper front page. Built for the make.fun bounty
**news-image-20261122**, *"Sum up 22 November's world news in one image"*.

## The final full-day edition

This is the final edition of the entry. It covers the **entire** day of
Sunday 22 November 2026 in **36 stories**, researched from Reuters, BBC,
ATP Tour, ESPNcricinfo and other outlets, and verified to have happened
on that day. Every story is numbered, and every story with a location
carries a numbered pin on the dotted world map at the top of the page.

## The day's biggest stories

- **COP31 collapses with no deal** — the EU rejects the Antalya Pact
  over its fossil-fuel omission, ending the longest climate summit ever,
  two days into overtime.
- **Alcaraz wins his maiden ATP Finals** — beats world No. 1 Zverev
  6-2, 7-6(7) in Turin, finishing 5-0 for the week with a record
  $5.171M prize.
- **India post 720/9, a record total in New Zealand** — Rahul 136 and
  Pant 128 in Wellington, the first time ever the first seven
  partnerships all passed 50.
- **Democrats win their biggest House majority since 1992** — at least
  258 seats after flipping a North Carolina seat.
- **Liverpool thrash 10-man Manchester United 4-0**, and Verstappen
  takes a dramatic Las Vegas Grand Prix.

The front page also carries a markets strip in the footer: the Sensex
ending its two-day rally, crude oil futures down over 3%, Bitcoin
holding above $60,000, and COP31 ending with no deal.

## What is in this repo

| File | What it is |
| --- | --- |
| `entry.png` | The front page itself: 1024x1024 PNG, under 1 MiB |
| `main.py` | The submission entry point (standard library only) |
| `LICENSE` | MIT licence |

## How the image is put together

The page is drawn as a classic newspaper front page: a bold masthead
("THE WORLD IN ONE DAY"), a red date banner ("SUNDAY 22 NOVEMBER
2026"), a dotted world map built from a small built-in land mask, 32
numbered location pins placed by latitude/longitude and spread apart
so none overlap, then the 36 stories in three columns of twelve —
headline in bold with a one-to-two-line summary — and the markets
strip along the bottom. Stories that share a city — Washington DC,
Delhi, Shanghai, Mumbai — get their pins fanned out around the same
spot instead of stacking on top of each other.

## How main.py works

`main.py` is a thin, dependency-free entry program:

1. It reads the bundled `entry.png` sitting next to it.
2. It validates the file: PNG signature, size under 1 MiB, a real
   1024x1024 IHDR, and a chunk walk that ends cleanly with an IEND
   chunk carrying the correct CRC.
3. It copies the bytes to `entry.png` inside the output directory
   (`$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`), then reads
   the copy back and refuses to finish unless it matches the bundle
   exactly.

Run it twice and the output is byte-identical both times. It makes no
network calls.

```sh
python3 main.py
```

## Checking the entry yourself

- Open `entry.png` and confirm it is 1024x1024 and opens as a normal
  PNG image.
- Count the stories: 36, numbered 1–36 across three columns.
- Count the pins on the map: 32 numbered red pins (four stories have
  no location to pin). No two pins overlap.
- Compare two runs of `main.py`: the SHA-256 printed each time is the
  same, and the file it writes matches the bundled image byte for byte.

## Licence

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?ref=08bvq6fy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
