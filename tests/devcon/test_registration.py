from datetime import datetime
from playwright.sync_api import expect
from tests.devcon.conftest import *


def test_tc_unconfirmed_restricts_profile_creation(terms_and_conditions: Terms_And_Conditions):
    terms_and_conditions.open()
    expect(terms_and_conditions.next_button).to_be_visible()
    expect(terms_and_conditions.next_button).to_be_disabled()


def test_tc_confirmed_enables_profile_creation(terms_and_conditions: Terms_And_Conditions):
    terms_and_conditions.open()
    expect(terms_and_conditions.next_button).to_be_visible()
    expect(terms_and_conditions.next_button).to_be_disabled()
    terms_and_conditions.switch_tc()
    expect(terms_and_conditions.next_button).to_be_enabled()


def test_profile_creation_is_accessible_directly(profile_creation: Profile_Creation):
    profile_creation.open()
    expect(profile_creation.header_text).to_have_text(profile_creation.HEADTEXT)
    expect(profile_creation.input_name).to_be_visible()
    expect(profile_creation.register_button).to_be_visible()


def test_username_proposal(profile_creation: Profile_Creation):
    profile_creation.open()
    expect(profile_creation.input_name).not_to_be_empty()


def test_register_with_proposed_name(profile_creation: Profile_Creation, home: Home, profile: Profile):
    profile_creation.open()
    profile_creation.register_as()

    expect(home.profile_ico).to_be_visible()
    home.profile_ico.click()

    expect(profile.username).to_have_text(profile_creation.username)


def test_register_with_custom_name(profile_creation: Profile_Creation, home: Home, profile: Profile):
    profile_creation.open()
    now = datetime.now()
    timestamp = now.year.__str__() +now.month.__str__() +now.day.__str__() +now.hour.__str__() + now.minute.__str__()
    profile_creation.register_as('test ' + timestamp)

    expect(home.profile_ico).to_be_visible()
    home.profile_ico.click()

    expect(profile.username).to_have_text(profile_creation.username)