"""
This module defines tests of the overridden "createsuperuser" management command.

See:
    https://github.com/django/django/blob/master/django/contrib/auth/management/commands/createsuperuser.py
    https://github.com/django/django/blob/master/django/contrib/auth/management/commands/createsuperuser.py
    https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
    https://docs.python.org/3/library/argparse.html#partial-parsing

"""
import django.core.management
import django.test


class TestCreateSuperUserOverride(django.test.TestCase):
    """
    A test suite of the createsuperuser management command override.

    In addition to Django's existing tests of contrib.auth's createsuperuser, this management
    command override must pass these tests. Command executions in which the password option is
    omitted are not tested here as the overridden command should fall back to contrib.auth's
    behavior and should therefore pass all of the relevant, built-in Django tests.

    See:
        https://github.com/django/django/blob/master/tests/auth_tests/test_management.py

    """

    def test_interactive_password_option(self):
        """
        Test that the password option is accepted and saved successfully.

        When the password option is passed with a valid argument in an interactive execution, ensure
        that contrib.auth behavior is overridden and user is NOT prompted for a password value and
        NO exception is raised.

        Django's management command framework is built around Python's built-in argparse library for
        argument parsing. By default, when unknown options are encountered, argparse will raise
        a SystemExit exception. Ensure that the password option is NOT unknown to the
        createsuperuser command and that it will NOT cause a SystemExit exception.

        Note that argparse.ArgumentParser.parse_known_args() will not raise SystemExit on unknown
        options passed but this behavior is not used by the Django management command framework.

        See:
            https://docs.python.org/3/library/exceptions.html#SystemExit
            https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args

        """
        pass

    def test_noninteractive_password_option(self):
        """
        Test that no prompts or other overridden behavior is exhibited in noninteractive executions.

        When the password option is passed with a valid argument in a noninteractive execution,
        ensure that user is NOT prompted for a password value and NO exception is raised.

        Django's management command framework is built around Python's built-in argparse library for
        argument parsing. By default, when unknown options are encountered, argparse will raise
        a SystemExit exception. Ensure that the password option is NOT unknown to the
        createsuperuser command and that it will NOT cause a SystemExit exception.

        Note that argparse.ArgumentParser.parse_known_args() will not raise SystemExit on unknown
        options passed but this behavior is not used by the Django management command framework.

        See:
            https://docs.python.org/3/library/exceptions.html#SystemExit

        """
        pass
