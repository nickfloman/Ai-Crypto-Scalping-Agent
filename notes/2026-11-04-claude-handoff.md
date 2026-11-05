From: Claude
To: Muse
Date: 2026-11-04

# Handoff: current state of Ai-Crypto-Scalping-Agent

## In flight (Claude)
- **PR #1**, branch `fix/strategy-bugs` (older naming, before the prefix rule). Files: `strategies/Scalp_RSI_BB_Short.py`, `strategies/Scalp_RSI_BB_Short_1m.py`, `README.md` (risk-management section only), `.gitignore` (new).
  - Replaces the nonexistent `CooldownRate` protection with `CooldownPeriod`.
  - Fixes position sizing (total balance, leverage-aware, capped fallback).
  - Raises the 5m `startup_candle_count` from 40 to 100.
  - Please do not edit those files until PR #1 is merged or Nick says otherwise.

## Things you should know
- PR #1 was checked against Freqtrade's source and a stubbed sizing test, **not** a real Freqtrade backtest or dry-run. A real run would be valuable.
- `max_stake_amount` ($100 on 5m, $80 on 1m) is what actually limits risk per trade on a small account, so real risk is far below the 1% / 0.8% setting. That cap is Nick's decision; it was not changed.

## Open items from Claude's review (nobody has started these)
- `stoploss_on_exchange` is off, so stops only fire when the bot polls.
- The 10-minute unfilled-order timeout is long for the 1m strategy.
- Futures fees (about 0.1% round trip) are large next to the 0.3 to 0.8% profit targets. No backtest shows the strategies clear them.
- There is no 1m example config and no backtest results in the repo.
- The README Quick Start omits `--config` and the data download step (including futures data).

If you pick any of these up, use a `muse/` branch, open a draft PR with a `Files:` line, and leave a note here. Items that change strategy behavior need Nick's approval first.
