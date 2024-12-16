# Rick and Morty Species Data Analysis
This project loads, cleans, and visualizes data related to species distribution and human vs non-human distribution from the Rick and Morty API. It performs the following key tasks:

- Loads the data either from a CSV file or by fetching it from the Rick and Morty API.
- Cleans the data by removing unnecessary columns and adding relevant attributes.
- Generates two types of visualizations:
    - A pie chart of species distribution and human vs non-human distribution.
    - A bar chart showing the breakdown of species, highlighting the most popular species.

Table of Contents
1. Installation
2. Usage
3. Functions
4. Installation

### Clone the repository:

```bash
git clone https://github.com/dmorton714/data_m2.git
```
Navigate into the project directory:

```bash
cd rick_n_morty
```

## Create a virtual environment:

#### Virtual Environment Commands

| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |


## Usage
Run the Script
To load the data, clean it, and generate the visualizations, simply run the scripts in `final.ipynb`

This will:

- Check if the CSV file rick_n_morty.csv exists. If it doesn't, the data will be fetched from the Rick and Morty API.
- Clean the data by removing unnecessary columns and adding a is_human column.
- Display two visualizations:
    - A pie chart showing the distribution of species and human vs non-human characters.
    - A bar chart showing the breakdown of species, with the most popular species highlighted.

| Functions | Description | Arguments | Returns |
| --- | --- | --- | --- | 
| load_or_fetch_data(csv_file_path: str, api_url: str) -> pd.DataFrame | Loads data from a CSV file if it exists. If the file does not exist, it fetches data from the provided API URL and saves it to the CSV file. | csv_file_path (str): The path to the CSV file. | api_url (str): The base URL of the API to fetch data from. | A Pandas DataFrame containing the loaded or fetched data. | 
| rnm_cleaning(rnm: pd.DataFrame) -> pd.DataFrame | Cleans the Rick and Morty DataFrame by dropping unnecessary columns, converting the created column to datetime format, and adding an is_human column. | rnm (pd.DataFrame): The input DataFrame. | The cleaned DataFrame. |
| plot_species_and_human_distribution(cleaned_rnm: pd.DataFrame) -> None | Plots two pie charts: one showing the species distribution and another showing the human vs non-human distribution. | cleaned_rnm (pd.DataFrame): The cleaned DataFrame with the species and is_human columns. | None. | 
| plot_species_breakdown(cleaned_rnm: pd.DataFrame) -> None | Plots a bar chart showing the breakdown of species, highlighting the most popular species. | cleaned_rnm (pd.DataFrame): The cleaned DataFrame with the species column. | None.| 

#### TO Make a requirements text file 
```bash
pip freeze > requirements.txt
```