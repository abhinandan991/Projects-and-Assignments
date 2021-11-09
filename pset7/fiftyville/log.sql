--First the crime scene reports were read for the required day, to search for clues related to the henious crime of the theft of the cs50 duck.
select description from crime_scene_reports where day=28 and month=7 and year=2020 and street="Chamberlin Street";

--From the reports it was found that there were three witnesses whose testimonies were recorded and each of their descriptions had a mention of courthouse in them.
--Descriptions by the three witnesses were read to gather information about the thief.
select transcript from interviews where transcript like "%courthouse%";

--From witnesses it was found that the thief had left the courthouse within 10 mins of the theft in a car from the parking lot, he had withdrawn money that day in the morning, from an atm at Fifer street and had called his accomplis for less than a minute and asked them to purchase a ticket for the first flight to leave Fiftyville.

--The courthouse security logs were searched and a table was generated which contained the license plates of all the vehicles that exited within 10 minutes of the theft, but as per witness transcript, only one car had left the parking lot when the theif was spotted in it. So only cars leaving at distinct times were considered. This was done to find the person with whom the license plate is assossiated.
--The call records were searched to generate a list of the callers and recievers on the day and which had a duration of call less than 1 minute. This was done to find the phone number of the thief.
--From atm and bank records account number was generated for which money had been deposited on the same day from atm at fifer street. This was done to find the bank account number of the thief.
--From flights the passport number of all people on the earliest flight from flightville the next day were generated. This was done to find the passport number of the thief.

--From the people table the name of the person for which all of the data intersects is generated.
select * from people where people.id in (select id from people where phone_number in(select phone_calls.caller from phone_calls where year=2020 and month=7 and day=28 and duration<60)) and people.id in (select id from people where people.passport_number in (select passengers.passport_number from passengers where passengers.flight_id=(select flights.id from flights where year=2020 and month=7 and day=29 and origin_airport_id=(select id from airports where city="Fiftyville") and hour=8 and minute=20))) and people.id in (select id from people where license_plate in  (select courthouse_security_logs.license_plate from courthouse_security_logs where day=28 and year=2020 and month=7 and hour=10 and minute between 15 and 25));
--The name generated is Ernest. Ernest is the thief.

--The name of the city from the destination id for the airport for the earliest flight from flightville the next day was generated.
select city from airports where id=(select destination_airport_id from flights where origin_airport_id=(select id from airports where city="Fiftyville") );
--It was found to be London. So the thief would be escaping to London.

--From call records the name of the reciever was checked.
select name from people where people.phone_number=(select receiver from phone_calls where day=28 and year=2020 and month=7 and duration<60 and caller=(select phone_number from people where name="Ernest"));
--The name of the receiver was found to be Berthold, thus he is the accomplice.

