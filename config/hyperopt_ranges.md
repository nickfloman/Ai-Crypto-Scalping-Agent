# Hyperopt Recommended Ranges

Use these ranges when running hyperopt on the scalping strategies.

## Scalp_RSI_BB_Short (5m)

```bash
freqtrade hyperopt \
  --strategy Scalp_RSI_BB_Short \
  --hyperopt-loss SharpeHyperOptLoss \
  --spaces buy sell \
  --timerange 20250901-20251101 \
  -i 5m \
  -e 300
```

### Parameter ranges (already defined in strategy)

| Parameter       | Space | Range       | Default |
|-----------------|-------|-------------|---------|
| buy_rsi         | buy   | 22 – 35     | 28      |
| sell_rsi        | sell  | 65 – 80     | 72      |
| short_rsi       | sell  | 65 – 80     | 72      |
| cover_rsi       | buy   | 22 – 35     | 28      |
| bb_period       | buy   | 16 – 24     | 20      |
| bb_std          | buy   | 1.8 – 2.4   | 2.0     |
| volume_factor   | buy   | 0.6 – 1.2   | 0.75    |

## Scalp_RSI_BB_Short_1m (1m)

```bash
freqtrade hyperopt \
  --strategy Scalp_RSI_BB_Short_1m \
  --hyperopt-loss SharpeHyperOptLoss \
  --spaces buy sell \
  --timerange 20251001-20251101 \
  -i 1m \
  -e 300
```

### Parameter ranges

| Parameter       | Space | Range       | Default |
|-----------------|-------|-------------|---------|
| buy_rsi         | buy   | 18 – 32     | 25      |
| sell_rsi        | sell  | 68 – 82     | 75      |
| short_rsi       | sell  | 68 – 82     | 75      |
| cover_rsi       | buy   | 18 – 32     | 25      |
| bb_period       | buy   | 12 – 20     | 14      |
| bb_std          | buy   | 1.6 – 2.2   | 1.9     |
| volume_factor   | buy   | 0.5 – 1.1   | 0.7     |

## Notes

- Always include realistic fees in backtesting/hyperopt.
- Prefer `SharpeHyperOptLoss` or `OnlyProfitHyperOptLoss` for scalping.
- After hyperopt, re-validate on a different out-of-sample period.
- Never hyperopt and go live on the same data window.
