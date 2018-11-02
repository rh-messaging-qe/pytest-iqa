"""PyTest fixtures."""

import pytest

from pytest_iqa.logger import get_logger

__all__ = ('iqa',)
log = get_logger(__name__)


@pytest.fixture()
def iqa(request):
    return request.config.iqa
