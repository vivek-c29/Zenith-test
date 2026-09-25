from pinecone_client import validate_data_format


def sync_data(data):
    # Log the incoming data for debugging
    print(f"Syncing data: {data}")
    if not validate_data_format(data):
        raise ValueError("Data format is invalid.")
    # Proceed with the sync operation
    # ... (rest of the sync logic)

