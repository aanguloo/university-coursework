CREATE MATERIALIZED VIEW join_orders_items_books AS
SELECT o.order_date,
       b.book_id, b.title, b.genre,
       oi.quantity * oi.unit_price AS line_revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN books b        ON b.book_id   = oi.book_id;

