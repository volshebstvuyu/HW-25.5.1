# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")

# driver.get('https://petfriends.skillfactory.ru/')
class Pet:
    def __init__(self, photo, name, animalType, age):
        self.photo = photo
        self.name = name
        self.animalType = animalType
        self.age = age


def test_petfriends(driver):
    driver.get('https://petfriends.skillfactory.ru/')
    wait = WebDriverWait(driver, 10)
    # driver.find_element("xpath", "//button[@onclick=\"document.location='/new_user';\"]").click()
    # driver.find_element("xpath", "//a[@href=\"/login\"]").click()
    # driver.find_element("id", "email").send_keys("test32@gmail.com")
    # driver.find_element("id", "pass").send_keys("test32")
    # driver.find_element("xpath", "//button[@type='submit']").click()
    # driver.find_element("xpath", "//a[@href=\"/my_pets\"]").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/login\"]"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("test32@gmail.com")
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("test32")
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"/my_pets\"]"))).click()

    wait.until(EC.title_is('PetFriends: My Pets'))

    # stringCountOfPets = driver.find_element('xpath', "/html/body/div[1]/div/div[1]").text
    stringCountOfPets = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text
    countOfPets = stringCountOfPets.split('\n')[1].split(':')[1].strip()

    # listOfRows =  driver.find_elements("xpath", "//tbody/tr")
    listOfRows =  wait.until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr')))
    assert int(countOfPets) == len(listOfRows)

    petList = []
    listOfPetsName = []

    for i in range(len(listOfRows)):
        petItem = ''
        # rowElements = driver.find_elements('xpath', f'//tbody/tr[{i + 1}]/td')
        rowElements = wait.until(EC.presence_of_all_elements_located((By.XPATH, f'//tbody/tr[{i + 1}]/td')))
        
        itemPhoto = wait.until(EC.presence_of_element_located((By.XPATH, f'//tbody/tr[{i + 1}]/th[@scope="row"]/img'))).get_attribute('src')
    
        itemName = rowElements[0].text.strip()
        itemAnimalType = rowElements[1].text.strip()
        itemAge = rowElements[2].text.strip()

        petItem = Pet(itemPhoto, itemName, itemAnimalType, itemAge)
        petList.append(petItem)
        
        assert itemName != ''
        assert itemAnimalType != ''
        assert itemAge != ''

        listOfPetsName.append(itemName)


    emptyPhotoCount = 0
    for pet in petList:
        if pet.photo == '':
            emptyPhotoCount += 1
        
    assert emptyPhotoCount <= (len(petList) / 2)

    uniquePetsName = list(dict.fromkeys(listOfPetsName))
    assert len(listOfPetsName) == len(uniquePetsName) 

    uniquePets = list(dict.fromkeys(petList))
    assert len(petList) == len(uniquePets)