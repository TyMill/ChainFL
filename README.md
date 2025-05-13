# ChainFL

[![PyPI version](https://img.shields.io/pypi/v/chainfl.svg)](https://pypi.org/project/chainfl/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15399944.svg)](https://doi.org/10.5281/zenodo.15399944)
[![Python](https://img.shields.io/pypi/pyversions/chainfl.svg)](https://pypi.org/project/chainfl/)
[![License](https://img.shields.io/github/license/tymmill/chainfl)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Tests](https://github.com/tymmill/chainfl/actions/workflows/tests.yml/badge.svg)](https://github.com/tymmill/chainfl/actions)
[![Downloads](https://static.pepy.tech/badge/chainfl)](https://pepy.tech/project/chainfl)


**ChainFL** is a modular simulation framework for Federated Learning with blockchain-based trust and model integrity mechanisms. Designed for experimentation, research, and education in secure and decentralized AI.

## 🚀 Features

- Federated Learning with pluggable aggregation (FedAvg, etc.)
- Blockchain-simulated model registry with PBFT-style consensus
- Agent-based training, hashing, signing, and verification
- Support for Sybil attack simulation and trust audits
- YAML-based configuration and modular architecture

## 📊 Architecture Diagram

```
[Simulation] → [Agent Nodes] → [Consensus Engine] → [Blockchain Ledger]
         ↓                        ↑                        ↓
   [Scheduler]        ←    [Coordinator: Aggregator + Publisher]
```

## 📁 Project Structure

```
chainfl/
├── agent/          ← Model training, hashing, signing
├── blockchain/     ← Ledger, consensus, validators
├── coordinator/    ← Aggregation, verification, publishing
├── simulator/      ← Rounds, metrics, scheduler
├── utils/          ← YAML loader, crypto helpers
├── examples/       ← Run scenarios: minimal, sybil attack
├── tests/          ← Pytest unit tests
├── config/         ← default.yaml configuration
```

## 📦 Installation

```bash
git clone https://github.com/yourname/chainfl.git
cd chainfl
pip install -r requirements.txt
```

## 🧪 Run an Example

```bash
python examples/minimal_chainfl_run.py
```

## 📜 License

MIT License – see [LICENSE](./LICENSE)

---

Created by Tymoteusz Miller
