def test_petfriends(driver):
    driver.implicitly_wait(10)

    driver.get('https://petfriends.skillfactory.ru/')

    driver.find_element("xpath", "//button[@onclick=\"document.location='/new_user';\"]").click()
    driver.find_element("xpath", "//a[@href=\"/login\"]").click()
    driver.find_element("id", "email").send_keys("test32@gmail.com")
    driver.find_element("id", "pass").send_keys("test32")
    driver.find_element("xpath", "//button[@type='submit']").click()

    driver.implicitly_wait(10)

    cards = driver.find_elements('css selector', '.card-deck .card')

    for i in range(len(cards)):
        driver.implicitly_wait(10)
        image = cards[i].find_element('xpath', '//img[@class="card-img-top"]').get_attribute('src')
        driver.implicitly_wait(10)
        name = cards[i].find_element('xpath', '//h5[@class="card-title"]').text
        driver.implicitly_wait(10)
        description = cards[i].find_element('xpath', '//p[@class="card-text"]').text

        assert image != ''
        assert name != ''
        assert description != ''
        assert ', ' in description
        parts = description.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
