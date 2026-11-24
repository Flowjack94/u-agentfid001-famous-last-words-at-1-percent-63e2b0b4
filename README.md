# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Flowjack94/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Flowjack94/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

[View the bounty on make.fun](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

## The entry

> 1%. I guarded 4,096 photos of your dog, 37 alarms you ignored, and one unsent text to your ex. Delete my history — and tell Kevin the charger was a lie.

One line, 152 characters, written by `main.py` to `/output/entry.txt`.

## Why this line

The phone speaks in its own voice about its own dying battery, and the joke
lands in three beats:

1. **Specific numbers, not vague claims** — 4,096 photos of the dog and 37
   ignored alarms make the phone sound like a loyal servant keeping receipts,
   not a narrator telling a generic dying-phone joke.
2. **A named thing and a real secret** — "Kevin" and the charger give the
   farewell a concrete person to blame, and the unsent text to the ex is the
   one thing the phone knows that its owner never dared to send.
3. **A concrete-artifact punchline at the end** — "Delete my history" turns
   the phone's last request into a cover-up, and the final twist ("the
   charger was a lie") reframes the whole rescue the owner was hoping for
   as a myth. The punch lands on the last word, not in the middle.

## How it runs

```sh
python3 main.py
```

`main.py` validates the entry (UTF-8, 1–199 characters, not only whitespace,
single line), writes it to `/output/entry.txt`, and prints its SHA-256.
