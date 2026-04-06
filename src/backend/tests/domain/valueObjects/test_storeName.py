import domain.valueObjects.storeName as storeName
import pytest

def test_valid_store_name():
    valid_name = "Test Store"
    store_name = storeName.StoreName(valid_name)
    
    assert store_name.name == valid_name
    
def test_empty_store_name():
    with pytest.raises(ValueError) as excinfo:
        storeName.StoreName("")
    assert str(excinfo.value) == "Store name cannot be empty."
    
def test_exceeding_length_store_name():
    with pytest.raises(ValueError) as excinfo:
        long_name = "a" * 51  # 51 characters, exceeding the limit of 50
        storeName.StoreName(long_name)
    assert str(excinfo.value) == "Store name cannot exceed 50 characters."