-- valide resets attribute valide email
CREATE TRIGGER reset_attribute AFTER UPDATE
ON user 
FOR EACH ROW
SET NEW.valid_email = NOT OLD.valid_email;