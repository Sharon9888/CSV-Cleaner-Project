import pandas as pd
from colorama import init, Fore, Style
init (autoreset=True)
from visualizer import pie_chart, line_graph, bar_chart_missing_values


from data_cleaner import remove_missing_rows, fill_missing_values
from analyzer import analyze_data
from visualizer import pie_chart

import logging
logging.basicConfig(
    filename="csv_cleaner.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 4. Main menu function
def main():
    try:
        # Load the original CSV file
        df = pd.read_csv("data.csv")
    except FileNotFoundError:
        print(Fore.RED + "RROR: 'data.csv' file not found in this folder.")
        return

    while True:
        # Show menu
        print(Fore.BLUE + "\n========= CSV CLEANER MENU =========")
        print("1. Remove rows with missing data")
        print("2. Fill missing values")
        print("3. Analyze data")
        print("4. Show pie chart (Total sales by product)")
        print("5.Show line graph (Sales over time)")
        print("6. Show bar chart (Missing values before cleaning)")
        print("7. Exit")
        
        
        choice = input("Choose an option (1-7): ")
        if choice == "1": 
            remove_missing_rows(df)
        elif choice == "2": 
            fill_missing_values(df)
        elif choice == "3": 
            filled_df = fill_missing_values(df) 
            analyze_data(filled_df)
        elif choice =="4":
            filled_df=fill_missing_values(df)
            pie_chart(filled_df)    
        elif choice == "5":
            filled_df = fill_missing_values(df)
            line_graph(filled_df)
        elif choice == "6":
            bar_chart_missing_values(df)
        elif choice == "7": 
            print(Fore.BLACK + "Goodbye!")
            break
        else: 
             print(Fore.RED + Style.BRIGHT+ "Invalid choice")

# 5. Run the program
if __name__ == "__main__":
    main()
