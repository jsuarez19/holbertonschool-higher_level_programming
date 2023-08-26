-- lists all cities contained in the database hbtn_0d_usa
-- multiple selection
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id;