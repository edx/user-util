# -*- coding: utf-8 -*-

"""Main module."""
import hashlib


RETIRED_USERNAME_DEFAULT_FMT = 'retired_username_{}'
RETIRED_EMAIL_DEFAULT_FMT = 'retired_email_{}@retired.edx.org'
SALT_LIST_EXCEPTION = ValueError("Salt must be a list -or- tuple of all historical salts.")


def _compute_retired_hash(value_to_retire, salt):
    """
    Returns a retired value given a value to retire and a hash.

    Arguments:
        value_to_retire (str): Value to be retired.
        salt (str): Salt string used to modify the retired value before hashing.
    """
    return hashlib.sha1(
        salt.encode() + value_to_retire.encode()
    ).hexdigest()


def get_all_retired_usernames(username, salt_list, retired_username_fmt=RETIRED_USERNAME_DEFAULT_FMT):
    """
    Returns a generator of possible retired usernames based on the original username
    and all the historical salts, from oldest to current.
    The current salt is assumed to be the last salt in the list.

    Raises :class:`~ValueError` if the salt isn't a list of salts.

    Arguments:
        username (str): The name of the user to be retired.
        salt_list (list/tuple): List of all historical salts.

    Yields:
        Returns a generator of possible retired usernames based on the original username
        and all the historical salts, including the current salt, from oldest to current.
    """
    if not isinstance(salt_list, (list, tuple)):
        raise SALT_LIST_EXCEPTION

    for salt in salt_list:
        yield retired_username_fmt.format(_compute_retired_hash(username, salt))


def get_all_retired_emails(email, salt_list, retired_email_fmt=RETIRED_EMAIL_DEFAULT_FMT):
    """
    Returns a generator of possible retired email addresses based on the original email
    and all the historical salts, from oldest to current.
    The current salt is assumed to be the last salt in the list.

    Raises :class:`~ValueError` if the salt isn't a list of salts.

    Arguments:
        email (str): Email address of the user to be retired.
        salt_list (list/tuple): List of all historical salts.

    Yields:
        Returns a generator of possible retired email addresses based on the original email
        and all the historical salts, including the current salt, from oldest to current.
    """
    if not isinstance(salt_list, (list, tuple)):
        raise SALT_LIST_EXCEPTION

    for salt in salt_list:
        yield retired_email_fmt.format(_compute_retired_hash(email, salt))


def get_retired_username(username, salt_list, retired_username_fmt=RETIRED_USERNAME_DEFAULT_FMT):
    """
    Returns a retired username based on the original username
    and all the historical salts, from oldest to current.
    The current salt is assumed to be the last salt in the list.

    Raises :class:`~ValueError` if the salt isn't a list of salts.

    Arguments:
        username (str): The name of the user to be retired.
        salt_list (list/tuple): List of all historical salts.

    Yields:
        Returns a retired username based on the original username
        and all the historical salts, including the current salt.
    """
    if not isinstance(salt_list, (list, tuple)):
        raise SALT_LIST_EXCEPTION

    return retired_username_fmt.format(_compute_retired_hash(username, salt_list[-1]))


def get_retired_email(email, salt_list, retired_email_fmt=RETIRED_EMAIL_DEFAULT_FMT):
    """
    Returns a retired email address based on the original email address
    and all the historical salts, from oldest to current.
    The current salt is assumed to be the last salt in the list.

    Raises :class:`~ValueError` if the salt isn't a list of salts.

    Arguments:
        email (str): Email address of the user to be retired.
        salt_list (list/tuple): List of all historical salts.

    Yields:
        Returns a retired email address based on the original email
        and all the historical salts, including the current salt.
    """
    if not isinstance(salt_list, (list, tuple)):
        raise SALT_LIST_EXCEPTION

    return retired_email_fmt.format(_compute_retired_hash(email, salt_list[-1]))
