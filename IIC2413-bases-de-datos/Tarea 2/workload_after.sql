-- Workload for group 3.
-- 100 queries sampled from 12 classes (Q01..Q12).
-- Each query is tagged with its class and an instance index so the
-- runner can aggregate timings by class.
--
-- You may add CREATE INDEX statements to speed these queries up.
-- For the materialization step, you may rewrite individual queries
-- to consume a MATERIALIZED VIEW you create -- but the rewritten
-- query MUST return the same result for the same parameters.

-- ===== 001 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'mystery'
  AND price BETWEEN 15 AND 25
  AND publication_year >= 2022
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 002 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books  
WHERE order_date >= '2022-01-01' AND order_date < '2022-02-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 003 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'Zara.moreno33740@mail.com';

-- ===== 004 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 12383
ORDER BY review_date DESC LIMIT 20;

-- ===== 005 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 19028 AND warehouse_id = 6;

-- ===== 006 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 20125 AND warehouse_id = 5;

-- ===== 007 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'jonas.okafor37801@example.org';

-- ===== 008 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'eero.jensen118484@mail.com';

-- ===== 009 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 20053
ORDER BY review_date DESC LIMIT 20;

-- ===== 010 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2024-11-01' AND order_date < '2024-12-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 011 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 6361
ORDER BY review_date DESC LIMIT 20;

-- ===== 012 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2023-04-01' AND order_date < '2023-05-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 013 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 24501 AND warehouse_id = 1;

-- ===== 014 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Empir%'
ORDER BY title LIMIT 25;

-- ===== 015 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2022-11-01' AND order_date < '2022-12-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 016 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 24897
ORDER BY review_date DESC LIMIT 20;

-- ===== 017 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'wei.larsen160023@shop.net';

-- ===== 018 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'wei.chen46301@shop.net';

-- ===== 019 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'dania.nakamura69819@mail.com';

-- ===== 020 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 7215
ORDER BY review_date DESC LIMIT 20;

-- ===== 021 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 16997
ORDER BY review_date DESC LIMIT 20;

-- ===== 022 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'victor.kowalski67139@mail.com';

-- ===== 023 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'River%'
ORDER BY title LIMIT 25;

-- ===== 024 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 27621
ORDER BY review_date DESC LIMIT 20;

-- ===== 025 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'daniel.GUPTA14921@mail.com';

-- ===== 026 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 11435 AND warehouse_id = 5;

-- ===== 027 =====
SELECT order_id, user_id, order_date, total_amount
FROM orders
WHERE order_date >= '2025-03-01' AND order_date < '2025-04-01'
ORDER BY order_date DESC LIMIT 50;

-- ===== 028 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 6361
ORDER BY review_date DESC LIMIT 20;

-- ===== 029 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2025-04-01' AND order_date < '2025-05-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 030 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'uma.okafor134808@books.io';

-- ===== 031 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 26683
ORDER BY review_date DESC LIMIT 20;

-- ===== 032 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('ROSA.FERREIRA47314@SHOP.NET');

-- ===== 033 =====
SELECT genre, DATE_TRUNC('month', order_date) AS month,
       SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2022-12-01' AND order_date < '2023-12-01'
GROUP BY genre, DATE_TRUNC('month', order_date)
ORDER BY month, revenue DESC;

-- ===== 034 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 7520
ORDER BY review_date DESC LIMIT 20;

-- ===== 035 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 7594
ORDER BY review_date DESC LIMIT 20;

-- ===== 036 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 26150
ORDER BY review_date DESC LIMIT 20;

-- ===== 037 =====
SELECT genre, DATE_TRUNC('month', order_date) AS month,
       SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2022-12-01' AND order_date < '2023-12-01'
GROUP BY genre, DATE_TRUNC('month', order_date)
ORDER BY month, revenue DESC;

-- ===== 038 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('INES.MORENO126822@MAIL.COM');

-- ===== 039 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'farid.tanaka51289@mail.com';

-- ===== 040 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'reference'
  AND price BETWEEN 20 AND 40
  AND publication_year >= 2018
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 041 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'biography'
  AND price BETWEEN 20 AND 25
  AND publication_year >= 2020
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 042 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2022-03-01' AND order_date < '2022-04-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 043 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 8871 AND warehouse_id = 1;

-- ===== 044 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 24184
ORDER BY review_date DESC LIMIT 20;

-- ===== 045 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 26913 AND warehouse_id = 5;

-- ===== 046 =====
SELECT COUNT(*) FROM (
    SELECT book_id FROM reviews
    GROUP BY book_id
    HAVING COUNT(*) >= 10 AND AVG(rating) > 4.0
) sub;

-- ===== 047 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'zara.XU138209@example.org';

-- ===== 048 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 3847
ORDER BY review_date DESC LIMIT 20;

-- ===== 049 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Spark%'
ORDER BY title LIMIT 25;

-- ===== 050 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 7790
ORDER BY review_date DESC LIMIT 20;

-- ===== 051 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'biography'
  AND price BETWEEN 10 AND 30
  AND publication_year >= 2020
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 052 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('BIANCA.VARGAS29989@SHOP.NET');

-- ===== 053 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'greta.vargas164804@books.io';

-- ===== 054 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'fiction'
  AND price BETWEEN 5 AND 40
  AND publication_year >= 2020
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 055 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Daugh%'
ORDER BY title LIMIT 25;

-- ===== 056 =====
SELECT o.order_id, o.user_id, o.order_date, o.total_amount
FROM orders o
JOIN users u ON u.user_id = o.user_id
WHERE u.is_premium = TRUE
  AND o.order_date >= '2024-12-15' AND o.order_date < '2024-12-22'
ORDER BY o.order_date DESC;

-- ===== 057 =====
SELECT genre, DATE_TRUNC('month', order_date) AS month,
      SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2023-12-01' AND order_date < '2024-12-01'
GROUP BY genre, DATE_TRUNC('month', order_date)
ORDER BY month, revenue DESC;

-- ===== 058 =====
SELECT COUNT(*) FROM (
    SELECT book_id FROM reviews
    GROUP BY book_id
    HAVING COUNT(*) >= 10 AND AVG(rating) > 4.0
) sub;

-- ===== 059 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2023-10-01' AND order_date < '2023-11-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 060 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 29608
ORDER BY review_date DESC LIMIT 20;

-- ===== 061 =====
SELECT o.order_id, o.user_id, o.order_date, o.total_amount
FROM orders o
JOIN users u ON u.user_id = o.user_id
WHERE u.is_premium = TRUE
  AND o.order_date >= '2024-03-01' AND o.order_date < '2024-03-08'
ORDER BY o.order_date DESC;

-- ===== 062 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 2397
ORDER BY review_date DESC LIMIT 20;

-- ===== 063 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Last %'
ORDER BY title LIMIT 25;

-- ===== 064 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 12536
ORDER BY review_date DESC LIMIT 20;

-- ===== 065 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('NOAH.JENSEN82368@EXAMPLE.ORG');

-- ===== 066 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2022-06-01' AND order_date < '2022-07-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 067 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 18434
ORDER BY review_date DESC LIMIT 20;

-- ===== 068 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 12210 AND warehouse_id = 1;

-- ===== 069 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'Kiri.petrov1358@example.org';

-- ===== 070 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'scifi'
  AND price BETWEEN 15 AND 25
  AND publication_year >= 2022
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 071 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'tara.zhang100993@mail.com';

-- ===== 072 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'mystery'
  AND price BETWEEN 5 AND 40
  AND publication_year >= 2022
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 073 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('FATIMA.YAMAMOTO123796@EXAMPLE.ORG');

-- ===== 074 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'cyrus.nakamura113798@books.io';

-- ===== 075 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 13480
ORDER BY review_date DESC LIMIT 20;

-- ===== 076 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 8158
ORDER BY review_date DESC LIMIT 20;

-- ===== 077 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'Cyrus.espinoza70866@example.org';

-- ===== 078 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 17870
ORDER BY review_date DESC LIMIT 20;

-- ===== 079 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('LUCA.VARGAS193553@MAIL.COM');

-- ===== 080 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'Maya.davidson46906@books.io';

-- ===== 081 =====
SELECT order_id, user_id, order_date, total_amount
FROM orders
WHERE order_date >= '2022-09-01' AND order_date < '2022-10-01'
ORDER BY order_date DESC LIMIT 50;

-- ===== 082 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2023-12-01' AND order_date < '2024-01-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 083 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 22685
ORDER BY review_date DESC LIMIT 20;

-- ===== 084 =====
SELECT order_id, user_id, order_date, total_amount
FROM orders
WHERE order_date >= '2024-09-01' AND order_date < '2024-10-01'
ORDER BY order_date DESC LIMIT 50;

-- ===== 085 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 6498
ORDER BY review_date DESC LIMIT 20;

-- ===== 086 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Thron%'
ORDER BY title LIMIT 25;

-- ===== 087 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'cyrus.rossi21948@shop.net';

-- ===== 088 =====
UPDATE inventory
SET stock_count = stock_count - 1, last_updated = CURRENT_TIMESTAMP
WHERE book_id = 10065 AND warehouse_id = 1;

-- ===== 089 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('EERO.UEDA185836@EXAMPLE.ORG');

-- ===== 090 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'wei.chen186555@mail.com';

-- ===== 091 =====
SELECT book_id, title, SUM(line_revenue) AS revenue
FROM join_orders_items_books
WHERE order_date >= '2025-04-01' AND order_date < '2025-05-01'
GROUP BY book_id, title
ORDER BY revenue DESC LIMIT 10;

-- ===== 092 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 7774
ORDER BY review_date DESC LIMIT 20;

-- ===== 093 =====
SELECT review_id, user_id, rating, review_text, review_date
FROM reviews
WHERE book_id = 16821
ORDER BY review_date DESC LIMIT 20;

-- ===== 094 =====
SELECT o.order_id, o.user_id, o.order_date, o.total_amount
FROM orders o
JOIN users u ON u.user_id = o.user_id
WHERE u.is_premium = TRUE
  AND o.order_date >= '2024-03-15' AND o.order_date < '2024-03-22'
ORDER BY o.order_date DESC;

-- ===== 095 =====
SELECT book_id, title, price
FROM books
WHERE title LIKE 'Shado%'
ORDER BY title LIMIT 25;

-- ===== 096 =====
SELECT book_id, title, price, publication_year
FROM books
WHERE genre = 'fiction'
  AND price BETWEEN 10 AND 30
  AND publication_year >= 2022
ORDER BY publication_year DESC, price ASC LIMIT 50;

-- ===== 097 =====
SELECT user_id, is_premium
FROM users
WHERE LOWER(email) = LOWER('UMA.IVANOV28836@BOOKS.IO');

-- ===== 098 =====
SELECT order_id, user_id, order_date, total_amount
FROM orders
WHERE order_date >= '2022-03-01' AND order_date < '2022-04-01'
ORDER BY order_date DESC LIMIT 50;

-- ===== 099 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'zara.ivanov81231@shop.net';

-- ===== 100 =====
SELECT user_id, is_premium, country
FROM users
WHERE email = 'jonas.ferreira86776@example.org';
