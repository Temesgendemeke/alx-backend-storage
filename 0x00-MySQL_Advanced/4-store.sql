-- trigger that decreases the quantity of an item
-- after adding a new order.

CREATE TRIGGER update_quantity_after_new_order
AFTER INSERT ON order FOR EACH ROW
UPDATE items
SET quantity = OLD.quantity - NEW.number
WHERE name=NEW.item_name;
