from domain.valueObjects.storeId import StoreID
import uuid
import pytest

def test_valid_store_id():
    
    valid_id = uuid.uuid4()
    print(len(str(valid_id)))
    store_id = StoreID(valid_id)
    
    assert store_id.id() == str(valid_id)
    
def test_empty_store_id():
    with pytest.raises(ValueError) as excinfo:
        StoreID(None)
    assert str(excinfo.value) == "Store ID cannot be empty."
    
def test_exceeding_length_store_id():
    with pytest.raises(ValueError) as excinfo:
        
        invalid_id = str(uuid.uuid4()) + "a"  # 37 characters, exceeding the limit of 36
        StoreID(invalid_id)
    assert str(excinfo.value) == "Store ID cannot exceed 36 characters."
