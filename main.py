import asyncio

from playwright.async_api import async_playwright

from config import TEST_URL, DIAG_CODE, PASSWORD, HOURS_TIMEOUT


class Diag:
    def __init__(self, diag_url: str, diag_code: str, password: str, headless: bool = False) -> None:
        self.diag_url = diag_url
        self.diag_code = diag_code
        self.password = password
        self.headless = headless

    async def start_diag(self) -> None:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=self.headless)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(self.diag_url)
        await page.wait_for_selector(".auth2")
        await page.fill('input[id="login"]', self.diag_code)
        await page.fill('input[id="password"]', self.password)
        await page.locator("button").click()

        await page.wait_for_selector(".class2")
        await page.click('//button[contains(text(), "Далее")]')


async def main():
    # try:
    diag = Diag(
        diag_url=TEST_URL,
        diag_code=DIAG_CODE,
        password=PASSWORD
    )
    await diag.start_diag()
    # except:
    #     print("Error while diag testing")

    await asyncio.sleep(HOURS_TIMEOUT*60*60)


if __name__ == '__main__':
    asyncio.run(main())
