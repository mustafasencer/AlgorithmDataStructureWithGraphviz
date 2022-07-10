"""
https://helokarma.com/2021/04/27/codility-test-challenge-2/
"""


def solve():
    """
        create database test

    create table teams
    (
        team_id   integer     not null,
        team_name varchar(30) not null,
        unique (team_id)
    );

    create table matches
    (
        match_id    integer not null,
        host_team   integer not null,
        guest_team  integer not null,
        host_goals  integer not null,
        guest_goals integer not null,
        unique (match_id)
    );




    CREATE TABLE candidates AS
    Select 'junior' AS position, 5000 AS salary
    Union All
    Select 'junior' AS position, 7000 AS salary
    Union All
    Select 'junior' AS position, 7000 AS salary
    Union All
    Select 'senior' AS position, 10000 AS salary
    Union All
    Select 'junior' AS position, 10000 AS salary
    Union All
    Select 'senior' AS position, 20000 AS salary
    Union All
    Select 'senior' AS position, 30000 AS salary;


    with cteWindowSum as
             (SELECT position, salary, SUM(salary) OVER (PARTITION BY position ORDER BY salary ASC) AS window_sum
              FROM candidates)

     select * from cteWindowSum


    cte as (SELECT
           position,
        COUNT(position) filter (where position = 'junior') AS junior,
        COUNT(position) filter (where position = 'senior') AS senior
    from (SELECT position, salary, SUM(salary) OVER (ORDER BY position DESC, salary ASC) AS window_sum
          FROM (SELECT position, salary, SUM(salary) OVER (PARTITION BY position ORDER BY salary ASC) AS sun_sum
                FROM (
                         SELECT position, salary
                         FROM cteWindowSum
                         WHERE window_sum < 50000
                         ORDER BY position DESC) as p) as r) as q
    WHERE window_sum <= 50000
    GROUP BY position),

    cte1 as (select cast(1 as text) as id, coalesce(junior, 0) as junior from cte
    where junior != 0),

    cte2 as (select cast(1 as text) as id, coalesce(senior, 0) as senior from cte
    where senior != 0)


    select cte1.junior as junior, cte2.senior as senior from cte1
    inner join cte2
    on cte1.id = cte2.id


        :return:
    """


if __name__ == "__main__":
    solve()
