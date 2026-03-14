# ohlcv-router

[![CI](https://github.com/FaustoS88/ohlcv-router/actions/workflows/ci.yml/badge.svg)](https://github.com/FaustoS88/ohlcv-router/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Async Python library for fetching OHLCV (candlestick) market data from multiple free providers. Automatically routes symbols to the best available data source and falls back gracefully when a provider fails.

```
BTCUSDT  →  Binance  →  CoinGecko  →  Kraken  →  KuCoin  →  yfinance
AAPL     →  yfinance  →  Tiingo (daily/weekly)  →  Finnhub
WM.TO    →  yfinance  →  Finnhub
EURUSD   →  yfinance  →  Finnhub
```

## Features

- **Multi-provider** — Binance, CoinGecko, Kraken, KuCoin, yfinance, Tiingo, Finnhub with automatic fallback
- **Auto-routing** — asset class detection picks the right provider chain per symbol
- **Async** — built on `asyncio` / `aiohttp`, no blocking calls
- **Typed** — full type annotations, `py.typed` marker included
- **CLI** — `ohlcv fetch BTCUSDT 1d 30` out of the box
- **Intervals** — `1m`, `5m`, `15m`, `1h`, `4h`, `1d`, `1w`
- **Resilient** — structured logging on every provider attempt and failure

## Installation

```bash
pip install ohlcv-router
```

Or from source:

```bash
git clone https://github.com/FaustoS88/ohlcv-router.git
cd ohlcv-router
pip install -e ".[dev,cli]"
```

## Quick Start

```python
import asyncio
from ohlcv_hub import fetch

async def main():
    # Crypto — routes to Binance automatically
    candles = await fetch("BTCUSDT", interval="1d", limit=10)
    for c in candles[-3:]:
        print(f"{c.time}  O:{c.open:.2f}  H:{c.high:.2f}  L:{c.low:.2f}  C:{c.close:.2f}")

asyncio.run(main())
```

## CLI

```bash
# Basic fetch (auto-routes to best provider)
ohlcv fetch BTCUSDT

# Custom interval and limit
ohlcv fetch AAPL 1d 30

# Force a specific provider
ohlcv fetch EURUSD 1d 20 --provider yfinance

# Output as CSV
ohlcv fetch BTCUSDT 1d 10 --csv
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
| Crypto      | `BTCUSDT`        | Binance → CoinGecko → Kraken → KuCoin → yfinance |
| US stocks   | `AAPL`, `^GSPC`  | yfinance → Tiingo (daily/weekly) → Finnhub  |
| Intl stocks | `WM.TO`, `RIO.L` | yfinance → Finnhub                          |
| Forex       | `EURUSD`         | yfinance → Finnhub                          |

Tiingo requires `TIINGO_API_KEY`. Finnhub requires `FINNHUB_API_KEY` and a **paid plan** — the free tier does not include historical candles. Both fall back gracefully when the key is absent or the plan lacks access.

CoinGecko requires no API key. It supports `4h` and `1d` intervals only (granularity is automatic). Volume is not available from the OHLC endpoint and is always `0`.

Kraken requires no API key. Public REST API for all listed crypto pairs. Supports all standard intervals from `1m` to `1w`. Returns up to 720 bars per request.

KuCoin requires no API key. Public REST API supporting all standard intervals from `1m` to `1w`. Returns up to 1500 bars per request. Uses `BASE-QUOTE` symbol format internally (e.g. `BTC-USDT`).

## Examples

See [`examples/`](examples/) for runnable scripts:

- [`basic_fetch.py`](examples/basic_fetch.py) — fetch candles for crypto, stock, and forex
- [`multi_provider.py`](examples/multi_provider.py) — inspect provider chains and observe fallback behaviour

## Roadmap

- [x] Tiingo provider (daily/weekly, stocks and ETFs)
- [x] Finnhub provider (stock candles + forex via Oanda feed)
- [x] Session reuse in BinanceProvider
- [x] CLI tool: `ohlcv fetch BTCUSDT 1d 100`
- [x] KuCoin provider (crypto, no key, 1500 bars, all intervals)
- [ ] Response caching (TTL-based)
- [ ] pip release

## License

MIT
