select title, 女 gener
from temp_result_2
union 
select title, 男
from temp_result_2
order by title;

create table temp_result_2 as 
select title, 
max(case gender when 'F' then ratings else 0 end) 女,
max(case gender when 'M' then ratings else 0 end) 男
from temp_result 
group by title

select * 
from temp_result
where title in 
(
select title 
from movies
where movie_id in 
(
	select movie_id 
	from ratings
	group by movie_id
	having count(movie_id) >= 250
)
)

create table temp_result as 
select title, gender, avg(ratings) as ratings from (
select users.gender, movies.movie_id, movies.title, ratings.ratings
from users inner join ratings
on users.user_id = ratings.user_id
inner join movies
on ratings.movie_id = movies.movie_id
) a 
group by title, gender 


alter table movies add primary key(movie_id);
alter table users add primary key(user_id);

alter table ratings 
add constraint FK_movie_id foreign key(movie_id) REFERENCES movies(movie_id);

alter table ratings 
add constraint FK_user_id foreign key(user_id) REFERENCES users(user_id);