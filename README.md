# Exploratory Data Analysis - CodeAlpha Task 2

## Project Overview

This project is developed as part of the CodeAlpha Internship - Task 2: Exploratory Data Analysis (EDA).

The project analyzes a product dataset collected during Task 1 using Python. The analysis focuses on understanding the dataset, identifying patterns, checking data quality, and visualizing important findings.

## Objective

The main objectives of this project are:

- Explore the structure of the dataset
- Understand variables and data types
- Identify missing values and duplicate records
- Analyze product prices
- Study product rating distribution
- Analyze product availability
- Identify patterns and trends
- Create visualizations to understand the data

## Dataset

The dataset was collected from the Books to Scrape demo website during Task 1.

The dataset contains the following information:

- Product Name
- Price
- Rating
- Availability

Total Records: 20 products

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## EDA Performed

The following analysis was performed:

1. Dataset structure and shape
2. Column names and data types
3. Missing value detection
4. Duplicate value detection
5. Statistical analysis of product prices
6. Average, highest and lowest product prices
7. Product rating distribution
8. Product availability analysis
9. Data visualization

## Visualizations

The project contains the following charts:

- Product Price Distribution
- Product Rating Distribution
- Product Availability Distribution
- Top 10 Most Expensive Products

All charts are stored inside the `eda_charts` folder.

## Project Structure

```text
task2_EDA/
│
├── eda_analysis.py
├── products_dataset.csv
├── README.md
│
└── eda_charts/
    ├── price_distribution.png
    ├── rating_distribution.png
    ├── availability_distribution.png
    └── top_10_expensive_products.png
How to Run

Install the required libraries:

py -m pip install pandas matplotlib seaborn

Run the EDA program:

py eda_analysis.py
Key Findings
The dataset contains 20 products.
No missing values were identified in the analyzed columns.
Product prices were converted into numeric values for statistical analysis.
Product ratings were analyzed to understand their distribution.
Product availability was analyzed using visualization.
Price distribution and the most expensive products were visualized.
Conclusion

This project demonstrates how Exploratory Data Analysis can be used to understand a dataset before further analysis. Python libraries such as Pandas, Matplotlib, and Seaborn were used to clean, analyze, and visualize the product data.

Author

M. Bala Murugan

Internship

CodeAlpha Internship - Task 2: Exploratory Data Analysis