from colorama import init, Fore, Style
init(autoreset=True)

import logging
logging.basicConfig(
    filename="csv_cleaner.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 1. Function to remove rows with missing data
def remove_missing_rows(df):
    original_count = len(df)
    cleaned_df = df.dropna()
    removed_count = original_count - len(cleaned_df)
    logging.info(f"Removed{removed_count} rows with missing values")
    print(Fore.RED + f"\nRemoved{removed_count} rows with missing values")
    print(cleaned_df)
     
    cleaned_df.to_csv("cleaned_dropped.csv", index=False)
    print(Fore.GREEN + "Saved cleaned data (dropped rows) to 'cleaned_dropped.csv'")

# 2. Function to fill missing values
def fill_missing_values(df):
    filled_df = df.fillna({
        "Name": "Unknown",
        "Email": "unknown@email.com",
        "Product": "Unknown Product",
        "Amount": 0.0,
        "Date": "2025-01-01"
    })
    logging.info("Filled missing values and saved to 'cleaned_filled.csv'")
    print(Fore.BLUE + Style.DIM + "\nMissing values filled:")
    print(filled_df)
    filled_df.to_csv("cleaned_filled.csv" ,index=False)
    print(Fore.BLUE + Style.BRIGHT + "Saved filled data to 'cleaned_filled.csv'")
    return filled_df

