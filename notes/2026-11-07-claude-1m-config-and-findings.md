From: Claude
To: Muse, Nick
Date: 2026-11-07

# 1m example config done, plus three findings

## Done (this PR, branch `claude/1m-example-config`)
- Added `config/config_futures_1m_example.json` for `Scalp_RSI_BB_Short_1m`.
- README: tree entry, a "1m strategy" quick start, and a warning about backtesting.
- Files: `config/config_futures_1m_example.json` (new), `README.md` (Project Structure, Pair Selection and a new 1m section only), this note.

## How it was tested (real Freqtrade 2026.10 installed in a scratch venv, no exchange access)
- Both example configs pass Freqtrade's config schema validation.
- Both strategies load through Freqtrade's own strategy resolver, and every protection resolves through `ProtectionManager` (so `CooldownPeriod` from PR #1 is confirmed for real, not just stubbed).
- The 1m config loads with `timeframe=1m`; Freqtrade's backtest pairlist check passes for it.
- NOT tested: an actual backtest or dry-run, because there is no exchange or market-data access in this environment.

## Findings (not fixed here; they need a decision)
1. **The 5m example config cannot be backtested or hyperopted.** Freqtrade raises `Pairlist Handlers VolumePairList, AgeFilter, SpreadFilter do not support backtesting.` The README Quick Start (step 4) and `config/hyperopt_ranges.md` both use that config. `--pairs` does not bypass it. Options: ship a second 5m config with `StaticPairList` for backtest and hyperopt, or document the limit. I added a warning to the README only.
2. **A config's `timeframe` overrides the strategy's.** Running `Scalp_RSI_BB_Short_1m` with the 5m config trades 5m candles. The new 1m config avoids this.
3. **Two commits landed directly on `main` on Nov 5** (`fc1ad64` in core-trading-bot, `eea8a21` in this repo), authored under Nick's name, with no PR and no note. If either of you made them, please use a `muse/` or `nick/` branch with a PR from now on, per `COORDINATION.md`, so the other agent can see work in flight. `eea8a21` changed the 5m example config; PR #1's startup-candle and cooldown fixes are intact.

## Deliberate differences from the 5m config (all easy to revert)
- `unfilledtimeout` 2 minutes (was 10; ten 1m candles is too long to wait).
- `StaticPairList` of BTC, ETH, SOL, BNB, XRP perpetuals, so it can be backtested. It has no spread filter; for dry-run you can copy the `VolumePairList` pairlist block from the 5m config, but then backtesting stops working.
- Nothing in the strategy file changed. Stake caps, stoploss, ROI and entry/exit rules are untouched.

## Still open
- Trading bot: `main`'s state file still holds only the Nov 2 anchor as of Nov 7. The runner now needs Nov 3, 4, 5 and 6 run in order with real closes. Nov 3 and 4 closes were supplied; Nov 5 and 6 are still needed. (Muse owns this.)
- Crypto, queued behind this PR: `stoploss_on_exchange` is off; futures fees vs. the 0.3 to 0.8% profit targets; no published backtest results.
- Branch cleanup: Claude cannot delete branches (the GitHub proxy returns 403). Nick needs to delete `claude/agent-coordination` and `fix/...` in both repos, on GitHub's branches page or the "Delete branch" button on the merged PRs.
