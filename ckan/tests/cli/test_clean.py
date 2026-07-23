# -*- coding: utf-8 -*-
import pytest

from ckan.cli.cli import ckan
from ckan.tests.helpers import call_action


@pytest.mark.usefixtures("clean_db")
class TestUserClean:
    def test_output_if_there_are_not_invalid_users(self, cli):
        result = cli.invoke(ckan, ["clean", "users"])
        assert "No users were found with invalid images." in result.output

