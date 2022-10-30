# qa_python

## Список тестов:
1. test_add_new_book_add_two_books  
Проверка что добавилось именно 2 книги
2. test_add_new_book_default_rating_1  
Проверка что новая книга имеет рейтинг 1 по умолчанию
3. test_add_new_book_add_two_same_books_ratings_length_1  
Проверка что при добавлении двух одинаковых книг будет добавлена только одна
4. test_set_book_rating_more_10_rating_is_default  
Проверка что при установление рейтинга книги больше 10 значение не изменится и будет 1
5. test_get_book_rating_unknown_book_rating_is_none  
Проверка что при запросе рейтинга для несуществующей книги вернется значение None
6. test_get_books_with_specific_rating_get_only_books_with_rating_3  
Проверка что при запросе книг с рейтингом 3 вернутся только такие книги
7. test_get_books_rating_get_rating_dictionary_with_length_1  
Проверка что при запросе списка рейтинга книг вернется только одна существующая книга
8. test_add_book_in_favorites_nonexistent_book_cannot_be_added_to_favorites  
Проверка что при добавлении несуществующей книги в избранное она не добавится
9. test_delete_book_from_favorites_book_is_deleted_from_favorites  
Проверка что при удалении книги из избранного она успешно удаляется
10. test_get_list_of_favorites_books_get_list_with_length_1  
Проверка что при запросе списка избранного возвращается одна добавленная книга