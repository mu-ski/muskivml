import pytest

from email_validator import validate_email

from virtmulib.applogic import usecases
from virtmulib.applogic.onloader.spotify_onloader import SpotifyOnLoader

def test_login_get_displayname_spotify() -> bool:
	name = usecases.LoginSignup()(SpotifyOnLoader)
	assert name is not None and name != ''

def test_get_user_data_spotify() -> bool:
	usecases.GetUserData()(SpotifyOnLoader)
	assert True
