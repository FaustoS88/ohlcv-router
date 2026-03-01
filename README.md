# ohlcv-hub

Async Python library for fetching OHLCV (candlestick) market data from multiple free providers. Automatically routes symbols to the best available data source.

```
BTCUSDT  →  Binance  →  yfinance (fallback)
AAPL     →  yfinance
WM.TO    →  yfinance  (exchange-suffix support)
EURUSD   →  yfinance  (forex)
```

## Features

- **Multi-provider** — Binance, yfinance, Tiingo, Finnhub (more coming)
- **Auto-routing** — asset class detection picks the right provider chain automatically
- **Async** — built on `asyncio` / `aiohttp`, no blocking calls
- **Typed** — `Candle` dataclass with slots, fully annotated
- **Intervals** — `1m`, `5m`, `15m`, `1h`, `4h`, `1d`, `1w`

## Installation

```bash
pip install ohlcv-hub
```

Or from source:

```bash
git clone https://github.com/FaustoS88/ohlcv-hub.git
cd ohlcv-hub
pip install -e ".[dev]"
```

## Quick Start

```python
import asyncio
from ohlcv_hub import fetch

async def main():
    # Crypto — routes to Binance automatically
    candles = await fetch("BTCUSDT", interval="1d", limit=30)
    for c in candles[-3:]:
        print(f"{c.time}  O:{c.open:.2f}  H:{c.high:.2f}  L:{c.low:.2f}  C:{c.close:.2f}")

asyncio.run(main())
```

## Supported Intervals

| Interval | Description |
|----------|-------------|
| `1m`     | 1 minute    |
| `5m`     | 5 minutes   |
| `15m`    | 15 minutes  |
| `1h`     | 1 hour      |
| `4h`     | 4 hours     |
| `1d`     | Daily       |
| `1w`     | Weekly      |

## Provider Routing

| Asset class | Pattern example  | Provider chain                              |
|-------------|------------------|---------------------------------------------|
| Crypto      | `BTCUSDT`        | Binance → yfinance                          |
| US stocks   | `AAPL`, `^GSPC`  | yfinance → Tiingo (daily/weekly) → Finnhub  |
| Intl stocks | `WM.TO`, `RIO.L` | yfinance → Finnhub                          |
| Forex       | `EURUSD`         | yfinance → Finnhub                          |

Tiingo requires `TIINGO_API_KEY`. Finnhub requires `FINNHUB_API_KEY`. Both fall back gracefully when the key is absent.

## Roadmap

- [x] Tiingo provider (daily/weekly, stocks and ETFs)
- [x] Finnhub provider (stock candles + forex via Oanda feed)
- [ ] Session reuse in BinanceProvider
- [ ] CLI tool: `ohlcv fetch BTCUSDT 1d 100`
- [ ] Response caching (TTL-based)
- [ ] pip release

## License

MIT
