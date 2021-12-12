Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "docs" directory and online at https://docs.djangoproject.com/en/stable/. If you're just getting started, here's how we recommend you read the docs:

First, read docs/intro/install.txt for instructions on installing Django.
Next, work through the tutorials in order (docs/intro/tutorial01.txt, docs/intro/tutorial02.txt, etc.).
If you want to set up an actual deployment server, read docs/howto/deployment/index.txt for instructions.
You'll probably want to read through the topical guides (in docs/topics) next; from there you can jump to the HOWTOs (in docs/howto) for specific problems, and check out the reference (docs/ref) for gory details.
See docs/README for instructions on building an HTML version of the docs.
Docs are updated rigorously. If you find any problems in the docs, or think they should be clarified in any way, please take 30 seconds to fill out a ticket here: https://code.djangoproject.com/newticket

To get more help:

Join the #django channel on irc.libera.chat. Lots of helpful people hang out there. See https://web.libera.chat if you're new to IRC.
Join the django-users mailing list, or read the archives, at https://groups.google.com/group/django-users.
To contribute to Django:

Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for information about getting involved.
To run Django's test suite:

Follow the instructions in the "Unit tests" section of docs/internals/contributing/writing-code/unit-tests.txt, published online at https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests
Supporting the Development of Django
Django's development depends on your contributions.

If you depend on Django, remember to support the Django Software Foundation: https://www.djangoproject.com/fundraising/

Instructions Seed Database.
1.- Create your database on postgresql and put the following commands

CREATE DATABASE ravn-back;
\connect ravn-back;

CREATE TABLE authors (
  id serial PRIMARY KEY,
  name text,
  date_of_birth timestamp
);
						
CREATE TABLE books (
  id serial PRIMARY KEY,
  author_id integer REFERENCES authors (id),
  isbn text
);
						
CREATE TABLE sale_items (
  id serial PRIMARY KEY,
  book_id integer REFERENCES books (id),
  customer_name text,
  item_price money,			
  quantity integer
);	

2.- Seed the database with the following commands: 

#Table Authors 

INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (1, 'Lorelai Gilmore', '1968-04-25 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (2, 'Agatha Mary Clarissa Miller', '1890-09-15 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (3, 'Emily Carrillo', '1931-07-21 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (4, 'Robin Sanchez', '2016-07-07 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (5, 'Walter Alvarado', '1954-03-03 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (6, 'Antonio Hall DDS', '1929-04-16 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (7, 'Lindsey Grimes', '2010-02-10 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (8, 'Mark Robertson', '1983-01-26 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (9, 'William Perkins', '1933-02-21 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (10, 'Lisa Santiago', '1984-05-23 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (11, 'Charles Brooks', '2020-06-18 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (12, 'Craig Davis', '1989-04-03 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (13, 'Brent Esparza', '1912-10-06 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (14, 'Brittany Fuentes', '1918-07-08 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (15, 'Jessica Sims DDS', '1906-03-10 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (16, 'Marissa Smith', '1986-05-29 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (17, 'Stanley Smith', '1930-04-22 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (18, 'Michelle Everett', '1996-10-17 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (19, 'Sheila Mitchell', '1940-03-14 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (20, 'Shelly Henry', '1947-01-10 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (21, 'Joseph Grant', '1960-10-13 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (22, 'Kelly Garcia', '1962-06-17 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (23, 'Chelsea Garcia', '2017-09-25 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (24, 'Nicole Robertson', '1974-01-24 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (25, 'Kelly Golden', '2018-08-01 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (26, 'Courtney Adkins', '1906-04-17 00:00:00');
INSERT INTO "public"."authors" ("id", "name", "date_of_birth") VALUES (27, 'Kelli Boyle', '1908-07-16 00:00:00');

#table Books

INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (1, 14, '0-226-28500-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (2, 1, '0-553-32548-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (3, 12, '1-56655-944-8');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (4, 18, '1-340-78506-4');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (5, 21, '0-7768-0967-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (6, 1, '0-89370-405-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (7, 9, '0-659-89504-8');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (8, 25, '1-990923-04-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (9, 19, '1-4149-9026-X');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (10, 22, '0-298-83700-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (11, 23, '1-60624-648-8');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (12, 18, '1-80483-303-7');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (13, 19, '0-939261-65-0');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (14, 24, '1-200-71029-0');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (15, 20, '1-107-10610-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (16, 5, '1-08-993861-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (17, 5, '1-5424-7369-1');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (18, 3, '1-228-87006-3');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (19, 5, '0-7112-8929-8');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (20, 13, '0-525-78241-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (21, 8, '0-288-37450-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (22, 20, '0-00-639760-3');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (23, 13, '1-121-01044-X');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (24, 5, '1-221-44722-X');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (25, 5, '1-4468-9544-0');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (26, 7, '0-465-88973-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (27, 18, '1-950298-77-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (28, 18, '1-01-310611-3');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (29, 26, '0-915016-94-X');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (30, 14, '1-83280-953-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (31, 11, '0-223-53505-2');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (32, 27, '1-234-37836-1');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (33, 10, '0-305-35770-0');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (34, 26, '0-18-245591-2');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (35, 20, '1-4295-0509-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (36, 6, '0-7428-7562-8');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (37, 2, '0-10-915615-3');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (38, 15, '1-01-593082-4');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (39, 10, '0-9750033-6-4');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (40, 9, '1-4017-8293-0');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (41, 10, '0-19-578553-3');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (42, 14, '1-894077-67-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (43, 10, '0-85917-061-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (44, 4, '0-495-91340-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (45, 13, '0-695-34610-5');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (46, 19, '1-01-143615-9');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (47, 21, '0-235-92048-7');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (48, 2, '1-04-072053-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (49, 4, '0-88975-055-6');
INSERT INTO "public"."books" ("id", "author_id", "isbn") VALUES (50, 18, '0-18-878536-1');

#table sale_items

INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (1, 9, 'Jeffery Martin', 'S/ 43.00', 3);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (2, 10, 'Jeffrey Hodges', 'S/ 129.00', 14);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (3, 26, 'Victoria Smith', 'S/ 121.00', 7);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (4, 17, 'Kimberly Daniel', 'S/ 97.00', 6);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (5, 21, 'Kimberly Howard', 'S/ 140.00', 5);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (6, 6, 'Elijah Hamilton', 'S/ 17.00', 19);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (7, 23, 'Ryan Chung', 'S/ 75.00', 4);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (8, 18, 'Michelle Rodriguez', 'S/ 53.00', 4);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (9, 13, 'Jillian Smith', 'S/ 34.00', 20);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (10, 3, 'Teresa Thompson', 'S/ 21.00', 11);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (11, 5, 'Amber Davis', 'S/ 116.00', 17);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (12, 11, 'Anthony Thompson', 'S/ 117.00', 18);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (13, 17, 'Henry Hopkins', 'S/ 133.00', 1);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (14, 19, 'Andrea Phillips', 'S/ 20.00', 10);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (15, 22, 'Heather Adkins', 'S/ 69.00', 11);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (16, 9, 'Melanie Bryant', 'S/ 30.00', 17);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (17, 26, 'Teresa Jackson', 'S/ 27.00', 3);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (18, 5, 'Jessica Johnson', 'S/ 15.00', 7);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (19, 8, 'Lisa Briggs', 'S/ 52.00', 15);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (20, 10, 'Shawn Clay', 'S/ 55.00', 18);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (21, 25, 'Eric Soto DDS', 'S/ 69.00', 14);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (22, 4, 'Mrs. Jessica Thompson', 'S/ 41.00', 8);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (23, 6, 'Chad Castillo', 'S/ 100.00', 20);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (24, 13, 'Veronica Martin', 'S/ 85.00', 15);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (25, 5, 'Jamie Neal', 'S/ 131.00', 7);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (26, 5, 'Cassandra Walter', 'S/ 37.00', 16);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (27, 25, 'Jordan Santana', 'S/ 120.00', 8);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (28, 21, 'Robert Nguyen', 'S/ 56.00', 14);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (29, 17, 'Kathryn Johnson', 'S/ 70.00', 14);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (30, 6, 'Michelle Boyd', 'S/ 138.00', 4);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (31, 5, 'Brian Adkins', 'S/ 70.00', 10);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (32, 25, 'Jeremy Hill', 'S/ 41.00', 7);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (33, 18, 'Michael Carter', 'S/ 144.00', 16);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (34, 19, 'Jeffrey Vazquez', 'S/ 23.00', 8);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (35, 9, 'Michael Nguyen', 'S/ 130.00', 13);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (36, 22, 'John Davila', 'S/ 86.00', 18);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (37, 17, 'Travis Miller', 'S/ 39.00', 8);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (38, 17, 'Robert Hill', 'S/ 72.00', 16);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (39, 4, 'Jennifer Rivera', 'S/ 95.00', 2);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (40, 25, 'Carol Warren', 'S/ 17.00', 11);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (41, 4, 'Chad Dunn', 'S/ 140.00', 5);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (42, 16, 'Alicia Scott', 'S/ 18.00', 15);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (43, 19, 'Paula Hall', 'S/ 63.00', 18);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (44, 27, 'Sandra Jimenez', 'S/ 135.00', 3);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (45, 14, 'Miss Sandra Jimenez', 'S/ 93.00', 13);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (46, 17, 'Kayla Higgins', 'S/ 85.00', 19);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (47, 8, 'Eileen Hoover', 'S/ 132.00', 4);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (48, 6, 'Travis Gray', 'S/ 68.00', 8);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (49, 2, 'Christopher Clay', 'S/ 144.00', 1);
INSERT INTO "public"."sale_items" ("id", "book_id", "customer_name", "item_price", "quantity") VALUES (50, 17, 'Carrie Bowman', 'S/ 112.00', 4);

1.- Challenge SQL
1.1.-Who are the first 10 authors ordered by date_of_birth?

SELECT * from authors ORDER BY date_of_birth asc limit 10

1.2. What is the sales total for the author named “Lorelai Gilmore”?

SELECT au."id",au."name" as "author",sum(sale_items.item_price) as "sales_total" FROM authors as au 
inner join books on books."author_id"=au."id"
inner join sale_items on books."id"=sale_items.book_id
where au."name"='Lorelai Gilmore'
GROUP BY au."id",au."name"
ORDER BY au."name" ASC

1.3 What are the top 10 performing authors, ranked by sales revenue?

SELECT au."id",au."name" as "author",sum(sale_items.item_price) as "sales_total" FROM authors as au 
inner join books on books."author_id"=au."id"
inner join sale_items on books."id"=sale_items.book_id
GROUP BY au."id",au."name"
ORDER BY sales_total DESC
limit 10

