import os
import pytest
import allure
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
from pages.notes import Notes

# Környezeti változók betöltése
load_dotenv()

# Fixture az Allure environment metaadat beállításához
@pytest.fixture(autouse=True, scope="function")
def set_environment_label():
    env_url = os.getenv("PYTEST_BASE_URL", "unknown")
    allure.dynamic.label("environment", env_url)  # Címke a tesztekhez
    # Explicit környezetváltozó hozzáadása az Allure-hoz
    allure.environment("base_url", env_url)
    yield  # Teszt futtatása után visszaadja a vezérlést

# Hook a teszt riportok és screenshotok kezelésére
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Screenshot készítése."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":  # Csak a teszt futtatása végén
        page = item.funcargs.get("page", None)  # "page" fixture ellenőrzése
        if page:
            # Screenshot készítése és csatolása
            screenshot_path = f"reports/allure-results/screenshots/{item.name}_{report.outcome}.png"
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name=f"{item.name}_screenshot", attachment_type=allure.attachment_type.PNG)
            print(f"📸 Screenshot saved and attached: {screenshot_path}")

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("PYTEST_BASE_URL", "https://devcon.buzz")

# Playwright fixtures
@pytest.fixture(scope='function')
def page(request, context, browser, base_url) -> Page:
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
    Path('.auth').mkdir(parents=True, exist_ok=True)
    file = open(file_path, 'w+')
    file.write('')
    file.close()

def create_auth_content(browser, base_url):
    page = browser.new_page(base_url=base_url)
    page.goto('profilecreation')
    page.get_by_role('button', name='Start Building Your Community').click()
    page.wait_for_url('home')
    page.context.storage_state(path='.auth/storage.json')
    page.close()

# DevCon Page Fixtures
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

@pytest.fixture(scope="function")
def notes(page):
    return Notes(page)