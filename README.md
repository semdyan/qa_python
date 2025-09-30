# qa_python

    Реализованные тесты проверяют, что:

    test_init_is_books_genre_empty_true - при создании объекта словарь books_genre инициализируется пустым 

    test_add_two_matching_books_items_added - add_new_book добавляет более одной книги, если их названия не совпадают

    test_set_book_genre_matching_genre_is_added - set_book_genre добавляет жанр для книги, которая уже есть в books_genre

    test_get_book_genre_book_returns_correct_genre - get_book_genre возвращает корректный жанр, если книга и жанр есть в books_genre

    test_get_book_genre_book_not_found - get_book_genre не возвращает ничего, если в него передана книга, которой нет в books_genre

    test_get_books_with_specific_genre_expected_book_in_list - get_books_with_specific_genre возвращает книгу переданного жанра, которая есть в books_genre

    test_get_books_genre_returns_expected_dict - get_books_genre возвращает корректно заполненный до этого books_genre

    test_get_books_for_children_book_in_list - get_books_for_children возвращает книгу, жанра которой нет в genre_age_rating
 
    test_get_books_for_children_book_not_in_list - get_books_for_children не возвращает книгу, жанр которой в genre_age_rating

    test_add_book_in_favorites_new_book_added - add_book_in_favorites добавлаяет книгу в favorites

    test_delete_book_from_favorites_book_deleted - delete_book_from_favorites удаляет книгу из favorites

    test_get_list_of_favorites_books_returns_correct_list_len - get_list_of_favorites_books возращает favorites корректной длины    