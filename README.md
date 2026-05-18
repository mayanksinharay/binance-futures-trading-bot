# Binance Futures Testnet Trading Bot

A simplified Python trading bot for Binance Futures Testnet (USDT-M).

This project was built as part of a Python Developer internship assignment. The application allows users to place MARKET and LIMIT orders on Binance Futures Testnet through a command-line interface (CLI).

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support for BUY and SELL orders
- CLI-based user input
- Input validation
- Logging of API requests and responses
- Exception handling
- Modular and reusable project structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Installation

### 1. Clone the Repository

```bash
git clone <your_repository_link>
cd trading_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Binance Testnet Setup

1. Create a Binance Futures Testnet account
2. Generate API Key and Secret Key
3. Create a `.env` file in the root directory

Example:

```env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

---

## Usage

### MARKET Order

```bash
py -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
py -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Validation Examples

### Invalid Side

```bash
py -m bot.cli --symbol BTCUSDT --side ABC --type MARKET --quantity 0.001
```

### Negative Quantity

```bash
py -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity -5
```

---

## Logging

Logs are automatically stored in:

```text
logs/trading_bot.log

The log file records:
- API responses

---

## Error Handling

The application handles:
- Invalid order type
- Negative quantity
- Missing price for LIMIT orders
- Binance API errors
- Network/API exceptions

---

## Requirements

Contents of `requirements.txt`:

```text
python-binance
python-dotenv
```

---

## Notes

- This project uses Binance Futures Testnet only.
- No real funds are used.
- API keys should never be shared publicly.

---

## Author

Mayank Sinharay
