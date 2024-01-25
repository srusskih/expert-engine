import pytest
from password_gen_api.password_generator import PasswordGenerator, Configuration


def assure_length(expected_length):
    def _assure(password):
        assert len(password) == expected_length
    return _assure


@pytest.mark.parametrize(
    "configuration, validate",
    (
        (
            Configuration(length=8),
            assure_length(8),
        ),
        (
                Configuration(length=1),
                assure_length(1),
        ),
        (
                Configuration(length=16),
                assure_length(16),
        ),
    )
)
def test_simple(configuration, validate):
    validate(PasswordGenerator(configuration).generate())
