-- valide resets attribute valide email
CREATE TRIGGER reset_attribute BEFORE UPDATE
ON user 
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email 
    THEN SET NEW.valid_email = 0;
    END IF;
END;