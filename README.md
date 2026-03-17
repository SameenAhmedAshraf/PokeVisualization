# Pokémon Data Analysis & Visualization

A comprehensive data analysis project exploring Pokémon characteristics, types, and stats using Python data science libraries and an interactive Streamlit dashboard.

## Project Overview

This project performs in-depth exploratory data analysis (EDA) on the Pokémon dataset, uncovering patterns in type distribution, stat correlations, generation trends, and legendary Pokémon characteristics. The analysis is presented through both a detailed Jupyter notebook and an interactive one-page dashboard.

## Features

- **Exploratory Data Analysis**: Detailed data cleaning, exploration, and statistical analysis
- **Interactive Dashboard**: One-page Streamlit app with 5 compact visualizations
- **Type Analysis**: Distribution and characteristics of 18 Pokémon types
- **Stat Correlations**: Heatmap analysis showing relationships between attributes
- **Generation Trends**: Evolution of Pokémon stats across 6 generations
- **Legendary Analysis**: Comparison of legendary vs non-legendary Pokémon

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SameenAhmedAshraf/PokeVisualization.git
   cd PokeVisualization
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit pandas matplotlib seaborn scikit-learn numpy jupyter
   ```

## Usage

### Running the Interactive Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open at `http://localhost:8501` and display:
- 5 KPI metrics (Total Pokémon, Types, Generations, Legendary count, Average stats)
- 5 compact visualizations in one row:
  - Type Distribution (pie chart)
  - Top Attack Stats (horizontal bar chart)
  - Attribute Correlations (heatmap)
  - Generation Stats (line chart)
  - Legendary Impact (bar chart)
- Key findings summary

### Running the Jupyter Notebook

```bash
jupyter notebook PokemonDataVisualization.ipynb
```

The notebook contains:
1. Data loading and initial exploration
2. Data cleaning and preprocessing
3. Type distribution analysis
4. Attribute correlation analysis
5. Type-based stat analysis
6. Generation analysis
7. Violin plot visualizations
8. Legendary vs non-legendary comparisons
9. Pokémon comparison tool
10. Comprehensive summary and insights

## Key Findings

### Dataset Overview
- **Total Pokémon**: 800+ unique Pokémon
- **Type Distribution**: 18 distinct types
- **Generations**: 6 generations covered
- **Legendary Pokémon**: ~80 legendary species

### Major Insights

1. **Type Distribution**
   - Water, Normal, and Grass types dominate (~45% of all Pokémon)
   - Water type represents ~14% of the dataset
   - Balanced distribution across remaining types

2. **Stat Correlations**
   - HP, Attack, Defense, Sp. Atk, Sp. Def, and Speed are highly correlated with Total stats (0.9+)
   - Generation has minimal correlation with stats
   - Legendary status shows some correlation with stat distribution

3. **Type Characteristics**
   - **Dragon types** excel in Attack capability (avg: 123)
   - **Steel types** lead in Defense (avg: 106)
   - **Water types** are the most balanced across attributes
   - **Psychic types** have highest Sp. Atk relative to other types

4. **Generation Trends**
   - **Generation 3** has the strongest Pokémon overall (avg total: 358)
   - Stats remain relatively consistent across generations
   - Each generation introduces both weak and strong Pokémon independently

5. **Legendary Pokémon**
   - Legendary Pokémon have **+106 average stat advantage** over non-legendary
   - Average total stats: 
     - Legendary: 599
     - Non-legendary: 493
   - Legendary status is a strong predictor of high stats across all types

6. **Data Quality**
   - Missing Type 2 values filled with Type 1 (136 Pokémon had single type)
   - No other missing values in the dataset
   - Complete coverage across all numeric attributes

## Data Files

- `Pokemon.csv`: Raw Pokémon dataset with 800+ records
- `PokemonDataVisualization.ipynb`: Detailed analysis notebook
- `dashboard.py`: Streamlit dashboard application

## Technologies Used

- **Python 3**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Statistical visualizations
- **Scikit-learn**: Machine learning utilities
- **Streamlit**: Interactive web dashboard
- **Jupyter**: Interactive data analysis environment

## Project Structure

```
PokeVisualization/
├── README.md
├── Pokemon.csv
├── PokemonDataVisualization.ipynb
├── dashboard.py
└── requirements.txt
```

## Requirements

See `requirements.txt` for full list. Key dependencies:
- streamlit >= 1.55.0
- pandas >= 1.4.0
- matplotlib >= 3.4
- seaborn >= 0.13.0
- numpy >= 1.23
- scikit-learn >= 1.0

## License

This project is open source and available under the MIT License.

## Author

Sameen Ahmed Ashraf

## Contributing

Contributions are welcome! Feel free to fork, submit issues, or create pull requests.
