import pandas as pd
import os

def load_data(path):
    """Load the raw CSV file into a pandas DataFrame."""
    df = pd.read_csv(path, low_memory=False)
    return df

def rename_columns(df):
    """Standardize column names to snake_case for easier coding and DB compatibility."""
    df = df.rename(columns={
        'Order ID': 'order_id',
        'Date': 'date',
        'Status': 'status',
        'Fulfilment': 'fulfilment',
        'Sales Channel ': 'sales_channel',
        'ship-service-level': 'ship_service_level',
        'Style': 'style',
        'SKU': 'sku',
        'Category': 'category',
        'Size': 'size',
        'ASIN': 'asin',
        'Courier Status': 'courier_status',
        'Qty': 'quantity_ordered',
        'Currency': 'currency',
        'Amount': 'amount',
        'ship-city': 'ship_city',
        'ship-state': 'ship_state',
        'ship-postal-code': 'ship_postal_code',
        'ship-country': 'ship_country',
        'promotion-ids': 'promotion_ids',
        'B2B': 'b2b',
        'fulfilled-by': 'fulfilled_by',
    })
    return df

def drop_unused_columns(df):
    """Remove redundant or empty columns found during initial data exploration."""
    if 'Unnamed: 22' in df.columns:
        df = df.drop(columns=['Unnamed: 22'])
    if 'index' in df.columns:
        df = df.drop(columns=['index'])
    return df

def fix_dtypes(df):
    """Convert columns to their correct data types (e.g., strings to datetime)."""
    # Specified format '%m-%d-%y' to avoid UserWarnings and improve performance
    df['date'] = pd.to_datetime(df['date'], format='%m-%d-%y', errors='coerce')
    return df

def drop_duplicates(df):
    """Remove identical rows to ensure data integrity."""
    df = df.drop_duplicates()
    return df

def handle_missing(df):
    """Fill null values with 'Unknown', 'None', or 0 to avoid calculation errors."""
    df['fulfilled_by'] = df['fulfilled_by'].fillna('Unknown')
    df['promotion_ids'] = df['promotion_ids'].fillna('None')
    df['currency'] = df['currency'].fillna('Undefined')
    df['amount'] = df['amount'].fillna(0)
    df['ship_city'] = df['ship_city'].fillna('Unknown')
    df['ship_state'] = df['ship_state'].fillna('Unknown')
    df['ship_country'] = df['ship_country'].fillna('Unknown')
    df['ship_postal_code'] = df['ship_postal_code'].fillna('Unknown')
    df['courier_status'] = df['courier_status'].fillna('Unknown')
    
    # Business Logic: If an order is cancelled, ensure courier status reflects that
    df.loc[df['status'] == 'Cancelled', 'courier_status'] = 'Cancelled'
    return df

def clean_ship_state(df):
    """Clean and standardize Indian state names (e.g., mapping codes like 'PB' to 'Punjab')."""
    ship_state_map = {
        'NEW_DELHI': 'DELHI', 'DELHI': 'DELHI', 'ORISSA': 'ODISHA',
        'AR': 'ARUNACHAL_PRADESH', 'PONDICHERRY': 'PUDUCHERRY',
        'RAJSTHAN': 'RAJASTHAN', 'RAJSHTHAN': 'RAJASTHAN',
        'RAJSH_THAN': 'RAJASTHAN', 'PB': 'PUNJAB', 'RJ': 'RAJASTHAN',
        'NL': 'NAGALAND', 'DADRA_AND_NAGAR': 'DADRA_&_NAGAR_HAVELI',
    }
    df['ship_state'] = (
        df['ship_state']
        .str.strip()
        .str.replace(' ', '_')
        .str.upper()
        .replace(ship_state_map)
        .str.capitalize()
        .str.split('/').str[0]
    )
    # Remove rows with specific non-state codes like 'Apo'
    df = df[df['ship_state'] != 'Apo']
    return df

def clean_category(df):
    """Standardize category names by replacing spaces with underscores and capitalizing."""
    df['category'] = (
        df['category']
        .str.replace(' ', '_')
        .str.capitalize()
    )
    return df

def save_data(df, path):
    """Create the destination folder if it doesn't exist and save the cleaned CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"File successfully saved to: {path}")

def run_pipeline(input_path='data/raw/amazon_sales.csv', output_path='data/cleaned/amazon_sales_cleaned.csv'):
    """The main entry point that executes the entire ETL (Extract, Transform, Load) process."""
    print("Starting data cleaning pipeline...")
    df = load_data(input_path)
    df = rename_columns(df)
    df = drop_unused_columns(df)
    df = fix_dtypes(df)
    df = drop_duplicates(df)
    df = handle_missing(df)
    df = clean_ship_state(df)
    df = clean_category(df)
    save_data(df, output_path)
    print("Pipeline completed successfully!")
    return df

if __name__ == '__main__':
    run_pipeline()