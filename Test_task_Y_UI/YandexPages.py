from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class YandexSeacrhLocators:
    # Локаторы нужных элементов для проверки первого тест-кейса
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")  # поисковик
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button.mini-suggest__button")  # кнопка поиска
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup")  # suggest

    # первая ссылка таблицы результатов по поиску
    LOCATOR_YANDEX_FIRST_ELEMENT = (By.CSS_SELECTOR, 'span.OrganicTitleContentSpan.organic__title')

    # первое слово в suggest
    LOCATOR_YANDEX_SUGGEST_TEXTS = (By.CSS_SELECTOR, "li.mini-suggest__item.mini-suggest__item_type_fulltext")

    # Вкладка "Картинки"
    LOCATOR_YANDEX_PICTURES_TAB = (By.CSS_SELECTOR, "li.navigation__item.navigation__item_name_images")

    # Первая категория в картинках
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.CSS_SELECTOR, "div.PopularRequestList-Item.PopularRequestList-Item_pos_0")

    # Имена категорий
    LOCATOR_YANDEX_NAMES_CATEGORIES = (By.CLASS_NAME, "PopularRequestList-SearchText")

    # Картинки в таблице
    LOCATOR_YANDEX_PICTURES_IN_THE_TABLE = (By.CSS_SELECTOR, "img.serp-item__thumb.justifier__thumb")

    # Открытая картинка
    LOCATOR_YANDEX_PICTURE = (By.CSS_SELECTOR, "img.MMImage-Origin")

    # Стрелки вправо и влево, для просмотра картинок
    LOCATOR_YANDEX_ARROWS = {'right': (By.CLASS_NAME, "CircleButton.CircleButton_type_next"),
                             'left': (By.CLASS_NAME, "CircleButton.CircleButton_type_prev")}


class SearchHelper(BasePage):

    def enter_word(self, word):
        """Поиск по слову"""
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_enter(self):
        """Нажать Enter"""
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2)
        search_field.send_keys(Keys.ENTER)
        time.sleep(1)

    def check_search_field(self):
        """Проверка наличие поисковика"""
        try:
            search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        except:
            return False
        return True

    def check_suggest(self):
        """Проверка suggest"""
        try:
            suggest = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)
        except:
            return False
        return True

    def go_to_link(self):
        """Переход на другую страницу"""
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_ELEMENT, time=2).click()
        handles = self.driver.window_handles
        handle = self.driver.current_window_handle
        for new_handle in handles:
            if new_handle != handle:
                self.driver.switch_to.window(new_handle)
        time.sleep(2)

    def check_pictures_tab(self):
        """Проверка вкладки "Картинки"""
        try:
            pictures_tab = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES_TAB)
        except:
            return False
        return True

    def get_name_category(self):
        """Получить имя первой категории в нижнем регистре"""
        name = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAMES_CATEGORIES)[0]
        return name.text.lower()

    def go_to_category(self):
        """Перети в перву категорию"""
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_CATEGORY).click()

    def get_text_from_search(self):
        """Записать слово в поисковике"""
        text = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST_TEXTS)[0]
        return text.get_attribute('data-text')

    def check_picture(self):
        """Проверить картинку"""
        try:
            picture = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE)
        except:
            return False
        return True

    def get_src_picture(self):
        """Получить src картинки"""
        picture = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE)
        return picture.get_attribute('src')

    def open_the_picture(self, id_picture):
        """Открыть картинку (под нод номером id_picture)"""
        return self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES_IN_THE_TABLE)[id_picture].click()

    def switch_picture(self, direction):
        """Перейти на другую картинку по стрелке"""
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ARROWS[direction]).click()
