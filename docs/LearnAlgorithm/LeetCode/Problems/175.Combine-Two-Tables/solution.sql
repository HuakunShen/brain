-- Runtime: 346 ms, faster than 91.11% of MySQL online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
select FirstName, LastName, City, State
from Person left join Address using(PersonId)