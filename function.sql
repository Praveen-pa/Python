USE `dbms`;
DROP function IF EXISTS `Customer`;

DELIMITER $$
USE `dbms`$$
CREATE FUNCTION `Customer` (credit decimal(10,2))
RETURNS varchar(20)
deterministic
BEGIN
declare Customer varchar(20);
if credit>50000 then
set Customer='platinum';
elseif (credit>=50000 and credit<=10000) then
set Customer='gold';
elseif credit<10000 then
set Customer='silver';
end if;
return(Customer);
END$$

DELIMITER ;