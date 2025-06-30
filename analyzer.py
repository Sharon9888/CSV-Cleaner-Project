from colorama import init, Fore, Style
init(autoreset=True)

# 3. Function to analyze the data
def analyze_data(df):
    total = df["Amount"].sum()
    average = df["Amount"].mean()
    print("\nData Analysis:")
    print(Fore.CYAN + "Total Amount Spent:", total)
    print(Fore.CYAN + "Average Amount Spent:", average)