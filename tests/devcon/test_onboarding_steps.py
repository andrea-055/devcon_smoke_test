from playwright.sync_api import Page, expect
from tests.devcon.conftest import *


def test_app_is_accessible(page: Page, onboard_join: Onboard_Join):
    page.goto("/")
    page.wait_for_url(onboard_join.URL)
    expect(onboard_join.header_text).to_have_text(onboard_join.HEADTEXT)
    expect(page).to_have_title("Devcon Buzz")


def test_redirect_unregistered(home: Home, onboard_join: Onboard_Join):
    home.open()
    expect(home.page).to_have_url("")
    home.page.wait_for_selector('button')
    expect(onboard_join.page).to_have_url(onboard_join.URL)


def test_onboarding_steps_normal(
        onboard_join: Onboard_Join,
        onboard_discuss: Onboard_Discuss,
        onboard_swarm: Onboard_Swarm,
        onboard_stay: Onboard_Stay,
        terms_and_conditions: Terms_And_Conditions):
    
    onboard_join.open()
    expect(onboard_join.header_text).to_have_text(onboard_join.HEADTEXT)

    onboard_join.click_next_button()
    expect(onboard_discuss.header_text).to_have_text(onboard_discuss.HEADTEXT)

    onboard_discuss.click_next_button()
    expect(onboard_swarm.header_text).to_have_text(onboard_swarm.HEADTEXT)
    
    onboard_swarm.click_next_button()
    expect(onboard_stay.header_text).to_have_text(onboard_stay.HEADTEXT)
    
    onboard_stay.click_next_button()
    expect(terms_and_conditions.header_text).to_have_text(terms_and_conditions.HEADTEXT)


def test_onboarding_steps_reverse(
        onboard_join: Onboard_Join,
        onboard_discuss: Onboard_Discuss,
        onboard_swarm: Onboard_Swarm,
        onboard_stay: Onboard_Stay,
        terms_and_conditions: Terms_And_Conditions):
    
    terms_and_conditions.open()
    expect(terms_and_conditions.header_text).to_have_text(terms_and_conditions.HEADTEXT)
    
    terms_and_conditions.click_back_button()
    expect(onboard_stay.header_text).to_have_text(onboard_stay.HEADTEXT)

    onboard_stay.click_back_button()
    expect(onboard_swarm.header_text).to_have_text(onboard_swarm.HEADTEXT)

    onboard_swarm.click_back_button()
    expect(onboard_discuss.header_text).to_have_text(onboard_discuss.HEADTEXT)

    onboard_discuss.click_back_button()
    expect(onboard_join.header_text).to_have_text(onboard_join.HEADTEXT)