import csv
from pathlib import Path

DATASET_PATH = Path("data/raw/ai4i2020.csv")
EXPECTED_COLUMNS = {
    "UDI",
    "Product ID",
    "Type",
    "Machine failure",
}


def test_seed_dataset_is_available_and_has_expected_columns() -> None:
    assert DATASET_PATH.is_file()

    with DATASET_PATH.open(newline="", encoding="utf-8-sig") as dataset:
        reader = csv.DictReader(dataset)
        assert EXPECTED_COLUMNS <= set(reader.fieldnames or [])
        assert next(reader, None) is not None
