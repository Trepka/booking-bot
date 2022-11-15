import booking.constants as const
from selenium import webdriver
from selenium.webdriver.support.select import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = "C:\SeleniumDrivers\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(driver_path, options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    #exit when bot its own job
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Выберите валюту"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.CSS_SELECTOR, 
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, "xp__guests__toggle")
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR, f'button[aria-label="Взрослых: уменьшить количество"]')
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute("value")
            if int(adults_value) == 1:
                break

        increase_adult_element = self.find_element(By.CSS_SELECTOR, f'button[aria-label="Взрослых: увеличить количество"]')
        for i in range(count-1):
            increase_adult_element.click()

    def click_search(self):
        submit_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()

    def apply_filtrations(self, *star_values):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(star_values)
        filtration.sort_price_lower_first()

    def report_result(self):
        hotel_boxes = self.find_element(By.CSS_SELECTOR, 'div[data-block-id="hotel_list"]')
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_hotels_attributes())
        print(table)
        

    def close_pop_up(self):
        close_popup_btn = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Скрыть меню входа в аккаунт."]')
        close_popup_btn.click()
