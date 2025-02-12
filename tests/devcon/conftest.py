# ez headless

import os
import pytest
from dotenv import load_dotenv
from pathlib import Path
from playwright.sync_api import Page

from pages.agenda import Agenda
from pages.home import *
from pages.onboarding_pages import *
from pages.profile_creation import *
from pages.spaces import Spaces
from pages.terms_and_conditions import *
from pages.profile import *

# ------------------------------------------------------------
# Környezeti változók beolvasása
# ------------------------------------------------------------
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Fixture, amely az alapértelmezett környezeti változóból adja vissza az URL-t"""
    return os.getenv("PYTEST_BASE_URL", "https://devcon.buzz")


# ------------------------------------------------------------
# Playwright fixtures
# ------------------------------------------------------------

@pytest.fixture(scope='function')
def page(request, context, browser, base_url) -> Page:
    """Létrehoz egy Playwright oldalt a tesztekhez"""
    reg_marker = request.node.get_closest_marker('registered')
    file_path = Path('.auth/storage.json')

    if reg_marker is not None:
        if not file_path.exists():
            create_auth_file(file_path)
            create_auth_content(browser, base_url)
        context = browser.new_context(storage_state=file_path, base_url=base_url)
    else:
        context = browser.new_context(base_url=base_url)

    return context.new_page()


def create_auth_file(file_path):
    """Létrehoz egy üres autentikációs fájlt"""
    Path('.auth').mkdir(parents=True, exist_ok=True)
    file = open(file_path, 'w+')
    file.write('')
    file.close()


def create_auth_content(browser, base_url):
    """Létrehozza az autentikációs állapotot és elmenti a `.auth/storage.json`-be"""
    page = browser.new_page(base_url=base_url)
    page.goto('profilecreation')
    page.get_by_role('button', name='Start Building Your Community').click()
    page.wait_for_url('home')
    page.context.storage_state(path='.auth/storage.json')
    page.close()


# ------------------------------------------------------------
# DevCon Page Fixtures
# ------------------------------------------------------------

@pytest.fixture(scope='function')
def home(page):
    return Home(page)


@pytest.fixture(scope='function')
def onboard_join(page: Page):
    return Onboard_Join(page)


@pytest.fixture(scope='function')
def onboard_discuss(page: Page):
    return Onboard_Discuss(page)


@pytest.fixture(scope='function')
def onboard_swarm(page: Page):
    return Onboard_Swarm(page)


@pytest.fixture(scope='function')
def onboard_stay(page: Page):
    return Onboard_Stay(page)


@pytest.fixture(scope='function')
def terms_and_conditions(page: Page):
    return Terms_And_Conditions(page)


@pytest.fixture(scope='function')
def profile_creation(page: Page):
    return Profile_Creation(page)


@pytest.fixture(scope='function')
def profile(page: Page):
    return Profile(page)


@pytest.fixture(scope='function')
def agenda(page: Page):
    return Agenda(page)


@pytest.fixture(scope='function')
def spaces(page: Page):
    return Spaces(page)