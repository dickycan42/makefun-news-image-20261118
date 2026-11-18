[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/dickycan42/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/dickycan42/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World Today — Wednesday 18 November 2026

An entry for the make.fun competition **"Sum up 18 November's world news
in one image"** (`news-image-20261118`). The image is a newspaper front page
that sums up the biggest world news of Wednesday 18 November 2026, drawn from
scratch with Python's standard image library and checked against live news
reports from the day.

## The news in the picture

- **Lead story — APEC opens in Shenzhen.** The APEC summit opens in
  Shenzhen, China (18–19 Nov). Quad leaders meet in Manila first, and a
  first-ever Trump–Xi–Putin summit is set for the next day, 19 November.
- **Gulf on edge — Iran drones hit a US radar in Bahrain.** Iran's
  Revolutionary Guards launch drones at the US-operated radar at Sheikh Isa
  Air Base; Bahrain's air defences intercept them. Kuwait reports drone
  attacks too; Bahrain sounds a threat alert, then gives the all-clear.
- **War in Ukraine — Kerch Bridge hit for a second day.** Ukrainian drones
  strike the bridge to Crimea again and a road span falls into the strait,
  while Russia pounds bridges across Kyiv.
- **Storm watch — Cyclone Akvan.** The storm strengthens over the Bay of
  Bengal and heads for Andhra Pradesh, India, with landfall expected around
  20 November; Andhra Pradesh and Odisha are on high alert.
- **Business — Nvidia doubles sales.** Nvidia reports $115.84 billion in
  quarterly revenue, up 103% year on year, in its first results since Jensen
  Huang's exit; the board says it does not intend to bring him back.
- **Sport — Dhoni retires.** MS Dhoni ends his IPL playing career and
  becomes mentor of Chennai Super Kings.
- **Trade — Canada–China deal.** Xi meets Carney before APEC as Canada and
  China extend trade cooperation.
- **Sanctions — UK & Australia act.** London and Canberra sanction Israeli
  settlement firms in the West Bank.

## How the image is built

The front page is laid out like a newspaper: a masthead naming the date
("Wednesday 18 November 2026"), a large lead panel for the APEC story, two
rows of illustrated story panels for the Gulf, Ukraine, cyclone and Nvidia
stories, and a bottom strip of three short items (Dhoni, Canada–China,
UK–Australia sanctions). Every story has its own illustration and a headline
large enough to read at full size, so the picture can be understood on its
own, with no news feed.

The finished picture is stored in the repository as `entry.png`
(1024 × 1024 pixels, under 1 MiB). `main.py` simply copies that file,
byte for byte, to the grader's output location — it uses no network, reads
no clock, and reads no file outside this repository, so two runs always
produce identical bytes.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

With no `MAKEFUN_OUTPUT_DIR` set, the program writes to `/output/entry.png`,
as the competition rules describe. Requires Python 3.13 (standard library
only).

## License

MIT — see `LICENSE`.
