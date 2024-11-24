import pytest
from unittest.mock import patch, MagicMock
import llm
from llm_inference import InferenceChat, get_inference_models, register_models

@pytest.fixture
def mock_llm_key():
    with patch('llm.get_key', return_value='fake-key'):
        yield

@pytest.fixture
def mock_register():
    return MagicMock()

def test_get_inference_models():
    models = get_inference_models()
    assert isinstance(models, list)
    assert len(models) > 0

    # Test first model structure
    first_model = models[0]
    assert first_model["id"] == "meta-llama/llama-3.2-1b-instruct/fp-8"
    assert first_model["aliases"] == ["inf-1b"]

def test_inference_chat_class():
    chat = InferenceChat(
        model_id="inference/test-model",
        model_name="test-model",
        api_base="https://api.inference.net/v1",
        headers={"HTTP-Referer": "https://llm.datasette.io/", "X-Title": "LLM"}
    )

    assert chat.needs_key == "inference"
    assert chat.key_env_var == "INFERENCE_KEY"
    assert str(chat) == "Inference: inference/test-model"

def test_register_models_with_key(mock_llm_key, mock_register):
    register_models(mock_register)
    assert mock_register.call_count == len(get_inference_models())

    # Check first registration
    first_call = mock_register.call_args_list[0]
    model, kwargs = first_call.args[0], first_call.kwargs

    assert isinstance(model, InferenceChat)
    assert kwargs["aliases"] == ["inf-1b"]

def test_register_models_without_key():
    with patch('llm.get_key', return_value=None):
        register = MagicMock()
        register_models(register)
        register.assert_not_called()

@pytest.mark.parametrize("model_def", get_inference_models())
def test_model_definitions(model_def):
    """Test that each model definition has the required structure"""
    assert "id" in model_def
    assert isinstance(model_def["id"], str)
    assert "aliases" in model_def
    assert isinstance(model_def["aliases"], list)
    assert all(isinstance(alias, str) for alias in model_def["aliases"])
