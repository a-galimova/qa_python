from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_default_rating_1(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name=name)

        assert collector.get_book_rating(name=name) == 1

    def test_add_new_book_add_two_same_books_ratings_length_1(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name=name)
        collector.add_new_book(name=name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_more_10_rating_is_default(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name=name)
        collector.set_book_rating(name=name, rating=20)

        assert collector.get_book_rating(name=name) == 1

    def test_get_book_rating_unknown_book_rating_is_none(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        nonexistent_name = 'Неизвестная книга'
        collector.add_new_book(name=name)

        assert collector.get_book_rating(name=nonexistent_name) is None

    def test_get_books_with_specific_rating_get_only_books_with_rating_3(self):
        collector = BooksCollector()

        first_book = 'Гордость и предубеждение и зомби'
        second_book = 'Что делать, если ваш кот хочет вас убить'
        third_book = 'Война и мир'
        collector.add_new_book(name=first_book)
        collector.add_new_book(name=second_book)
        collector.add_new_book(name=third_book)

        collector.set_book_rating(name=first_book, rating=3)

        assert len(collector.get_books_with_specific_rating(rating=3)) == 1

    def test_get_books_rating_get_rating_dictionary_with_length_1(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name=name)

        assert len(collector.get_books_rating()) == 1

    def test_add_book_in_favorites_nonexistent_book_cannot_be_added_to_favorites(self):
        collector = BooksCollector()

        name = 'Гордость и предубеждение и зомби'
        nonexistent_name = 'Неизвестная книга'
        collector.add_new_book(name=name)
        collector.add_book_in_favorites(name=nonexistent_name)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_is_deleted_from_favorites(self):
        collector = BooksCollector()

        first_book = 'Гордость и предубеждение и зомби'
        second_book = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(name=first_book)
        collector.add_new_book(name=second_book)
        collector.add_book_in_favorites(name=first_book)
        collector.add_book_in_favorites(name=second_book)

        collector.delete_book_from_favorites(name=first_book)

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert favorites[0] == second_book

    def test_get_list_of_favorites_books_get_list_with_length_1(self):
        collector = BooksCollector()

        first_book = 'Гордость и предубеждение и зомби'
        second_book = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(name=first_book)
        collector.add_new_book(name=second_book)
        collector.add_book_in_favorites(name=first_book)

        assert len(collector.get_list_of_favorites_books()) == 1
