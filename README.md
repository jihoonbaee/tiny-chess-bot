# tiny-chess-bot

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/jihoonbaee/tiny-chess-bot/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/jihoonbaee/tiny-chess-bot/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4,062-byte chess engine in plain Python for the make.fun
`tiny-chess-01` bounty — written line by line, no compression, no
packed payload. 0x88 board, MTD(f) search with iterative deepening,
a transposition table, null-move pruning skipped at the root,
quiescence search, killer moves (512 slots) and a king piece-square
table. It plays every game through the make.fun env and searches
to a fixed node budget, never a clock, so a replay produces the
same moves.

## The size rule

- `main.py` is the whole engine: at most 4,096 bytes as committed,
  Python 3.13, standard library only. It reads, imports or execs no
  other file in the repository.
- The rest of the tree (this README, LICENSE) is at most 8,192 bytes
  in all, and no file over 4,096.

## Grade it locally

You need Docker and the `makefun` CLI. Download the competition's dev
kit, unpack it, and from inside it run:

    makefun grade-local --kit . --bot <your repository> --driver docker

It plays one practice trial against the house engines, replays it, and
prints the Elo the scorer gives it. Before you submit, `makefun check`
runs the site's own pre-submit checks, size caps included.

## Local practice

Version 12 scored a mean Elo of 1250.7 across three local practice
trials (24 games) against the house engines — above the 1154 practice
floor, below the 1325 baseline. Perft 20/20.
