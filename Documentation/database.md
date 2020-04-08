#Database Structure
*List of tables and its columns. Everywhere Id is the PRIMARY KEY*

**CustomUser**  
* Id - Int32
* Email - Char 200
* Password (hashed) - Char 200
* Name - Char 200
* Surname - Char 200
* Is_staff - Boolean, marks if user have access to admin panel 
* Is_active - Boolean, marks is he'she a learning student/working prof/doe member 
* Is_doe - Boolean
* Is_student - Boolean
* Is_prof    - Boolean
* Date_joined - Datetime


**Student** *inherits from CustomUser*
* User_id - foreign key to user
* Year of graduation - Int
 
**Professor** *inherits from CustomUser*
* User_id - foreign key to user
* Photo - can be none

**DoE member** *inherits from CustomUser*
* User_id - foreign key to user 
* Photo - can be none

**Course**
* Title - Char 200
* Description -Char 1000
* Is_elective - Boolean

**Teaches**   
*in fact this is relation between course and professor*
* Id - Int32
* Year - Int32
* Prof - foreignKey(prof_id) - Int32
* Course - foreignKey(course_id) - Int32
* Is_fall - Boolean

**Poll**  
* Id - Int32 
* Name - Char200
* Pub_date - Datetime, time the poll was created
* Open_date - Datetime, the time the poll will be visible for students
* Closed_date - Datetime, the time the poll will be closed for students
* Teaches - Int32, id of teaches relation

**Question**  
* Poll - Int32 foreignKey(poll_id) 
* Id -Int32 
* Question Text - Char200

**Answer**
* Id - Int32
* Answer Text - Char200
* Question - Int32 foreignKey(question_id) 
* Voted - points how many times the answer was chosen

**Votes**
* student - Int32 foreignKey(student_id)
* poll - Int32 foreignKey(poll_id)
* voted - Boolean, default False
