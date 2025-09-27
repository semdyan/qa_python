import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_init_is_books_genre_empty_true(self):
        collector = BooksCollector()
        assert len(collector.books_genre) == 0, 'Атрибут books_genre - не пустой'

    def test_add_two_matching_books_items_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2, 'Длина списка books_genre отличается от ожидаемой'

    def test_set_book_genre_matching_genre_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы', 'Добавленный жанр отличается от ожидаемого'

    def test_get_book_genre_book_not_found(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert not collector.get_book_genre('Что делать, если ваш кот хочет вас убить'), 'Для отсутствующей в списке книги, вернулся жанр'

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Мультфильмы']])
    def test_get_books_with_specific_genre_expected_book_in_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert book in collector.get_books_with_specific_genre(genre), 'Ожидаемой книги нет в списке'

    def test_get_books_genre_returns_expected_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы'}, 'books_genre отличается от ожидаемого'

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Шерлок Холмс', 'Детективы']])
    def test_get_books_for_children_book_not_in_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert not book in collector.get_books_for_children(), 'Ожидаемой книги нет в списке books_for_children'

    def test_add_book_in_favorites_new_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books(), 'Ожидаемой книги нет в списке favorites'

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert not 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books(), 'Книга не была удалена'

    def test_get_list_of_favorites_books_returns_correct_list_len(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1, 'Длина списка favorites отличается от ожидаемой'

