from selenium.webdriver.support.select import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR,'*')
        
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f"{star_value}":
                    star_element.click()

    def sort_price_lower_first(self):
        dropdown_sort_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        dropdown_sort_element.click()
        from_lowest_price_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        from_lowest_price_btn.click()
