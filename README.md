# The World in One Day — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/cryptokom-tech/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/cryptokom-tech/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One picture of Sunday 22 November 2026, drawn as a newspaper front
page. The red banner names the day; below it a dotted world map
carries a numbered pin for every story; below that, 36 numbered
stories in three columns, each a headline plus a short summary, so
anyone who missed the day can tell what happened from the image
alone.

## What happened that day

This is the round 1 morning edition, put together from the morning
wires of 22 November 2026 (Reuters, BBC, Jagran Josh, Newsmriti,
NationPress and others). Only events that happened, or were first
reported, on 22 November 2026 are in it. The front of the paper:

- IG Metall calls a 24-hour strike for Monday — 23,000 workers at
  19 firms in northern Germany, including Mercedes and Meyer Werft
- COP31 deadlocked into Sunday as the fossil-fuel fight continues
- France and the US draft a UN resolution for the post-UNIFIL
  vacuum in Lebanon
- US–China military talks end in Shanghai; the EU proposes budget
  cuts and a tax on digital platforms
- Modi opens the Nitish Setu bridge in Bihar; the ATP Finals
  semifinals are set in Turin
- India and New Zealand open their Test series in Wellington, and
  Australia end England's seven-match T20 winning run

## Files

- `entry.png` — the finished front page, 1024x1024, under 1 MiB
- `main.py` — the entry program (Python 3, standard library only)

## How the program works

`main.py` reads the bundled `entry.png`, checks that it is a real
PNG of 1024x1024 pixels under the 1 MiB limit with its IEND chunk
intact, copies it to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`), then reads the copy back and
refuses to finish unless the bytes match the bundle exactly. It
touches no network, and two runs write identical bytes.

Run it with:

```sh
python3 main.py
```

## Bounty

Built for the make.fun bounty `news-image-20261122` — "Sum up
22 November's world news in one image". MIT licensed.

---

<sub>Entered on [make.fun](https://make.fun/?ref=08bvq6fy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
