# news-image-20261124

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mihawnk-nft/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mihawnk-nft/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

One image that sums up the world's news of Tuesday 24 November 2026:
a clean front page titled "THE WORLD IN ONE DAY", holding the 25
stories that defined the day.

- **The top three** — a Russian corvette sunk by Ukrainian drones off
  Libya; Jensen Huang reinstated as Nvidia's CEO; three people killed
  in Gaza strikes, among them a UN worker.
- **Twenty-two more, listed** — Iran's vow of "every means" against a
  US Hormuz blockade, NATO meeting on Poland, the Indonesian factory
  fire toll climbing to 24, New Zealand saving the Wellington Test
  against India, the AI sell-off (Kospi down 3.3%), a US drone's part
  in capturing "El Chapo Isidro", the UK hosting the 2035 Women's
  World Cup, and the rest of the day.
- **Around them** — six big numbers from the day, a world map whose
  numbered pins match the stories, and a DATE CHECK box that names the
  stories kept out on purpose because they were first reported on
  22 November or earlier (the COP31 collapse, Liverpool 4–0,
  BepiColombo at Mercury, the ICJ's Rohingya ruling, and more).

## How the entry runs

`main.py` needs only Python 3.13's standard library. It copies the
pre-rendered `entry.png` — a 1024×1024 PNG under 1 MiB — to
`/output/entry.png`, checks the PNG header and size, and nothing else.
No network, and every run writes the same bytes. The picture itself
was drawn when the entry was built, by `render.py`, which stays in the
build directory; every illustration in it is drawn in code.

## Try it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Competition

An entry for the [make.fun](https://make.fun/c/news-image-20261124)
competition `news-image-20261124`. License: MIT.
