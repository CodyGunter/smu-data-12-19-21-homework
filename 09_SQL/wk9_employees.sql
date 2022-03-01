CREATE TABLE "departments" (
    "id" Serial  NOT NULL,
    "dept_no" varchar(10)   NOT NULL Unique,
    "dept_name" varchar(30),
    "last_update" timestamp  default localtimestamp NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "dept_emp" (
    "id" Serial NOT NULL,
    "emp_no" Int   NOT NULL,
    "dept_no" varchar(30)   NOT NULL,
    "last_update" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "dept_manager" (
    "id" Serial  NOT NULL,
    "dept_no" varchar(30)   NOT NULL,
    "emp_no" Int   NOT NULL,
    "last_update" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "employees" (
    "id" Serial  NOT NULL,
    "emp_no" INT   NOT NULL Unique,
    "emp_title_id" varchar(30)   NOT NULL,
    "birth_date" varchar(20),
    "first_name" varchar(20)   NOT NULL,
    "last_name" varchar(20)   NOT NULL,
    "sex" varchar(10)   NOT NULL,
    "hire_date" varchar(20)   NOT NULL,
    "last_update" timestamp   default localtimestamp NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "salaries" (
    "id" Serial NOT NULL,
    "emp_no" Int   NOT NULL,
    "salary" Int   NOT NULL,
    "last_update" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "title" (
    "id" Serial NOT NULL,
    "title_id" varchar(20) NOT NULL Unique,
    "title" varchar(30),
    "last_update" timestamp default localtimestamp   NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "title" ("title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

1) Find Employee name, number, and salary 

Select 
	e.emp_no, e.first_name, e.last_name, e.sex, s.salary
from
	employees as e
join salaries as s on e.emp_no=s.emp_no
limit 10;

2) Find employees hired in 1986

Select 
	e.first_name, e.last_name, e.hire_date
from 
	employees e
where
	e.hire_date like '%1986%'
limit 10;

3) Find manager of each department

Select 
	dm.dept_no, d.dept_name, e.emp_no, e.first_name, e.last_name
from 
	dept_manager as dm
join departments as d on dm.dept_no=d.dept_no
join employees as e on dm.emp_no=e.emp_no
limit 10;

4) List employees with department name

Select 
	de.emp_no, e.first_name, e.last_name, d.dept_name
from 
	dept_emp as de
join departments as d on de.dept_no=d.dept_no
join employees as e on de.emp_no=e.emp_no
limit 10;

5) Find employees with the name Hercules B....

Select 
	e.first_name, e.last_name, e.sex
From 
	employees as e
Where 
	e.first_name = 'Hercules'
And e.last_name Like 'B%';

6) Find all employees in the sales department with basic info

Select 
	de.emp_no, e.first_name, e.last_name, d.dept_name
from 
	dept_emp as de
join departments as d on de.dept_no=d.dept_no
join employees as e on de.emp_no=e.emp_no
Where 
	d.dept_name = 'Sales'
limit 10;
	

7) Find employees in the sales and development departments 

Select 
	de.emp_no, e.first_name, e.last_name, d.dept_name
from 
	dept_emp as de
join departments as d on de.dept_no=d.dept_no
join employees as e on de.emp_no=e.emp_no
Where 
	d.dept_name = 'Sales'
	Or d.dept_name = 'Development'
limit 50;

8) In descending order,  count the occurences of last names 
(Reference: '#https://stackoverflow.com/questions/1503959/how-to-count-occurrences-of-a-column-value-efficiently-in-sql')

SELECT 
	last_name, count(last_name)
FROM 
	employees
Group by 
	last_name
ORDER BY 
	count desc 
Limit 50



