'''Вывести содержимое таблицы book, при этом авторов
отсортировать по возрастанию, а цены книг по убыванию'''

SELECT b.book_title, a.author_name, b.book_price
FROM book_table b
JOIN author_table a ON b.author_id = a.author_id
ORDER BY b.book_title ASC, b.book_price DESC;

