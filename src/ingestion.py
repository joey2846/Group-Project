# Member A: Data Ingestion
import pandas as pd

def get_raw_data(file_path):
    return pd.read_excel(file_path)
