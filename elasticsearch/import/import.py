# Import the CSV module to read CSV files
import csv
# Import the Elasticsearch client
from elasticsearch import Elasticsearch
# Import the os module to work with file paths
import os
# Import the argparse module to handle command-line arguments
import argparse

def create_index(es, index_name, header):
    # Define the index settings and mappings based on the CSV header
    # Create a dictionary of properties with text type
    properties = {field: {"type": "text"} for field in header}
    settings = {
        "settings": {
            # Set the number of shards
            "number_of_shards": 1,
            # Set the number of replicas
            "number_of_replicas": 0
        },
        "mappings": {
            # Set the properties for the index
            "properties": properties
        }
    }
    # Create the index with the specified settings
    es.indices.create(index=index_name, body=settings)

def read_csv_and_index(csv_file, es):
    # Get the index name from the CSV filename (without extension)
    index_name = os.path.splitext(os.path.basename(csv_file))[0]
    # Open the CSV file in read mode
    with open(csv_file, mode='r') as file:
        # Create a CSV dictionary reader
        reader = csv.DictReader(file)
        # Get the header (field names) from the CSV file
        header = reader.fieldnames
        # Check if the index already exists
        if not es.indices.exists(index=index_name):
            # Create the index if it does not exist
            create_index(es, index_name, header)
        # Iterate over each row in the CSV file
        for row in reader:
            # Index each row into Elasticsearch
            es.index(index=index_name, body=row)

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Index CSV data into Elasticsearch')
    # Add arguments for Elasticsearch host, port, and CSV file path
    parser.add_argument('--host', type=str, required=True, help='Elasticsearch host')
    parser.add_argument('--port', type=int, required=True, help='Elasticsearch port')
    parser.add_argument('--csv_file', type=str, required=True, help='Path to the CSV file')
    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an Elasticsearch client
    es = Elasticsearch([{'host': args.host, 'port': args.port, 'scheme': 'http'}])
    
    # Read the CSV file and index the data
    read_csv_and_index(args.csv_file, es)
