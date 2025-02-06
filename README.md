# The Pep Guardiola Effect
---

## Abstract
---

## Project Structure
---
ThePepEffect/
│-- data/                   # Raw and processed datasets
│-- scripts/
│   │-- FBRefScraper.py     # Script for scraping football data
│-- analysis/
│   │-- ThePepEffect.ipynb   # Jupyter Notebook for analysis

## Prerequisites
---
Make sure you have the following installed:

Python 3.11+
[uv](https://docs.astral.sh/uv/) for dependency management

## Installation
---
### 1. Clone the Repo
```bash
git clone https://github.com/Football-Investigations/ThePepEffect.git
```

### 2. Install Dependencies
```bash
uv install
```

### 3a. Run the Data Collection Script
```bash
uv run scripts/FBRefScraper.py
```

### 3b. Run the Analysis
Find the Jupyter Notebook in the `analysis` directory, and run the cells.