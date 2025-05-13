# API Overview

This section summarizes key modules and classes:

## `chainfl.agent`

- `LocalTrainer` – trains logistic regression model
- `ModelHasher` – hashes model weights
- `Signer` – RSA-based model signature
- `Communicator` – model exchange

## `chainfl.blockchain`

- `BlockchainSimulator` – simulated ledger
- `ConsensusEngine` – PBFT-style consensus
- `LedgerExplorer` – chain inspection

## `chainfl.coordinator`

- `Aggregator` – FedAvg implementation
- `IntegrityChecker` – model hash validation
- `GlobalPublisher` – publishes global models

## `chainfl.simulator`

- `SimulationRunner` – core simulation loop
- `Scheduler` – agent selection logic
- `Metrics`, `Logger` – evaluation and logging