CREATE INDEX ON reviews (book_id, review_date DESC);
CREATE INDEX ON orders (order_date);
CREATE INDEX ON users (LOWER(email));
CREATE INDEX ON join_orders_items_books (order_date);

