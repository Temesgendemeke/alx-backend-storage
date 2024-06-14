-- trigger that decreases the quantity of an item
-- after adding a new order.

CREATE TRIGGER update_quantity_after_new_order
AFTER INSERT ON order 
FOR EACH ROW
BEGIN
UPDATE items
SET NEW.quantity = OLD.quantity - order.number
END;