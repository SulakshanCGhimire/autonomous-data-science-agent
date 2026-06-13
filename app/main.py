from tools.data_loader import load_csv

def main():
    # Define the path to our sample data
    # (Using ../ because we will run this from inside the app/ folder)
    data_path = '../data/sample/students.csv'
    
    print("Initializing Autonomous Data Science Agent...")
    
    # Use our reusable module to load the data
    df = load_csv(data_path)
    
    # Print the required outputs
    print(f"Dataset loaded successfully!")
    print(f"Number of rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

if __name__ == "__main__":
    main()