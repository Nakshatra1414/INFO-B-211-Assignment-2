# INFO-B-211-Assignment-2
Player Season Performance Analysis
Project Overview

This program analyzes basketball player statistics from a seasonal dataset and finds the top 100 player-seasons across several performance and efficiency metrics.
It reads data from a CSV file, calculates statistics, and prints the top performers in each category.

This project demonstrates:

Object-oriented programming in Python
CSV data processing
Statistical calculations
Sorting and filtering data
Metrics Calculated

The program calculates the following:

Field Goal Accuracy = FGM ÷ FGA
Three-Point Accuracy = 3PM ÷ 3PA
Free Throw Accuracy = FTM ÷ FTA
Points per Minute = PTS ÷ MIN
Overall Shooting Accuracy = (FGM + FTM) ÷ (FGA + FTA)
Blocks per Game = BLK ÷ GP
Steals per Game = STL ÷ GP
Data Filtering Rules

To make the results fair, minimum thresholds are applied:

Field Goal Accuracy: at least 100 attempts
Three-Point Accuracy: at least 50 attempts
Free Throw Accuracy: at least 50 attempts
Overall Shooting Accuracy: at least 100 field goal attempts
Blocks per Game: at least 30 games and 40 total blocks
Steals per Game: at least 30 games and 40 total steals

File Requirement

The program expects a CSV file named:

players_stats_by_season_full_details.csv

This file must be placed in the same folder as the Python script.

How to Run the Program

Make sure Python is installed.

Place the CSV file and the Python script in the same folder.

Open a terminal or command prompt.

Navigate to the folder.

Run:

python your_script_name.py

Example Output

--- Top 100 Field Goal Accuracy ---
Player Name (Season) - 0.830
Player Name (Season) - 0.802

--- Top 100 Three-Point Accuracy ---
Player Name (Season) - 0.650

Program Structure
PlayerSeason class
Stores player statistics
Contains methods to calculate metrics
top_100 function
Filters players using minimum requirements
Sorts players by the selected metric
Returns the top 100 results
print_top function
Prints formatted results to the console
Skills Demonstrated
Python classes and methods
CSV file handling
Data filtering and sorting
Basic sports analytics
Clean and modular code design