from YandexPages import SearchHelper
import time


def test_yandex_search(browser):
    """Поиск в яндексе"""

    # 1) Зайти на yandex.ru
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()

    # 2) Проверить наличия поля поиска
    assert yandex_main_page.check_search_field()

    # 3) Ввести в поиск Тензор
    yandex_main_page.enter_word("Тензор")

    # 4) Проверить, что появилась таблица с подсказками (suggest)
    assert yandex_main_page.check_suggest()

    # 5) При нажатии Enter появляется таблица результатов поиска
    yandex_main_page.click_on_the_enter()

    # 6) Проверить, что 1 ссылка ведет на сайт tensor.ru
    yandex_main_page.go_to_link()
    assert yandex_main_page.driver.current_url == "https://tensor.ru/"


def test_yandex_picture_new_version(browser):
    """Картинки на яндексе"""

    # 1)Зайти на yandex.ru
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Картинки")
    yandex_main_page.click_on_the_enter()

    # 2) Проверить, что ссылка «Картинки» присутствует на странице
    assert yandex_main_page.check_pictures_tab()

    # 3) Нажать на на ссылку
    yandex_main_page.go_to_link()

    # 4) Проверить, что перешли на url https://yandex.ru/images/
    assert yandex_main_page.driver.current_url == "https://yandex.ru/images/"

    # Запоминаем заранее название категории
    name_category = yandex_main_page.get_name_category()

    # 5) Открыть первую категорию
    yandex_main_page.go_to_category()

    # 6) Проверить, что название категории отображается в поле поиска
    assert name_category == yandex_main_page.get_text_from_search()

    # 7) Открыть 1 картинку
    yandex_main_page.open_the_picture(0)
    time.sleep(3)

    # 8) Проверить, что картинка открылась
    assert yandex_main_page.check_picture()

    # Запоминаем src картинки для будущий проверок
    src_picture = yandex_main_page.get_src_picture()

    # 9) Нажать кнопку вперед
    yandex_main_page.switch_picture('right')
    time.sleep(3)

    # 10) Проверить, что картинка сменилась
    assert src_picture != yandex_main_page.get_src_picture()

    # 11) Нажать кнопку назад
    yandex_main_page.switch_picture('left')
    time.sleep(3)

    # 12) Проверить, что картинка осталась из шага 8
    assert src_picture == yandex_main_page.get_src_picture()
    time.sleep(1)
