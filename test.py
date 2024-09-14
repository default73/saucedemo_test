from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class TestSauceDemoPurchase(unittest.TestCase):

    """
    Создание тестовой среды, запуск браузера, переход на сайт и настройка неявного ожидания
    """
    def setUp(self):
        """
        Создание тестовой среды
        """

        # Настройка опций Chrome
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Запуск браузера с указанными опциями
        self.driver = webdriver.Chrome(options=chrome_options)

        # переход на сайт Sauce Demo.
        self.driver.get('https://www.saucedemo.com/')

        # настройка неявного ожидания
        self.driver.implicitly_wait(10)

        # Увеличение окна браузера до максимума
        self.driver.maximize_window()

    def test_purchase_scenario(self):
        """
        Тестирование сценария покупки
        """
        driver = self.driver

        # Вход в систему под тестовой УЗ
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        # Ожидание появления кнопки добавления в корзину
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'add-to-cart-sauce-labs-backpack'))
        )

        # Добавление товара в корзину
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

        # Проверка наличия товара в корзине
        driver.find_element(By.ID, 'shopping_cart_container').click()
        self.assertEqual(driver.find_element(By.CLASS_NAME, 'inventory_item_name').text, 'Sauce Labs Backpack')

        # Переход к оформлению заказа
        driver.find_element(By.ID, 'checkout').click()

        # Ввод необходимой информации
        driver.find_element(By.ID, 'first-name').send_keys('user')
        driver.find_element(By.ID, 'last-name').send_keys('standard')
        driver.find_element(By.ID, 'postal-code').send_keys('12345')

        # Переход к следующему шагу
        driver.find_element(By.ID, 'continue').click()

        # Завершение покупки
        driver.find_element(By.ID, 'finish').click()

        # Проверка успешного завершения покупки
        self.assertEqual(driver.find_element(By.CLASS_NAME, 'complete-header').text, 'Thank you for your order!')

    def tearDown(self):
        """
        Завершение работы после каждого теста, выходя из экземпляра WebDriver
        """
        # Выход из экземпляра WebDriver
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
