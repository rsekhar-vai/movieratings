from unittest.mock import patch
import pytest

from django.contrib.auth import get_user_model

from utils import models

@pytest.mark.django_db
def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

@pytest.mark.django_db
def test_create_user_with_email_successful():
    """Test creating a new user with an email is successful"""
    email = 'test@londonappdev.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    assert user.email == email
    assert user.check_password(password)

@pytest.mark.django_db
def test_new_user_email_normalized():
    """Test the email for a new user is normalized"""
    email = 'test@LONDONAPPDEV.COM'
    user = get_user_model().objects.create_user(email, 'test123')

    assert user.email == email.lower()

@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test creating user with no email raises error"""
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(None, 'test123')

@pytest.mark.django_db
def test_create_new_superuser():
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
        'test@londonappdev.com',
        'test123'
    )

    assert user.is_superuser
    assert user.is_staff

