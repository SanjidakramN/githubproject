import pytest
from merlin_fashion import model_loader

def test_model_loading():
    # Correctly loading the model
    model = model_loader.load_model()  # Correct function name
    assert model is not None, "Model should be loaded"
    
def test_prediction():
    model = model_loader.load_model()
    result = model.predict("red dress")
    assert result == "expected_output", "Prediction does not match expected output"
