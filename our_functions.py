import pandas as pd
from pandas import DataFrame

def clean_ks(kick_starter) -> pd.DataFrame:
    # Clean column names
    kick_starter.columns = kick_starter.columns.str.title()
    # kick_starter.columns = kick_starter.columns.str.strip().str.replace('_', ' ')
    
    # Drop unnecessary columns
    cols_to_drop = ['Id', 'Deadline', 'Launched']
    kick_starter = kick_starter.drop(columns=cols_to_drop)
    
    # Drop rows with missing values
    kick_starter = kick_starter.dropna()
    
    # Return the cleaned DataFrame
    return kick_starter


def filter_by_country(kick_starter: DataFrame, country: str) -> DataFrame:
    """
    Filters the Kickstarter dataset to include only rows for a specific country.

    Parameters:
        kick_starter (pandas.DataFrame): The Kickstarter dataset containing a 'Country' column.
        country (str): The country to filter the dataset by.

    Returns:
        pandas.DataFrame: A filtered DataFrame containing only rows where the 'Country' column matches the specified country.
    """
    return kick_starter[kick_starter['Country'] == country]


def summarize_backers(kick_starter: DataFrame) -> str:
    """
    Calculates and summarizes the total, mean, and median number of backers 
    from a Kickstarter dataset.

    Parameters:
        kick_starter (pandas.DataFrame): The Kickstarter dataset containing a 
                                         'Backers' column.

    Returns:
        str: A formatted string summarizing the total, mean (rounded to 2 decimal places),
             and median number of backers.
    """
    # Calculate total, mean, and median backers
    backer_sum = kick_starter['Backers'].sum()
    backer_mean = kick_starter['Backers'].mean().round(2)
    backer_median = kick_starter['Backers'].median()

    # Return a formatted string
    return (f"The total number of backers is {backer_sum}.\n"
            f"The mean number of backers is {backer_mean}.\n"
            f"The median number of backers is {backer_median}.")


def category_backers_summary(kick_starter: DataFrame) -> DataFrame:
    """
    Analyzes the Kickstarter dataset by grouping the data by category and summing the backers. 
    It then finds the category with the most backers, sorts the values, and returns a sorted DataFrame.

    Parameters:
        kick_starter (pandas.DataFrame): The Kickstarter dataset containing a 'Category' and 'Backers' column.

    Returns:
        pandas.DataFrame: A DataFrame containing categories and their summed backers, sorted in descending order by backers.
    """
    # Group by Category and sum the backers
    category_backers = kick_starter.groupby('Category')['Backers'].sum().reset_index()

    # Find the category with the most backers
    most_backers_category = category_backers['Backers'].idxmax()
    most_backers = category_backers['Backers'].max()

    # Sort the values by 'Backers'
    category_backers = category_backers.sort_values(by='Backers', ascending=False)

    return category_backers


