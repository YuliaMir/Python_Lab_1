'''Создайте таблицу book с полями book_id (int), book_title (text),
book_author (text), publisher_id(int).
Введите несколько книг нескольких авторов.
Сделайте несколько SELECT для выборки книг по авторам, по
названиям.'''

CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    book_title TEXT,
    book_author TEXT,
    publisher_id INT
);


INSERT INTO book (book_title, book_author, publisher_id) VALUES ('Война и мир', 'Толстой', 1);
INSERT INTO book (book_title, book_author, publisher_id) VALUES ('Братья Карамазовы', 'Достоевский', 2);
INSERT INTO book (book_title, book_author, publisher_id) VALUES ('Воскресение', 'Толстой', 3);
INSERT INTO book (book_title, book_author, publisher_id) VALUES ('Мастер и Маргарита', 'Булгаков', 1);
INSERT INTO book (book_title, book_author, publisher_id) VALUES ('Преступление и наказание', 'Достоевский', 2);


SELECT * FROM book WHERE book_author = 'Толстой';
SELECT * FROM book WHERE book_title = 'Преступление и наказание';
