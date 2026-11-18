# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/davidwara/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/davidwara/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-image front page summing up Tuesday 17 November 2026: six stories — the Kerch Bridge strike, tankers mined near Hormuz, Trump in Manila, the JPMorgan outage, NVIDIA earnings and the Vulcan rocket failure — drawn by a Python script with PIL.

## Run it

```sh
python3 draw_image.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`draw_image.py` draws the 1024x1024 front page into `entry.png`; `main.py` copies it to the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`). No network, fully deterministic: two runs write identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=z5073zsc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
