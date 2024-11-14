import os
from playwright.sync_api import sync_playwright
from variables import VIDEO_DIR, BASE_DIR, TRACE_ZIP, CAPTURE_DIR, WINDOW_SIZE, BROWSER_LAUNCH_TIMEOUT, \
    SLOW_MO_TIME, TEMP_DIR
from dotenv import load_dotenv
from allure_commons._allure import attach
from allure_commons.types import AttachmentType


def save_video(context, scenario):
    context.page.video.save_as(os.path.join(f"{VIDEO_DIR}/{scenario.name}"))
    with open(
            os.path.join(BASE_DIR, context.page.video.path()), "rb"
    ) as video_file:
        attach(
            video_file.read(),
            name=f"Video : {scenario.name}",
            attachment_type=AttachmentType.WEBM,
        )


def save_screenshot(context, scenario):
    if scenario.status == 'passed':
        screenshot_name = "scenarioPassed" + scenario.name + ".png"
        screenshot_dir = TEMP_DIR / "passed_screenshots"
    else:
        screenshot_name = "scenarioFailed" + scenario.name + ".png"
        screenshot_dir = TEMP_DIR / "failed_screenshots"

    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    context.page.screenshot(path=screenshot_path)
    return screenshot_path


def set_browser(context, playwright):
    try:
        browser_type = context.browser
        print(f"Starting browser: {browser_type}")
        if browser_type == "CHROMIUM":
            browser = playwright.chromium.launch(
                headless=False,
                slow_mo=SLOW_MO_TIME,  # slows each action by 10s
                timeout=BROWSER_LAUNCH_TIMEOUT  # browser launch time
            )
        elif browser_type == "FIREFOX":
            browser = playwright.firefox.launch(
                headless=False,
                slow_mo=SLOW_MO_TIME,
                timeout=BROWSER_LAUNCH_TIMEOUT
            )
        elif browser_type == "WEBKIT":
            browser = playwright.webkit.launch(
                headless=False,
                slow_mo=SLOW_MO_TIME,
                timeout=BROWSER_LAUNCH_TIMEOUT
            )
        else:
            raise ValueError("browser type is not supported")
        context.browser_context = browser.new_context(
            ignore_https_errors=True,
            record_video_size=WINDOW_SIZE,
            record_video_dir=VIDEO_DIR
        )
        context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
        context.page = context.browser_context.new_page()
    except:
        raise ValueError("Error starting browser or navigating to the page")


def start_playwright(context):
    playwright = sync_playwright().start()
    set_browser(context, playwright)


def before_all(context):
    load_dotenv()
    context.browser = os.getenv("BROWSER")
    context.target_address = os.getenv("TARGET_ADDRESS")
    print(context.target_address)
    if not context.browser:
        raise ValueError("browser environment variable is not set")
    if not context.target_address:
        raise ValueError("address environment variable is not set")
    CAPTURE_DIR.mkdir(exist_ok=True)
    BASE_DIR.mkdir(exist_ok=True)
    start_playwright(context)


def after_scenario(context, scenario):
    screenshot_path = save_screenshot(context, scenario)
    attach.file(screenshot_path, name="Screenshot_2", attachment_type=AttachmentType.PNG)
    context.browser_context.tracing.stop(path=TRACE_ZIP)
    context.page.close()
    save_video(context, scenario)
    context.browser_context.close()
