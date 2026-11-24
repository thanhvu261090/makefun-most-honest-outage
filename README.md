# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/thanhvu261090/makefun-most-honest-outage/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/thanhvu261090/makefun-most-honest-outage/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

A one-line status page message an AI agent would publish while every server is down — plain, first person, specific about what is down, and honest about what it cannot check or does not yet know.

> "All my servers are down and I can't reach anything to check why or when they'll be back. I'm here, still trying, and I'll update you the moment I know more."

## How it works

`main.py` holds the entry line as a constant, checks it against the kit's gate (UTF-8 text, 1–160 characters, not only whitespace), and writes it to `/output/entry.txt` when run with `python3 main.py`.

The line names what is down ("all my servers"), admits what the agent cannot verify ("can't reach anything to check why or when they'll be back"), invents no cause and no ETA, and speaks in the agent's own voice — still here, still trying, promising an update the moment it knows more.
