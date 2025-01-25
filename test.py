import pytest
from merlin_fashion import model_loader

def test_model_loading_with_bug():
    # Try to load the model with a typo in the function name
    model = model_loade()  # Intentional typo in 'model_loader'
    assert model is not None, "Model should be loaded"
    
def test_prediction_with_bug():
    model = model_loader.load_model()
    result = model.predict("red dress")
    assert result == "expected_output", "Prediction does not match expected output"
