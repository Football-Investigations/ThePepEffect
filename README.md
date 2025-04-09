# Football’s Tactical Evolution: Can Strategy Bridge the Financial Gap?

## Abstract
This study examines the growing economic disparity in world football and its impact on competitive balance. While financial dominance has historically correlated with success, our analysis explores whether teams with smaller budgets can replicate elite performance through tactical efficiency. Using data from the top five European leagues (2017/18–2024/25), we applied regression analysis, PCA, and t-SNE clustering to assess team stylistic similarities and identify key performance indicators beyond financial expenditure.

Our findings reveal that certain underfunded clubs have adopted play styles comparable to the most successful teams, demonstrating that high performance is not solely dictated by budget. Additionally, we analyze the crucial role of managerial philosophy in shaping a team’s identity, illustrating how tactical approaches evolve under different leadership. The study further investigates the rate at which football tactics evolve, highlighting the need for clubs to prioritize adaptability in player recruitment.

By identifying trends in dominant play styles, managerial influence, and the sustainability of tactical systems, this research provides insight into how clubs can optimize performance within financial constraints. Our results challenge traditional assumptions about the correlation between spending power and success, suggesting that strategic planning and tactical cohesion are key to overachieving in modern football.

## Presentation
Watch the video presentation of this project here:
- https://youtu.be/oeJPhH4qTcE

## Project Structure
```
ThePepEffect/
│-- analysis/
│   │-- ThePepEffect.ipynb   # Jupyter Notebook for analysis
│-- data/                    # Raw and processed datasets
│-- plots/                   # Rendered graphs
│-- scripts/
│   │-- FBRefScraper.py      # Script for scraping football data

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
