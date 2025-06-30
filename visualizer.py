import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from colorama import Fore,Style

# 1. Pie Chart of total sales by Product
def pie_chart(df):
    totals= df.groupby("Product")["Amount"].sum()
    plt.figure(figsize=(6,6))
    plt.pie(totals, labels=totals.index, autopct="%1.1f%%", startangle=140)
    plt.title("Total Sales by Product")
    plt.show()

# 2. Line Graph of sales over time
def line_graph(df):
    df["Date"]=pd.to_datetime(df["Date"])
    totals_by_date = df.groupby("Date") ["Amount"].sum()
    plt.figure(figsize=(10, 5))
    plt.plot (totals_by_date.index, totals_by_date.values, marker="o", linestyle= "-")    
    plt.title("Sales over time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid=True
    plt.show()

# 3. Bar Chart of missing values before cleaning
def bar_chart_missing_values(df):
    missing = df.isnull().sum()
    plt.figure(figsize=(8,5))
    sns.barplot(x=missing.index, y=missing.values, palette="pastel")
    plt.title("Missing Values by Column")
    plt.ylabel("Number of Missing Values")
    plt.tight_layout()
    plt.show()
