from selenium.webdriver.common.by import By
import data
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from data import address_to
from selenium.webdriver.support import expected_conditions


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.CLASS_NAME, 'button.round')
    comfort_button = (By.CSS_SELECTOR, "div.tcard:nth-child(5)>div:nth-child(3)")
    selected_tariff = (By.CLASS_NAME, 'r-sw-label')
    click_number_phone = (By.CLASS_NAME, 'np-text')
    add_number_phone = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    add_phone_code = (By.ID, 'code')
    button_confirm_code = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_method = (By.CLASS_NAME, 'pp-text')
    add_card = (By.CLASS_NAME, 'pp-plus-container')
    card_number = (By.ID, 'number')
    add_code = (By.CSS_SELECTOR, '#code.card-input')
    card_space = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]')
    add_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    message_driver = (By.ID, "comment")
    ask_blanket_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    blanket_check = (By.CSS_SELECTOR, '.r-sw > div > input')
    ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    get_ice = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    reserve_taxi_button = (By.CLASS_NAME, 'smart-button')
    details = (By.CLASS_NAME, 'order-body')
    timer = (By.CLASS_NAME, 'order-header-content')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,address_from, aaddress_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_order_taxi_button(self):
        self.driver.find_element(*self.order_taxi_button).click()
        
    def click_comfort_button (self):
        comfort_element = self.driver.find_element(*self.comfort_button)
        comfort_element.click()

    def get_comfort(self):
        return self.driver.find_element(*self.selected_tariff).text

    def order_taxi_comfort(self):
        self.click_order_taxi_button()
        self.click_comfort_button()

    def click_add_number_phone (self):
        """ Agregar numero de telefono"""
        self.driver.find_element(*self.click_number_phone).click()

    def set_number_phone (self, number_phone):
        self.driver.find_element(*self.add_number_phone).send_keys(number_phone)

    def get_number (self):
        return self.driver.find_element(*self.click_number_phone).text

    def click_next_button (self):
        self.driver.find_element(*self.next_button).click()

    def insert_phone_code(self):
        self.driver.find_element(*self.add_phone_code).send_keys(retrieve_phone_code(self.driver))

    def button_code_confirm(self):
        self.driver.find_element(*self.button_confirm_code).click()

    def add_new_phone_number(self,number_phone):
        self.click_add_number_phone()
        self.set_number_phone(number_phone)
        self.click_next_button()
        self.insert_phone_code()
        self.button_code_confirm()

    def click_payment_method (self):
        """Agregar metodo de pago"""
        self.driver.find_element(*self.payment_method).click()

    def click_add_card (self):
        self.driver.find_element(*self.add_card).click()

    def click_card_number (self):
        self.driver.find_element(*self.card_number).click()

    def set_card_number (self, number_card):
        """ Agregar numero de tarjeta """
        self.driver.find_element(*self.card_number).send_keys(number_card)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def click_add_code (self):
        self.driver.find_element(*self.add_code).click()

    def set_add_code (self, code):
        """Agregar codigo de seguridad """
        self.driver.find_element(*self.add_code).send_keys(code)

    def get_code(self):
        return self.driver.find_element(*self.add_code).get_property('value')

    def click_card_space (self):
        self.driver.find_element(*self.card_space).click()

    def click_add_button (self):
        self.driver.find_element(*self.add_button).click()

    def click_close_button (self):
        self.driver.find_element(*self.close_button).click()

    def add_credit_card(self,number_card,code):
        self.click_payment_method()
        self.click_add_card()
        self.click_card_number()
        self.set_card_number(number_card)
        self.click_add_code()
        self.set_add_code(code)
        self.click_card_space()
        self.click_add_button()
        self.click_close_button()

    def set_message_driver (self, comment):
        self.driver.find_element(*self.message_driver).send_keys(comment)

    def get_message(self):
        return self.driver.find_element(*self.message_driver).get_property('value')

    def click_ask_blanket_scarves (self):
        self.driver.find_element(*self.ask_blanket_scarves).click()

    def get_blanket_switch_state(self):
        return self.driver.find_element(*self.blanket_check).is_selected()

    def click_add_ice_cream(self):
        self.driver.find_element(*self.ice_cream).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.get_ice).text

    def reserve_taxi(self):
        self.driver.find_element(*self.reserve_taxi_button).click()

    def get_order_section(self):
        return self.driver.find_element(*self.details).is_displayed()

    def driver_info(self):
        #time.sleep(20)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.details))
        return self.driver.find_element(*self.timer).is_displayed()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_taxi_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_taxi_comfort()
        assert routes_page.get_comfort() == 'Manta y pañuelos'


    def test_number_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_new_phone_number(data.phone_number)
        assert routes_page.get_number() == data.phone_number

    def test_setup_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert routes_page.get_card_number() == data.card_number
        assert routes_page.get_code() == data.card_code

    def test_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver(data.message_for_driver)
        assert routes_page.get_message() == data.message_for_driver

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ask_blanket_scarves()
        assert routes_page.get_blanket_switch_state() == True

    def test_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_ice_cream()
        routes_page.click_add_ice_cream()
        assert routes_page.get_ice_cream() == '2'

    def test_click_button_reserve_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi()
        assert routes_page.get_order_section()
        WebDriverWait(self.driver,5)

    def test_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.driver_info() == True
        WebDriverWait(self.driver, 5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
