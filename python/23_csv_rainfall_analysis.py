# Q23 CSV Data Analysis - Rainfall Analysis - @JIYO P V 2026-09-06
import csv
import numpy as np
from collections import defaultdict

def create_rainfall_csv(csv_file="rainfall_data.csv"):
    """Create sample rainfall data CSV file"""
    try:
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Station", "Rainfall(mm)"])
            writer.writerows([
                ["2024-01-01", "Station A", 45.2],
                ["2024-01-02", "Station A", 52.3],
                ["2024-01-01", "Station B", 38.5],
                ["2024-01-02", "Station B", 41.2],
                ["2024-01-03", "Station A", 65.8],
                ["2024-01-03", "Station B", 55.3],
                ["2024-01-04", "Station C", 72.4],
                ["2024-01-04", "Station A", 48.9],
                ["2024-01-05", "Station C", 61.2],
                ["2024-01-05", "Station B", 44.7],
            ])
        print(f"CSV file '{csv_file}' created successfully")
    except IOError as e:
        print(f"Error creating CSV: {e}")

def analyze_rainfall(csv_file, results_file="rainfall_analysis_results.csv"):
    """Analyze rainfall data from CSV file and save results"""
    try:
        station_data = defaultdict(list)
        all_rainfall = []
        max_rainfall = 0
        max_date = ""
        max_station = ""
        
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                station = row["Station"]
                rainfall = float(row["Rainfall(mm)"])
                date = row["Date"]
                
                station_data[station].append(rainfall)
                all_rainfall.append(rainfall)
                
                if rainfall > max_rainfall:
                    max_rainfall = rainfall
                    max_date = date
                    max_station = station
        
        # Compute statistics
        print("\n=== Rainfall Analysis ===")
        print("Average rainfall per station:")
        for station, rainfall_list in station_data.items():
            avg = np.mean(rainfall_list)
            print(f"  {station}: {avg:.2f} mm")
        
        print(f"\nMaximum rainfall: {max_rainfall:.2f} mm on {max_date} at {max_station}")
        print(f"Standard deviation: {np.std(all_rainfall):.2f} mm")
        
        # Save results to new CSV file
        with open(results_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            for station, rainfall_list in station_data.items():
                writer.writerow([f"{station} Average", f"{np.mean(rainfall_list):.2f} mm"])
            writer.writerow(["Maximum Rainfall", f"{max_rainfall:.2f} mm ({max_date}, {max_station})"])
            writer.writerow(["Standard Deviation", f"{np.std(all_rainfall):.2f} mm"])
        
        print(f"\nResults saved to {results_file}")
    
    except FileNotFoundError:
        print(f"File {csv_file} not found")
    except Exception as e:
        print(f"Error: {e}")

# Execute the program
create_rainfall_csv()
analyze_rainfall("rainfall_data.csv")
