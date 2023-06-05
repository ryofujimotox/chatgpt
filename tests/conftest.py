from chatgpt.tests.lib.get_env import env
import pytest


@pytest.fixture(autouse=True)
def common_setup_teardown(request):
    env_var = request.node.get_closest_marker("check_env")
    if env_var:
        env_value = env(env_var.args[0])
        if env_value == "0":
            pytest.skip(f"{env_var.args[0]} is 0")


@pytest.fixture(scope="module")
def api_key():
    return env("OPENAI_API_KEY")
