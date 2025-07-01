
# Market Risk Analysis with PySpark, Kafka & MetaTrader5

## Overview

This project demonstrates a scalable approach to financial market risk analysis using Python, PySpark, Kafka streaming, and MetaTrader5 data feed.  
It simulates or ingests real-time market tick data, performs streaming analytics, and calculates portfolio risk metrics such as Value at Risk (VaR).

---

## Features

- Real-time market tick data ingestion from MetaTrader5 (MT5) terminal  
- Stream processing using PySpark Structured Streaming  
- Kafka integration for scalable message passing and event streaming  
- Portfolio risk calculations including historical VaR  
- Modular Python notebooks and scripts for easy customization  
- CI/CD pipeline setup using GitHub Actions for automatic testing and deployment

---

## Prerequisites

- Python 3.12+  
- Java 11 or OpenJDK 11+ (required for Spark and Kafka)  
- Apache Kafka & Zookeeper installed and configured  
- MetaTrader5 terminal installed and configured  
- Basic familiarity with Spark, Kafka, and Python

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create and activate a Python virtual environment:

```bash
python -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup Kafka and Zookeeper services locally or on your cluster.

---

## Usage

### Running the Data Simulation & Analysis Notebook

Open `market_tick_pyspark_simulation.ipynb` in Jupyter Notebook or JupyterLab:

```bash
jupyter notebook market_tick_pyspark_simulation.ipynb
```

This notebook simulates streaming tick data, calculates portfolio returns, and estimates Value at Risk (VaR).

### Running Real-Time Tick Data Streaming (Advanced)

- Ensure MetaTrader5 terminal is running and authorized for API access  
- Start Zookeeper and Kafka brokers  
- Run your Kafka producer script that publishes MT5 tick data to Kafka topic  
- Run PySpark Structured Streaming consumer script to process live ticks and perform analytics

---

## Continuous Integration / Continuous Deployment (CI/CD)

This project uses GitHub Actions for CI:

- Runs Python tests on every push and pull request  
- Installs dependencies from `requirements.txt`  
- Can be extended to run code quality checks, notebooks execution, or deployment pipelines

Workflow file located at `.github/workflows/python-ci.yml`.

---

## Project Structure

```
├── .github/
│   └── workflows/
│       └── python-ci.yml         # GitHub Actions workflow
├── notebooks/
│   └── market_tick_pyspark_simulation.ipynb  # Main notebook for simulation & VaR calculation
├── scripts/
│   ├── kafka_producer.py         # Kafka producer example for MT5 tick data
│   ├── spark_streaming_consumer.py  # PySpark streaming consumer script
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

---

## References

- [MetaTrader5 Python API](https://www.mql5.com/en/docs/integration/python_metatrader5)  
- [PySpark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)  
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)  
- [Value at Risk (VaR) Concepts](https://www.investopedia.com/terms/v/var.asp)

---

## License

MIT License © Your Name

---

## Contact

For questions or contributions, please open an issue or contact me at your.email@example.com.
