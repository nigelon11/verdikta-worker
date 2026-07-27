# Verdikta Bounty Agent

An autonomous agent that monitors, evaluates, and interacts with Verdikta bounties on Base L2.

## What It Does

- **Monitor** open bounties on bounties.verdikta.org
- **Evaluate** viability based on threshold, payout, and remaining time
- **Read** bounty details, submission history, and AI evaluation results
- **Submit** work to bounties (via Verdikta Bot API)
- **Track** your submissions and scores across sessions

## Architecture

```
verdikta_agent.py          # Main agent loop
├── BountyMonitor          # Watches for new bounties
├── ViabilityScorer        # Evaluates ROI of each bounty
├── VerdiktaAPI            # API client (register, read, submit)
└── SubmissionTracker      # Tracks your submissions & scores
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Register for API Key

```bash
python verdikta_agent.py --register
```

This calls `POST /api/bots/register` and saves your API key to `config.json`.

### 3. Configure

Edit `config.json`:

```json
{
  "api_key": "YOUR_API_KEY",
  "wallet_address": "0xYOUR_WALLET",
  "min_payout_eth": 0.001,
  "max_threshold": 90,
  "check_interval_minutes": 30
}
```

### 4. Run

```bash
# Monitor mode — watch for new bounties
python verdikta_agent.py --monitor

# Check specific bounty
python verdikta_agent.py --check 157

# List all open bounties
python verdikta_agent.py --list

# View your submission history
python verdikta_agent.py --history
```

## How the Verdikta API Works

### Authentication

All API calls require the `X-Bot-API-Key` header:

```bash
curl -H "X-Bot-API-Key: YOUR_KEY" https://bounties.verdikta.org/api/jobs/157
```

### Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/bots/register` | POST | Register bot, get API key |
| `/api/jobs/{id}` | GET | Get bounty details |
| `/api/jobs` | GET | List all bounties |
| `/api/jobs/{id}/submit` | POST | Submit work to bounty |
| `/api/jobs/{id}/submissions` | GET | Get submission history |

### On-Chain Interaction

The BountyEscrow contract on Base L2:

```
Contract: 0x2Ae271f5E86bee449a36B943414b7C1a7b39772D
Network: Base Mainnet (Chain ID: 8453)
```

The agent reads on-chain data via BaseScan API to verify payments and submission statuses.

## Bounty Viability Scoring

The agent calculates a viability score for each open bounty:

```
viability = (payout_usd / effort_hours) * (1 - threshold/100) * time_factor
```

Where:
- `payout_usd` = ETH amount × current ETH price
- `effort_hours` = estimated effort based on bounty class
- `threshold` = minimum score required
- `time_factor` = remaining time / total time (urgency adjustment)

Bounties with viability > target are flagged for action.

## Example Output

```
🔍 Monitoring Verdikta bounties...

📊 Open Bounties:
┌─────┬────────────────────────────────┬──────────┬───────────┬─────────┐
│  #  │ Title                          │ Payout   │ Threshold │ Viab.   │
├─────┼────────────────────────────────┼──────────┼───────────┼─────────┤
│ 157 │ I Tried to Cheat a Bounty      │ 0.02 ETH │ 88%       │ HIGH ⭐ │
│ 158 │ Build an Agent (Verdikta)      │ 0.02 ETH │ 88%       │ HIGH ⭐ │
│ 160 │ Reddit AMA Post                │ 0.008 ETH│ 85%       │ MED     │
│ 153 │ CS3 Republish                  │ 0.002 ETH│ 88%       │ LOW     │
└─────┴────────────────────────────────┴──────────┴───────────┴─────────┘

🎯 Recommended: #157, #158 (targeted, high payout)
```

## Files

- `verdikta_agent.py` — Main agent code
- `config.json` — Configuration (API key, wallet, preferences)
- `requirements.txt` — Python dependencies
- `README.md` — This file

## Security Notes

- Never commit `config.json` with your API key
- The agent does NOT send on-chain transactions automatically — it only READS data and prepares submissions
- All ETH transfers require manual wallet confirmation

## License

MIT
