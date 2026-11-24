# news-image-20261124

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mihawnk-nft/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mihawnk-nft/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

Sum up 24 November's world news in one image — a clean newspaper front
page, "THE WORLD IN ONE DAY", for Tuesday 24 November 2026, with the 25
stories that defined the day:

- **3 big stories** — Ukraine sinks a Russian corvette off Libya; Nvidia
  brings back Jensen Huang as CEO; three killed in Gaza strikes, incl. a
  UN worker
- **22 more in the list** — Iran vows "every means" vs a US Hormuz
  blockade, NATO's council on Poland, the Indonesia factory fire toll
  rising to 24, New Zealand batting out a draw vs India in Wellington,
  the AI sell-off (Kospi −3.3%), a US drone helping capture "El Chapo
  Isidro", the UK as 2035 Women's World Cup host, and more
- **Plus** — a KPI strip of the day's big numbers, a numbered world map,
  and a DATE CHECK box naming the 22 November and earlier stories left
  out on purpose (COP31 collapse, Liverpool 4–0, BepiColombo, the ICJ
  Rohingya ruling, and more)

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024 PNG, under 1 MiB) to `/output/entry.png`. It runs
with no network and writes identical bytes on every run. The image was
drawn at build time by `render.py` (kept in the build directory).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

Built for the [make.fun](https://make.fun/c/news-image-20261124)
competition `news-image-20261124`. License: MIT.
