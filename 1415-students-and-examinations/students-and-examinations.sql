# Write your MySQL query statement below
select s.student_id, s.student_name, ss.subject_name, count(e.subject_name) as attended_exams
from Students s
join Subjects ss
left join Examinations e on e.student_id=s.student_id and e.subject_name=ss.subject_name
group by 1,2,3
order by 1,3
