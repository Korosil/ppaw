"""A simple pastebin api wrapper."""

import requests


def get_user_id(dev_key, username, password):
    """Return a string with the api user key."""
    data = {'api_dev_key': dev_key,
            'api_user_name': username,
            'api_user_password': password}

    r = requests.post('https://pastebin.com/api/api_login.php', data)

    return r.text


def get_user_details(api_dev_key, api_user_key):
    """Return user details"""
    data = locals()
    data['api_option'] = 'trends'

    r = requests.post('https://pastebin.com/api/api_post.php', data)

    return r.text


def get_trending(dev_key):
    """Return a dictionary with the most trending pastes."""
    data = {
        'api_dev_key': dev_key,
        'api_option': 'trends'}

    r = requests.post('https://pastebin.com/api/api_post.php', data)

    return r.text


def get_archive():
    """Return archive html page."""
    r = requests.get('https://pastebin.com/archive')

    return r.text


def get_raw_paste(paste_id):
    """Return raw text of given paste_id."""
    r = requests.get('https://pastebin.com/raw/' + paste_id)
    return r.text


def create_new_paste(
    api_dev_key,
    api_paste_code,
    api_paste_private=0,
    api_paste_name=None,
    api_paste_expire_date=None,
    api_paste_format=None,
        api_user_key=None):
    """Create a new paste if succesfull return it's url."""
    data = locals()
    data['api_option'] = 'paste'

    # Filter data and remove dictionary None keys.
    filtered_data = {k: v for k, v in data.items() if v is not None}

    r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

    return r.text


def get_user_pastes(api_dev_key, api_user_key, api_results_limit=None):
    """Return a list of user pastes."""
    data = locals()
    data['api_option'] = 'list'

    # Filter data and remove dictionary None keys.
    filtered_data = {k: v for k, v in data.items() if v is not None}

    r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

    return r.text


def delete_user_paste(api_dev_key, api_user_key, api_paste_key):
    """Deletes a paste created by the user."""
    data = locals()
    data['api_option'] = 'delete'

    r = requests.post('https://pastebin.com/api/api_post.php', data)

    return r.text
