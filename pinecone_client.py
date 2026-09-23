def validate_data_format(data):
    # Define the expected schema
    expected_schema = {"id": str, "vector": list, "metadata": dict}
    # Validate the data against the expected schema
    for key, expected_type in expected_schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            print(f"Invalid data format for key: {key}")
            return False
    return True
