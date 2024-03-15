'''Создайте запрос, который находит авторов, у которых только
минимальное количество книг на складе (в таблице book).
Используйте для этого View.'''

CREATE VIEW author_stock_count AS
SELECT a.author_id, a.author_name, COUNT(b.book_id) AS stock_count
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
WHERE b.stock > 0
GROUP BY a.author_id, a.author_name;

WITH min_stock AS (
    SELECT MIN(stock_count) AS min_count
    FROM author_stock_count
)
SELECT author_id, author_name, stock_count
FROM author_stock_count
WHERE stock_count = (SELECT min_count FROM min_stock);
