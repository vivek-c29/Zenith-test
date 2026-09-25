from sync_manager import sync_data

def test_sync_valid_data():
    data = {
        "id": "test-1",
        "vector": [0.1, 0.2, 0.3],
        "metadata": {"source": "test"},
    }

    sync_data(data)