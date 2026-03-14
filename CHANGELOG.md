# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

## [0.1.2] — 2026-03-14

### Added
- In-memory TTL cache in `ohlcv_router.cache` — interval-aware expiry (30s for `1m` up to 24h for `1w`)
- Cache integrated into `registry.fetch()` — hit avoids all provider calls, miss populates on success
- `OHLCV_CACHE_ENABLED=false` env var to disable cache process-wide
- `cache.clear()` and `cache.size()` for testing and CLI tooling
- 26 cache tests covering TTL expiry, eviction, env toggle, and registry integration
- README Caching section with TTL table and usage examples

## [0.1.1] — 2026-03-14

### Changed
- README roadmap: replace GitHub-flavored checkboxes with plain text (renders correctly on PyPI)
- Roadmap updated to reflect current state — all v0.1.0 items complete, new planned items added

---

## [0.1.0] — 2026-03-14

### Added
- `KuCoinProvider` — public REST API, no key, `BASE-QUOTE` symbol normalisation, all intervals, 1500 bars
- `KrakenProvider` — public REST API for crypto OHLCV, no key required; BTC→XBT symbol mapping; all standard intervals
- `CoinGeckoProvider` — crypto OHLCV with no API key; 4h and 1d granularity via auto-detection
- GitHub Actions release workflow — publishes to PyPI on `v*` tag push

### Fixed
- Logging added to registry fallback chain — silent `None` returns now emit `debug`/`warning` diagnostics

---

## [0.0.5] — 2026-03-03

### Added
- CLI tool: `ohlcv fetch SYMBOL INTERVAL LIMIT [--provider] [--csv]` via click
- `examples/basic_fetch.py` and `examples/multi_provider.py`
- GitHub Actions CI — pytest + ruff on Python 3.11 and 3.12

### Fixed
- Session reuse in `BinanceProvider` — single `aiohttp.ClientSession` per instance
- Close session on CLI exit via `registry.teardown()`
- Move `click` to core dependencies (was optional, broke CLI install)

---

## [0.0.4] — 2026-02-25

### Added
- `FinnhubProvider` — US stock candles and forex quotes via OANDA format
- `TiingoProvider` — daily and weekly bars for stocks and ETFs; requires `TIINGO_API_KEY`
- Tiingo and Finnhub wired into `registry.pick()` routing chains

### Fixed
- `build-backend` value in `pyproject.toml` (`setuptools.build_meta`)
- Replace `respx` with `aioresponses` in dev dependencies

---

## [0.0.3] — 2026-02-23

### Added
- `YFinanceProvider` — stocks, forex, and crypto via yfinance
- `py.typed` marker for typed package consumers

---

## [0.0.2] — 2026-02-22

### Added
- `BinanceProvider` — crypto OHLCV via Binance klines endpoint
- `OHLCVProvider` abstract base class and `Candle` model
- Provider registry with asset-class-based routing

---

## [0.0.1] — 2026-02-22

### Added
- Initial project scaffold — `pyproject.toml`, package structure, README
