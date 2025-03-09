# Football’s Tactical Evolution: Can Strategy Bridge the Financial Gap?


## Abstract
This study examines how elite football has evolved since Pep Guardiola's arrival at Manchester City in 2016. Using data from the top five European leagues (2017/18–2024/25), we applied PCA for dimensionality reduction and t-SNE clustering to identify key style-related statistics and compare Manchester City's tactical evolution to other top teams. We investigate whether successful teams increasingly mirror Guardiola’s approach, analyzing the sustainability of dominant styles. Our findings aim to reveal whether modern football undergoes cyclical stylistic shifts and to what extent managers, players, and play styles shape the game’s evolution.

## Project Structure
```
ThePepEffect/
│-- data/                   # Raw and processed datasets
│-- scripts/
│   │-- FBRefScraper.py     # Script for scraping football data
│-- analysis/
│   │-- ThePepEffect.ipynb   # Jupyter Notebook for analysis
```

## Prerequisites
Make sure you have the following installed:

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Installation
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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
