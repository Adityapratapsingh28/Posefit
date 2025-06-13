


<a name="_hlk197108004"></a> 
# <a name="_hlk197108371"></a>            **POSEFIT: YOUR PERSONALIZED PATH TO TOTAL WELLNESS**
21CSC205P Database Management Systems 

MINI PROJECT REPORT 

#### `                                         `*Submitted by*
Shubam Sarawagi[RA2311026010382]

` `Sai Ganeshan M[RA2311026010426]

Aditya Pratap Singh[RA2311026010429]
#### *                                                             
#### `                                                               `*Under the Guidance of*
## `                                      `Beaulah Jeyavathana R
(Associate professor, Computational Intelligence)
### <a name="_hlk197108275"></a>*in partial fulfillment of the requirements* *for the degree    of*
## BACHELOR OF TECHNOLOGY
## in
## COMPUTER SCIENCE ENGINEERING
## with specialization in ARTIFICIAL  INTELLIGENCE AND MACHINE LEARNING
![A blue and white logo

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.001.jpeg)


## DEPARTMENT OF NETWROKING AND COMMUNICATIONS
## SCHOOL OF COMPUTING
## COLLEGE OF ENGINEERING AND TECHNOLOGY
SRM INSTITUTE OF SCIENCE AND TECHNOLOGY
## KATTANKULATHUR- 603 203
### `                                                  `MAY 2025



# ![Logo](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.002.jpeg)
#
# SRM INSTITUTE OF SCIENCE AND TECHNOLOGY KATTANKULATHUR – 603 203

## BONAFIDE CERTIFICATE


Certified that Project report titled “**POSEFIT: YOUR PERSONALIZED PATH TO TOTAL WELLNESS**” is the bonafide work of “**CHHAVI TATER [RA2311026010724], PRAGYA HUNDIA[RA2311026010740]”** who carried out the **21CSC205P Database Management Systems** mini project work under my supervision. 










**Beaulah Jeyavathana R                                                                Dr. R. Annie Uthra**

**COURSE FACULTY                                                                   PROFESSOR &HEAD**

Associate Professor                                                                         Department of

Department Of                                                                                      Computational Intelligence

`   `Computational Intelligence



#####               






**ABSTRACT**

PoseFit is a modern health and wellness platform built to help people stay fit—physically, mentally, and emotionally. Whether you're just starting your fitness journey or you're already deep into it, PoseFit offers personalized tools to support your goals. Using advanced technology like OpenCV and MediaPipe, our Pose Analysis feature gives real-time feedback on your workout form to help you move better and stay injury-free. For nutrition and fitness advice, our AI chatbots (powered by Groq LLaMA 4) provide customized plans and tips tailored just for you.

But fitness isn’t just about the body—it’s also about the mind. That’s why our Mental Wellness section includes handpicked YouTube videos for meditation, yoga, and mindfulness practices, along with the option to book a session with an expert when you need a little extra support. To keep things fun and motivating, PoseFit includes daily challenges that reward you with points when you complete them. And if you’ve had injuries in the past, you can easily track them in the Injury History section to better understand your recovery and progress.

PoseFit brings everything together in one place to help you live a healthier, more balanced life.










#

#
# **Table of Contents:**



|Chapter No|Chapter Name|Page No|
| :- | :- | :- |
|1\.|Problem understanding, Identification of Entity and Relationships, Construction of DB using ER Model for the project|5|
|2\.|Design of Relational Schemas, Creation of Database Tables for the project.|10|
|3\.|Complex queries based on the concepts of constraints, sets, joins, views, Triggers and Cursors.|17|
|4\.|Analyzing the pitfalls, identifying the dependencies, and applying normalizations|53|
|5\.|Implementation of concurrency control and recovery mechanisms|72|
|6\.|Code for the project|57|
|7\.|Result and Discussion (Screen shots of the implementation with front end.)|71|






**PoseFit: Your Personalized Path to Total Wellness**

This report presents a detailed overview of PoseFit, a comprehensive health and wellness platform designed to support users in achieving their fitness, nutrition, and mental well-being goals. The objective of PoseFit is to provide a personalized, AI-powered ecosystem that guides users through physical workouts, balanced nutrition plans, mindfulness practices, and injury tracking—all in one place.

In today’s increasingly health-conscious environment, individuals seek accessible and reliable tools to manage their overall wellness. PoseFit addresses this need by combining advanced pose analysis technology, intelligent chatbots, wellness content, and gamified challenges. This report elaborates on the platform's design, key features, and the benefits it offers to users pursuing a healthier lifestyle through structured and engaging digital solutions.

PoseFit includes core components such as real-time Pose Analysis using OpenCV and MediaPipe, an AI-powered Nutrition Chatbot and Fitness Plan Chatbot built on Groq LLaMA 4, and a Mental Wellness module featuring curated YouTube video content and expert consultation booking. Additionally, it offers a Daily Challenges feature to motivate users through reward points, and an Injury History log for tracking and managing physical setbacks. These integrated functionalities are designed to create a seamless, user-centric experience that promotes consistent progress and well-being.

This report will explore the platform architecture, technical stack, and the practical impact of combining AI and health tracking tools into a single user-friendly system.







**Problem Statement:**

In today’s fast-paced and digitally driven world, maintaining a balanced and healthy lifestyle has become increasingly challenging. Individuals often struggle with fragmented fitness resources—juggling separate apps for workouts, nutrition guidance, mental wellness, and injury tracking. This lack of integration leads to inconsistent user engagement, limited personalization, and poor adherence to wellness routines.

Moreover, many fitness platforms lack real-time feedback on physical form, resulting in improper exercise execution and a higher risk of injury. Similarly, generalized diet and workout plans fail to meet individual needs, while mental wellness support is often overlooked or not easily accessible. The absence of a unified, intelligent system that caters to the complete spectrum of wellness—physical, nutritional, and mental—creates a gap in the user’s fitness journey.

PoseFit addresses this problem by providing an all-in-one platform that combines pose analysis, AI-powered fitness and nutrition chatbots, mental wellness support, gamified challenges, and injury tracking. By centralizing these essential components, PoseFit empowers users to take control of their health with personalized, data-driven, and engaging tools—bridging the gap between technology and holistic well-being.









**ENTITY – RELATIONSHIP MODEL**

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.003.jpeg)

Figure 2.1: ER Diagram of PoseFit

The ER (Entity-Relationship) diagram illustrates the comprehensive database structure of PoseFit that supports users in achieving their health goals through various interconnected modules. The core of the diagram revolves around the **USERS** entity, with numerous supporting entities capturing different aspects of user activity and system functionality.

**1. USERS**

This is the central entity in the diagram.

Attributes: user\_id (Primary Key), name, email, password, gender, age, height, weight.

Relationships:

Connected to all other modules through foreign keys like user\_id.

Supports many-to-one or one-to-many relationships with various activity logs.

**2. POSE\_ANALYSIS**

Tracks user posture analysis using pose\_id and associated data.

Attributes: pose\_id, user\_id, time\_stamp, pose\_score, feedback.

**3. NUTRITION\_PLANS**

Stores nutrition-related information.

Attributes: plan\_id, user\_id, calories\_target, created\_on.

Connected to Users via user\_id.

**4. SLEEP\_TRACKING**

Logs user sleep data.

Attributes: sleep\_id, user\_id, sleep\_duration, sleep\_quality, date.

**5. WATER\_INTAKE**

Monitors daily water consumption.

Attributes: entry\_id, user\_id, amount, date.

**6. CHATBOT\_INTERACTIONS**

Captures interactions with AI chatbots.

Attributes: interaction\_id, user\_id, query\_text, response\_text, timestamp.

**7. MENTAL\_WELLNESS**

Focuses on the user's mental health activities.

Attributes: session\_id, user\_id, stress\_level, mood, meditation\_done.

**8. WORKOUT\_PLANS**

Defines structured workout routines.

Attributes: plan\_id, name, duration, goal, difficulty\_level, exercise\_list.

**9. CHALLENGES**

Tracks participation in fitness challenges.

Attributes: challenge\_id, user\_id, challenge\_type, start\_date, end\_date, reward\_points.

**10. INJURY\_HISTORY**

Logs any user-reported injuries.

Attributes: injury\_id, user\_id, injury\_type, recovery\_status, date.

**11. HEART\_RATE\_MONITOR**

Records heart rate measurements.

Attributes: record\_id, user\_id, timestamp, heart\_rate.

**12. NOTIFICATION\_REMINDERS**

Stores notification data for users.

Attributes: notif\_id, user\_id, title, content, date, time.

**13. WORKOUT\_PROGRESS**

Tracks user performance over time.

Attributes: progress\_id, user\_id, date, weight\_lifted, reps, sets, calories\_burned, notes.

**Relationships Overview**

All modules are linked to the USERS table using user\_id as a foreign key, indicating a one-to-many relationship.

Activity logs such as sleep, water intake, heart rate, workouts, and challenges are designed for frequent updates.

The structure allows scalability for personalized data tracking and recommendations.

The ER diagram provides a modular and normalized database structure for a comprehensive fitness and wellness application. It ensures seamless user data integration across various health domains, supporting personalized experiences, analytical insights, and goal-oriented progress tracking.









**DATABASE SCHEMA(Relational Model)**

The database schema based on the ER model includes:

1. Users (user\_id, name, email, password, weight, age, gender)
1. Workout\_Plans (plan\_id, user\_id, plan\_name, exercise\_list, difficulty\_level, goal, duration)
1. Workout\_Progress (progress\_id, user\_id, plan\_id, exercise\_name, sets, reps, weight\_used, completion\_status, date)
1. Nutrition\_Plans (plan\_id, user\_id, calorie\_intake, protein)
1. Sleep\_Tracking (sleep\_id, user\_id, sleep\_duration, sleep\_quality)
1. Water\_Intake (water\_id, user\_id, amount, timestamp)
1. Pose\_Analysis (pose\_id, user\_id, exercise\_name, exercise\_score, feedback, time\_stamp)
1. Heart\_Rate\_Monitor (monitor\_id, user\_id, heart\_rate, timestamp)
1. Challenges (challenge\_id, user\_id, challenge\_name, start\_date, end\_date, reward\_points)
1. Injury\_History (injury\_id, user\_id, injury\_type, recovery\_status)
1. Mental\_Wellness (assessment\_id, user\_id, water\_id, injury\_id, stress\_level, mood)

Implementation Considerations:

- Primary Keys (PK) ensure each record is uniquely identifiable.
- Foreign Keys (FK) establish relationships between the users table and other modules like workout, nutrition, and mental health.
- Normalization ensures data is structured efficiently, avoiding redundancy and improving maintainability.

Indexing is applied to frequently queried fields like user\_id and date to enhance search performance.

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.004.png)

Figure 3.1: Relational Database Diagram

**ENTITY AND ATTRIBUTES**

**1. USERS**

The central table storing user profile information.

Fields:

- user\_id (Primary Key): Unique identifier for each user.
- name, email, password: Basic authentication and identity data.
- weight, age: Numeric health metrics.
- gender: ENUM representing user gender.

**2. WORKOUT\_PLANS**

Contains structured fitness plans assigned to users.

Fields:

- plan\_id (Primary Key), user\_id (Foreign Key)
- plan\_name, exercise\_list, goal
- difficulty\_level: ENUM type (e.g., Beginner, Intermediate, Advanced)
- duration: Plan duration in minutes.

**3. WORKOUT\_PROGRESS**

Tracks a user’s progress on their workout plans.

Fields:

- progress\_id (Primary Key), user\_id, plan\_id (Foreign Keys)
- exercise\_name, sets, reps, weight\_used
- completion\_status: VARCHAR
- date: Date of activity.

**4. NUTRITION\_PLANS**

Stores nutritional targets for each user.

Fields:

- plan\_id (Primary Key), user\_id (Foreign Key)
- calorie\_intake, protein: Nutritional metrics.

**5. SLEEP\_TRACKING**

Logs sleep-related data.

Fields:

- sleep\_id (Primary Key), user\_id (Foreign Key)
- sleep\_duration: In hours.
- sleep\_quality: ENUM (e.g., Poor, Average, Good).

**6. WATER\_INTAKE**

Tracks daily water consumption.

Fields:

- water\_id (Primary Key), user\_id (Foreign Key)
- amount: In liters.
- timestamp: Date and time of the log.

**7. POSE\_ANALYSIS**

Captures pose analysis results.

Fields:

- pose\_id (Primary Key), user\_id (Foreign Key)
- exercise\_name, exercise\_score: Quantitative posture score.
- feedback: Textual analysis.
- time\_stamp: Datetime of session.

**8. HEART\_RATE\_MONITOR**

Logs heart rate data in real-time.

Fields:

- monitor\_id (Primary Key), user\_id (Foreign Key)
- heart\_rate: BPM (beats per minute).
- timestamp: When the reading was taken.

**9. CHALLENGES**

Tracks user participation in fitness challenges.

Fields:

- challenge\_id (Primary Key), user\_id (Foreign Key)
- challenge\_name, start\_date, end\_date
- reward\_points: Earned upon completion.

**10. INJURY\_HISTORY**

Keeps record of past injuries.

Fields:

- injury\_id (Primary Key), user\_id (Foreign Key)
- injury\_type, recovery\_status: ENUM or descriptive status.

**11. MENTAL\_WELLNESS**

Monitors mental health metrics.

Fields:

- assessment\_id (Primary Key), user\_id, injury\_id, water\_id (Foreign Keys)
- stress\_level: Integer rating.
- mood: Text description.

Key Relationships

- One-to-Many: Each user can have multiple entries in all related tables (e.g., sleep, workouts, nutrition).
- Foreign Keys: Each table references user\_id from the users table for relational integrity.
- Comprehensive Design: The schema allows detailed tracking and personalized health insights.

**DATABASE CREATION**



**1.Users**

CREATE TABLE Users (

`    `user\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `name VARCHAR(100),

`    `email VARCHAR(100) UNIQUE,

`    `password VARCHAR(100),

`    `weight FLOAT,

`    `age INT,

`    `gender ENUM('Male', 'Female', 'Other')

);

INSERT INTO Users (name, email, password, weight, age, gender)

VALUES 

('Amit Sharma', 'amit.sharma@example.com', 'amit@123', 70.0, 27, 'Male'),

('Priya Iyer', 'priya.iyer@example.com', 'priya@456', 60.0, 30, 'Female');

SELECT \* FROM Users;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.005.png)

Figure 5.1 : Users Table

**2.Workout\_Plans**

CREATE TABLE Workout\_Plans (

`    `plan\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `plan\_name VARCHAR(100),

`    `difficulty\_level VARCHAR(50),

`    `goal VARCHAR(100),

`    `duration INT,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Workout\_Plans (user\_id, plan\_name, difficulty\_level, goal, duration)

VALUES 

(1, 'Bollywood Fit Plan', 'Beginner', 'Weight Loss', 30),

(2, 'Strength for Women', 'Intermediate', 'Toning', 45);

SELECT \* FROM Workout\_Plans;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.006.png)

Figure 5.2 : Workout\_Plans


3\. Workout\_Progress

CREATE TABLE Workout\_Progress (

`    `progress\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `plan\_id INT,

`    `exercise\_name VARCHAR(100),

`    `sets INT,

`    `reps INT,

`    `weight\_used FLOAT,

`    `completion\_status BOOLEAN,

`    `date DATE,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id),

`    `FOREIGN KEY (plan\_id) REFERENCES Workout\_Plans(plan\_id)

);

INSERT INTO Workout\_Progress (user\_id, plan\_id, exercise\_name, sets, reps, weight\_used, completion\_status, date)

VALUES 

(1, 1, 'Surya Namaskar', 3, 12, 0, TRUE, '2025-05-05');

SELECT \* FROM Workout\_Progress;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.007.png)

Figure 5.3 : Workout\_Progress Table


**4.** Nutrition\_Plans

CREATE TABLE Nutrition\_Plans (

`    `plan\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `total\_calories INT,

`    `total\_protein FLOAT,

`    `total\_fats FLOAT,

`    `total\_carbs FLOAT,

`    `plan\_name VARCHAR(100),

`    `duration INT,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Nutrition\_Plans (user\_id, total\_calories, total\_protein, total\_fats, total\_carbs, plan\_name, duration)

VALUES 

(1, 1800, 60, 50, 250, 'South Indian Veg Diet', 30);

SELECT \* FROM Nutrition\_Plans;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.008.png)

Figure 5.4 : Nutrition\_Plans Table


**5.** Sleep\_Tracking

CREATE TABLE Sleep\_Tracking (

`    `sleep\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `sleep\_duration FLOAT,

`    `sleep\_quality ENUM('Poor', 'Average', 'Good', 'Excellent'),

`    `timestamp DATETIME DEFAULT CURRENT\_TIMESTAMP,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Sleep\_Tracking (user\_id, sleep\_duration, sleep\_quality)

VALUES 

(1, 6.5, 'Average');

SELECT \* FROM Sleep\_Tracking;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.009.png)

Figure 5.5 : Sleep\_Tracking Table


**6. Water\_Intake**

CREATE TABLE Water\_Intake (

`    `water\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `amount FLOAT,

`    `timestamp DATETIME DEFAULT CURRENT\_TIMESTAMP,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Water\_Intake (user\_id, amount)

VALUES 

(1, 0.5), (1, 1.0);

SELECT \* FROM Water\_Intake;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.010.png)

Figure 5.6: Water\_Intake Table


**7. Pose\_Analysis**

CREATE TABLE Pose\_Analysis (

`    `pose\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `exercise\_name VARCHAR(100),

`    `exercise\_score FLOAT,

`    `feedback TEXT,

`    `timestamp DATETIME DEFAULT CURRENT\_TIMESTAMP,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Pose\_Analysis (user\_id, exercise\_name, exercise\_score, feedback)

VALUES 

(1, 'Surya Namaskar', 90.5, 'Maintain balance in backward bend');

SELECT \* FROM Pose\_Analysis; 


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.011.png)

Figure 5.7 : Pose\_Analysis Table


` `**8. Heart\_Rate\_Monitor Table**

CREATE TABLE Heart\_Rate\_Monitor (

`    `monitor\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `heart\_rate INT,

`    `timestamp DATETIME DEFAULT CURRENT\_TIMESTAMP,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Heart\_Rate\_Monitor (user\_id, heart\_rate)

VALUES 

(1, 76), (1, 82);

SELECT \* FROM Heart\_Rate\_Monitor;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.012.png)

Figure 5.8 : Heart\_Rate\_Monitor Table


**9. Challenges**

CREATE TABLE Challenges (

`    `challenge\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `challenge\_name VARCHAR(100),

`    `start\_date DATE,

`    `end\_date DATE,

`    `reward\_points INT,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Challenges (user\_id, challenge\_name, start\_date, end\_date, reward\_points)

VALUES 

(1, 'Yoga Every Morning', '2025-05-01', '2025-05-07', 100);

SELECT \* FROM Challenges;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.013.png)

Figure 5.9 : Challenges Table


**10. Injury\_History**

CREATE TABLE Injury\_History (

`    `injury\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `injury\_type VARCHAR(100),

`    `recovery\_status ENUM('Recovering', 'Recovered', 'Chronic'),

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Injury\_History (user\_id, injury\_type, recovery\_status)

VALUES 

(1, 'Knee Pain', 'Recovering');

SELECT \* FROM Injury\_History;


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.014.png)

Figure 5.10 : Injury\_History Table

**11. Mental\_Wellness**

CREATE TABLE Mental\_Wellness (

`    `assessment\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `stress\_level ENUM('Low', 'Moderate', 'High'),

`    `mood ENUM('Happy', 'Neutral', 'Sad', 'Anxious'),

`    `timestamp DATETIME DEFAULT CURRENT\_TIMESTAMP,

`    `FOREIGN KEY (user\_id) REFERENCES Users(user\_id)

);

INSERT INTO Mental\_Wellness (user\_id, stress\_level, mood)

VALUES 

(1, 'Moderate', 'Happy');

SELECT \* FROM Mental\_Wellness;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.015.png)

Figure 5.11 : Injury\_History Table



**CONSTRAINTS**


**1. PREVENT NEGATIVE WEIGHT**

ALTER TABLE Users

ADD CONSTRAINT chk\_weight\_positive CHECK (weight > 0);


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.016.png)

Figure 6.1 : NegativeWeight Constraint


**2. ENSURE UNIQUE PLAN NAME PER USER**

ALTER TABLE Workout\_Plans

ADD CONSTRAINT uq\_plan\_user UNIQUE (user\_id, plan\_name);

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.017.png)

Figure 6.2 : UniquePlanNumber Constraint


**3**. **ENSURE SLEEP DURATION IS REALISTIC (E.G. BETWEEN 1 AND 24 HOURS)**

ALTER TABLE Sleep\_Tracking

ADD CONSTRAINT chk\_sleep\_duration CHECK (sleep\_duration BETWEEN 1 AND 24);

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.018.png)

Figure 6.3 : RealisticSleepDuration Trigger




**SET**


**1. USERS WHO EITHER COMPLETED WORKOUTS OR JOINED CHALLENGES**

SELECT DISTINCT user\_id FROM Workout\_Progress

UNION

SELECT DISTINCT user\_id FROM Challenges;


![ref1]

Figure 7.1 :  Either Workout or Joined Challenges Set



**2. USERS WHO DID BOTH WORKOUTS AND JOINED CHALLENGES**

SELECT DISTINCT wp.user\_id

FROM Workout\_Progress wp

INNER JOIN Challenges c ON wp.user\_id = c.user\_id;


![ref1]

Figure 7.2 :  Both Workout & Joined Challenges Set

**3. USERS WHO JOINED CHALLENGES BUT NEVER LOGGED WORKOUT PROGRESS**

SELECT DISTINCT c.user\_id

FROM Challenges c

LEFT JOIN Workout\_Progress wp ON c.user\_id = wp.user\_id

WHERE wp.user\_id IS NULL;



**4. USERS WHO HAVE SLEEP OR WATER TRACKING RECORDS**

SELECT DISTINCT user\_id FROM Sleep\_Tracking

UNION

SELECT DISTINCT user\_id FROM Water\_Intake;

![ref1]

Figure 7.3 :  Have either Sleep or Water Tracking Records Set



**5. USERS WHO JOINED CHALLENGES BUT NEVER LOGGED WORKOUT PROGRESS**

SELECT DISTINCT pa.user\_id

FROM Pose\_Analysis pa

LEFT JOIN Injury\_History ih ON pa.user\_id = ih.user\_id

WHERE ih.user\_id IS NULL;




**JOINS**



**1. SHOW WORKOUT PROGRESS WITH USER'S NAME AND PLAN**

SELECT u.name, wp.plan\_name, w.exercise\_name, w.date

FROM Workout\_Progress w

JOIN Users u ON w.user\_id = u.user\_id

JOIN Workout\_Plans wp ON w.plan\_id = wp.plan\_id;


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.020.png)

Figure 8.1 :   First Join



**2. NUTRITION PLAN WITH USER DETAILS**

SELECT u.name, np.plan\_name, np.total\_calories

FROM Nutrition\_Plans np

JOIN Users u ON np.user\_id = u.user\_id;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.021.png)

Figure 8.2 :  Second Join


**3. WATER INTAKE LOGS WITH TIMESTAMP AND NAME**

SELECT u.name, wi.amount, wi.timestamp

FROM Water\_Intake wi

JOIN Users u ON wi.user\_id = u.user\_id;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.022.png)

Figure 8.3 :   Third Join

**4. USERS AND THEIR HEART RATE READINGS**

SELECT u.name, hr.heart\_rate, hr.timestamp

FROM Heart\_Rate\_Monitor hr

JOIN Users u ON hr.user\_id = u.user\_id;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.023.png)

Figure 8.4 :  Fourth Join


**5. JOIN CHALLENGES AND PROGRESS TO GET OVERLAP INFO**

SELECT DISTINCT u.name, c.challenge\_name, wp.exercise\_name

FROM Users u

JOIN Challenges c ON u.user\_id = c.user\_id

JOIN Workout\_Progress wp ON u.user\_id = wp.user\_id;

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.024.png)

Figure 8.5 :   Fifth Join



**VIEWS**

**1.** **VIEW: ACTIVE USERS WITH RECENT WORKOUT**

CREATE VIEW Active\_Workout\_Users AS

SELECT u.name, w.date

FROM Users u

JOIN Workout\_Progress w ON u.user\_id = w.user\_id

WHERE w.date >= CURDATE() - INTERVAL 7 DAY;


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.025.png)


**2. VIEW: HIGH SCORERS IN POSE ANALYSIS**

CREATE VIEW High\_Pose\_Scores AS

SELECT u.name, p.exercise\_name, p.exercise\_score

FROM Pose\_Analysis p

JOIN Users u ON p.user\_id = u.user\_id

WHERE p.exercise\_score >= 85;


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.026.png)


**3. VIEW: USERS WITH GOOD OR EXCELLENT SLEEP**

CREATE VIEW Good\_Sleepers AS

SELECT u.name, s.sleep\_quality, s.sleep\_duration

FROM Sleep\_Tracking s

JOIN Users u ON s.user\_id = u.user\_id

WHERE s.sleep\_quality IN ('Good', 'Excellent');

![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.027.png)

**4. VIEW: USERS IN ACTIVE CHALLENGES**

CREATE VIEW Ongoing\_Challenges AS

SELECT u.name, c.challenge\_name

FROM Challenges c

JOIN Users u ON c.user\_id = u.user\_id

WHERE c.end\_date >= CURDATE();


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.028.png)


**5. VIEW: USERS WITH INJURIES AND MOOD**

CREATE VIEW Injury\_Mental\_Status AS

SELECT u.name, i.injury\_type, m.mood, m.stress\_level

FROM Injury\_History i

JOIN Mental\_Wellness m ON i.user\_id = m.user\_id

JOIN Users u ON u.user\_id = i.user\_id;


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.029.png)


**TRIGGERS**


**1. TRIGGER: ALERT ON HIGH HEART RATE**

CREATE TRIGGER trg\_high\_heart\_rate

AFTER INSERT ON Heart\_Rate\_Monitor

FOR EACH ROW

BEGIN

`    `IF NEW.heart\_rate > 100 THEN

`        `INSERT INTO Heart\_Rate\_Alerts (user\_id, heart\_rate, alert\_message)

`        `VALUES (NEW.user\_id, NEW.heart\_rate, 'Heart rate exceeded safe limit!');

`    `END IF;

END;

**2. TRIGGER: AUTO FEEDBACK ON LOW POSE SCORE**

CREATE TRIGGER trg\_low\_pose\_feedback

BEFORE INSERT ON Pose\_Analysis

FOR EACH ROW

BEGIN

`    `IF NEW.exercise\_score < 60 THEN

`        `SET NEW.feedback = 'Needs improvement on posture';

`    `END IF;

END;

**3. TRIGGER: LOG WHEN USER JOINS CHALLENGE**

CREATE TABLE Challenge\_Logs (

`    `log\_id INT AUTO\_INCREMENT PRIMARY KEY,

`    `user\_id INT,

`    `challenge\_name VARCHAR(100),

`    `joined\_at DATETIME DEFAULT CURRENT\_TIMESTAMP

);

CREATE TRIGGER trg\_challenge\_join\_log

AFTER INSERT ON Challenges

FOR EACH ROW

BEGIN

`    `INSERT INTO Challenge\_Logs (user\_id, challenge\_name)

`    `VALUES (NEW.user\_id, NEW.challenge\_name);

END;

**4. TRIGGER: ENSURE RECOVERY\_STATUS IS 'RECOVERING' ON INSERT**

CREATE TRIGGER trg\_default\_recovery\_status

BEFORE INSERT ON Injury\_History

FOR EACH ROW

BEGIN

`    `IF NEW.recovery\_status IS NULL THEN

`        `SET NEW.recovery\_status = 'Recovering';

`    `END IF;

END;

**5. TRIGGER: PREVENT SLEEPING < 2 HOURS**

CREATE TRIGGER trg\_sleep\_duration\_check

BEFORE INSERT ON Sleep\_Tracking

FOR EACH ROW

BEGIN

`    `IF NEW.sleep\_duration < 2 THEN

`        `SIGNAL SQLSTATE '45000'

`        `SET MESSAGE\_TEXT = 'Sleep duration must be at least 2 hours';

`    `END IF;

END;





**CURSORS**


**1. CURSOR: COUNT WORKOUT SESSIONS PER USER**

DELIMITER $$

CREATE PROCEDURE Workout\_Count\_Per\_User()

BEGIN

`    `DECLARE done INT DEFAULT 0;

`    `DECLARE uid INT;

`    `DECLARE uname VARCHAR(100);

`    `DECLARE count\_workouts INT;

`    `DECLARE cur CURSOR FOR SELECT user\_id, name FROM Users;

`    `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

`    `OPEN cur;

`    `read\_loop: LOOP

`        `FETCH cur INTO uid, uname;

`        `IF done THEN LEAVE read\_loop; END IF;

`        `SELECT COUNT(\*) INTO count\_workouts FROM Workout\_Progress WHERE user\_id = uid;

`        `SELECT CONCAT(uname, ' has ', count\_workouts, ' workout sessions.') AS Info;

`    `END LOOP;

`    `CLOSE cur;

END$$

DELIMITER ;

**2. CURSOR: FETCH USERS AND CHECK STRESS LEVEL**

DELIMITER $$

CREATE PROCEDURE Check\_Stress()

BEGIN

`    `DECLARE done INT DEFAULT 0;

`    `DECLARE uid INT;

`    `DECLARE uname VARCHAR(100);

`    `DECLARE stress\_level VARCHAR(20);

`    `DECLARE cur CURSOR FOR

`        `SELECT u.user\_id, u.name FROM Users u

`        `JOIN Mental\_Wellness m ON u.user\_id = m.user\_id;

`    `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

`    `OPEN cur;

`    `read\_loop: LOOP

`        `FETCH cur INTO uid, uname;

`        `IF done THEN LEAVE read\_loop; END IF;

`        `SELECT stress\_level INTO stress\_level FROM Mental\_Wellness WHERE user\_id = uid LIMIT 1;

`        `SELECT CONCAT(uname, ' has ', stress\_level, ' stress.') AS Status;

`    `END LOOP;

`    `CLOSE cur;

END$$

DELIMITER ;


**3. CURSOR: CHECK USERS WITH INJURY + POSE SCORE < 60**

DELIMITER $$

CREATE PROCEDURE At\_Risk\_Users()

BEGIN

`    `DECLARE done INT DEFAULT 0;

`    `DECLARE uid INT;

`    `DECLARE uname VARCHAR(100);

`    `DECLARE pose\_score FLOAT;

`    `DECLARE cur CURSOR FOR

`        `SELECT DISTINCT u.user\_id, u.name

`        `FROM Users u

`        `JOIN Injury\_History i ON u.user\_id = i.user\_id

`        `JOIN Pose\_Analysis p ON u.user\_id = p.user\_id

`        `WHERE p.exercise\_score < 60;

`    `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

`    `OPEN cur;

`    `read\_loop: LOOP

`        `FETCH cur INTO uid, uname;

`        `IF done THEN LEAVE read\_loop; END IF;

`        `SELECT exercise\_score INTO pose\_score

`        `FROM Pose\_Analysis

`        `WHERE user\_id = uid

`        `ORDER BY time\_stamp DESC LIMIT 1;

`        `SELECT CONCAT(uname, ' is at risk with pose score: ', pose\_score) AS Alert;

`    `END LOOP;

`    `CLOSE cur;

END$$

DELIMITER ;

**4. CURSOR: USER HYDRATION STATUS (IF WATER INTAKE < 2L PER DAY)**

DELIMITER $$

CREATE PROCEDURE Hydration\_Status()

BEGIN

`    `DECLARE done INT DEFAULT 0;

`    `DECLARE uid INT;

`    `DECLARE uname VARCHAR(100);

`    `DECLARE total\_water FLOAT;

`    `DECLARE cur CURSOR FOR SELECT user\_id, name FROM Users;

`    `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

`    `OPEN cur;

`    `read\_loop: LOOP

`        `FETCH cur INTO uid, uname;

`        `IF done THEN LEAVE read\_loop; END IF;

`        `-- Sum of today's water intake

`        `SELECT IFNULL(SUM(amount), 0) INTO total\_water

`        `FROM Water\_Intake

`        `WHERE user\_id = uid AND DATE(timestamp) = CURDATE();

`        `IF total\_water < 2 THEN

`            `SELECT CONCAT(uname, ' is under-hydrated with only ', total\_water, 'L today.') AS Hydration\_Alert;

`        `ELSE

`            `SELECT CONCAT(uname, ' has sufficient hydration: ', total\_water, 'L.') AS Hydration\_Status;

`        `END IF;

`    `END LOOP;

`    `CLOSE cur;

END$$

DELIMITER ;

**5. CURSOR: CALORIES VS SLEEP QUALITY ANALYSIS PER USER (OPTIONAL ADVANCED)**

DELIMITER $$

CREATE PROCEDURE Calorie\_Sleep\_Analysis()

BEGIN

`    `DECLARE done INT DEFAULT 0;

`    `DECLARE uid INT;

`    `DECLARE uname VARCHAR(100);

`    `DECLARE calories INT;

`    `DECLARE sleep\_hrs FLOAT;

`    `DECLARE quality VARCHAR(50);

`    `DECLARE cur CURSOR FOR

`        `SELECT u.user\_id, u.name FROM Users u

`        `JOIN Nutrition\_Plans np ON u.user\_id = np.user\_id

`        `JOIN Sleep\_Tracking st ON u.user\_id = st.user\_id;

`    `DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

`    `OPEN cur;

`    `read\_loop: LOOP

`        `FETCH cur INTO uid, uname;

`        `IF done THEN LEAVE read\_loop; END IF;

`        `SELECT calorie\_intake INTO calories FROM Nutrition\_Plans WHERE user\_id = uid LIMIT 1;

`        `SELECT sleep\_duration, sleep\_quality INTO sleep\_hrs, quality

`        `FROM Sleep\_Tracking

`        `WHERE user\_id = uid ORDER BY sleep\_id DESC LIMIT 1;

`        `SELECT CONCAT(uname, ' has ', calories, ' kcal and slept ', sleep\_hrs, ' hrs with sleep quality: ', quality) AS Report;

`    `END LOOP;

`    `CLOSE cur;

END$$

DELIMITER ;



**Identifying the Dependencies**



1. **Functional Dependencies**

|**Table Name**|**Functional Dependency**|
| :-: | :-: |
|**users**|user\_id → name, email, password, weight, age, gender|
|**pose\_analysis**|pose\_id → user\_id, exercise\_name, accuracy\_score, feedback, time\_stamp|
|**nutrition\_plans**|plan\_id → user\_id, calorie\_intake, protein|
|**sleep\_tracking**|sleep\_id → user\_id, sleep\_duration, sleep\_quality|
|**water\_intake**|water\_id → user\_id, amount, timestamp|
|**mental\_wellness**|assessment\_id → user\_id, stress\_level, mood|
|**injury\_history**|injury\_id → user\_id, injury\_type, recovery\_status|
|**heart\_rate\_monitor**|monitor\_id → user\_id, heart\_rate, timestamp|
|**workout\_plans**|plan\_id → user\_id, plan\_name, exercise\_list, difficulty\_level, goal, duration|
|**workout\_progress**|progress\_id → user\_id, plan\_id, exercise\_name, sets, reps, weight\_used, completion\_status, date|
|**challenges**|challenge\_id → user\_id, challenge\_name, start\_date, end\_date, reward\_points|

**Explanation:**

Functional dependencies describe the relationship between attributes in a table, where a particular column (or set of columns) uniquely determines another column. In a well-structured database, each table should have a primary key that uniquely identifies each record, and all non-key attributes should depend only on that key.

For example:

In the users table, user\_id uniquely determines a user's name, email, password, weight, age, and gender. This is written as:

user\_id → name, email, password, weight, age, gender.

In the pose\_analysis table, the pose\_id uniquely identifies a specific posture analysis entry and determines details like which user performed the pose, the exercise name, accuracy score, feedback, and timestamp.

pose\_id → user\_id, exercise\_name, accuracy\_score, feedback, time\_stamp.

By identifying these functional dependencies, we ensure each piece of data is stored in only one place, eliminating redundancy and improving data integrity. Each table focuses on a single entity or concept, with clearly defined relationships to others via foreign keys (e.g., user\_id).

Correct functional dependency mapping is the foundation for First Normal Form (1NF) and is essential before checking for partial or transitive dependencies in 2NF or 3NF.


1. **Partial Dependencies (Violates 2NF if present)**

|**Table Name**|**Partial Dependencies**|
| :-: | :-: |
|**workout\_progress**|exercise\_name → sets, reps (if exercise details are redundantly stored instead of normalized)|
|**pose\_analysis**|exercise\_name → accuracy\_score (if stored across users instead of per-user performance)|
|**nutrition\_plans**|user\_id → calorie\_intake (if same plan is reused across users, normalization is needed)|



**Explanation:**

Partial dependencies happen when part of a composite key determines non-key attributes. In workout\_progress, if exercise\_name is reused and has static sets/reps info, then the dependency is partial and should be moved to a reference table (e.g., exercises).


**3. Transitive Dependencies (Violates 3NF if present)**

|**Table Name**|**Transitive Dependencies**|
| :-: | :-: |
|**workout\_progress**|progress\_id → plan\_id → plan\_name, difficulty\_level|
|**pose\_analysis**|pose\_id → user\_id → user\_name|
|**heart\_rate\_monitor**|monitor\_id → user\_id → age, gender|
|**challenges**|challenge\_id → user\_id → user\_name|
|**injury\_history**|injury\_id → user\_id → user\_name, age|

**Explanation:**

Transitive dependencies occur when non-key attributes depend on another non-key attribute that in turn depends on the primary key. For instance, in pose\_analysis, pose\_id → user\_id → name is a transitive dependency, and attributes like user name should not be stored there.




**PITFALLS , Normalizations & Dependencies**

**1.Customer Table**

![A black screen with white text

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.030.jpeg)

Figure 12.1 :   Customer Table before normalization

**Functional Dependencies**:

• customer\_id → name, email, phone\_number, address\
• email → customer\_id\
• phone\_number → customer\_id

**Normalization:**

|**Normal Form**|**Status**|**Reason**|
| :- | :- | :-: |
|**1NF**|Yes|All values are atomic (e.g., single phone number per row)|
|**2NF**|Yes|Primary key is a single attribute (patient\_id), all attributes fully depend on it|
|**3NF**|Yes|No transitive dependencies (email and phone\_number are direct dependents)|
|**BCNF**|Yes|All determinants (including email, phone\_number) are candidate keys|
|**4NF**|Yes|No multivalued dependencies|
|**5NF**|Yes|No join dependency anomalies|
### **Pitfalls:**
There are **no design flaws or normalization issues** in the Patient table.

All dependencies are clear, and every attribute depends directly and only on the primary key (or a candidate key).






**2.Orders**
### ![A black screen with white text

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.031.jpeg)
Figure 12.2 :   Orders table before normalization
### **Functional Dependencies:**
• order\_id → customer\_id, items\_list, total\_amount\
• items\_list → product\_ids (Multivalued)\
• order\_id, product\_id → quantity, price
------------------------------------------------------
###
**Normalization:**

|**Normal Form**|**Status**|**Explanation**|
| :- | :- | :-: |
|**1NF**|` `No|items\_list is a comma-separated list – not atomic|
|**2NF**|` `No|Partial dependency of quantity and price on product\_id|
|**3NF**|` `No|Transitive dependency possible via customer\_id → customer details|
|**BCNF**|` `No|items\_list is not a candidate key|
|**4NF**|` `No|Multivalued dependencies|
|**5NF**|` `No|Lossless join is not guaranteed unless normalized|
### **Pitfalls:**
- **Non-Atomic Values (1NF Violation)**: items\_list is a comma-separated list
- **Multivalued Dependencies (4NF Violation)**
- **Partial Dependencies (2NF Violation)**: Partial dependency of quantity and price on product\_id.
- **Transitive Dependencies (3NF Violation)**: Transitive dependency possible via customer\_id → customer details
- **Non-Candidate Key Determinants (BCNF Violation)**: items\_list is not a candidate key
### **Functional Dependencies (in Normalized Design)**
• Orders: order\_id → customer\_id, order\_date, total\_amount\
• OrderItems: (order\_id, product\_id) → quantity, price\
This resolves multivalued and partial dependencies.





**3.Products**

![A screenshot of a computer screen

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.032.jpeg)

Figure 12.3 : Products table before normalization

### **Functional Dependencies:**
` `• product\_id → product\_name, category\_id, price, stock

` `**Normalization:**

|**Normal Form**|`   `**Status**|`              `**Reason**|
| :- | :-: | :- |
|`  `1NF                 |`   `Yes|`              `All values are atomic|
|`  `2NF|`   `Yes           |`              `Single-column primary key; all fields fully dependent on it|
|`  `3NF|`   `Yes|`              `No transitive dependencies|
|` `BCNF|`   `Yes|`              `All determinants are candidate keys|
|`  `4NF|`   `Yes|`              `No multivalued dependencies|
|5NF|`   `yes|`              `No join dependency anomalies|

**Pitfalls:**

- There are **no design flaws** or normalization issues in the DrugCategory table.
- Each attribute directly and fully depends on the primary key (drug\_category\_id)

**4.Category**

![A screenshot of a computer program

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.033.jpeg)

Figure 12.4 :   Category table before nromalization

**Functional Dependencies:**

- ` `category\_id → category\_name, description.

**Normalization (Before Fix):**

|**Normal Form**|**Status**|**Explanation**|
| :- | :-: | :-: |
|1NF|Yes|All values are atomic|
|2NF|Yes|Single-column primary key|
|3NF|Yes|No transitive dependencies|
|BCNF|Yes|All determinants are candidate keys|
|4NF|Yes|No multivalued dependencies|
|5NF|Yes|No join dependency anomalies|








**TRANSACTIONS**

1. **Basic Transaction: Create Invoice, Log Transaction sql**

START TRANSACTION;

INSERT INTO Invoice (date, customer\_name, customer\_contact)

VALUES (CURDATE(), 'Rahul Kumar', '9998887776');

SET @bill\_number = LAST\_INSERT\_ID();

INSERT INTO TransactionTable (bill\_number, date, total\_amount)

VALUES (@bill\_number, CURDATE(), 350.00);

![A screenshot of a computer program

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.034.jpeg)

Figure 13.1 :   First Transaction

1. **Complete Purchase Transaction: Invoice + Items + Stock Update**

   START TRANSACTION;

   INSERT INTO Invoice (date, customer\_name, customer\_contact)

   VALUES (CURDATE(), 'Neha Sharma', '8887776665');

   SET @bill\_number = LAST\_INSERT\_ID();

   INSERT INTO Transactions (bill\_number, total\_amount)

   VALUES (@bill\_number, 270.00);

   INSERT INTO TransactionItems (bill\_number, product\_name, quantity, price)

   VALUES

   (@bill\_number, 'Milk', 2, 60.00),

   (@bill\_number, 'Lays Chips', 3, 150.00),

   (@bill\_number, 'Tomato', 2, 60.00);

   UPDATE Product SET stock\_quantity = stock\_quantity - 2 WHERE product\_name = 'Milk';

   UPDATE Product SET stock\_quantity = stock\_quantity - 3 WHERE product\_name = 'Lays Chips';

   UPDATE Product SET stock\_quantity = stock\_quantity - 2 WHERE product\_name = 'Tomato';

   ![A computer screen shot of a black screen

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.035.jpeg)

Figure 13.2 :   Second Transaction

1. **Commit-- Begin transaction**

   START TRANSACTION;

   INSERT INTO Transactions (total\_amount) VALUES (0.00);

   SET @bill\_number = LAST\_INSERT\_ID();

   INSERT INTO TransactionItems (bill\_number, product\_name, quantity, price)

   VALUES (@bill\_number, 'Apple', 2, 25.00);

   UPDATE Product SET quantity = quantity - 2 WHERE product\_name = 'Apple';

   COMMIT;

   ![A screen shot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.036.jpeg)

Figure 13.3 :   Third Transaction

1. **Rollback**

   START TRANSACTION;

   INSERT INTO Transactions (total\_amount) VALUES (0.00);

   SET @bill\_number = LAST\_INSERT\_ID();

   INSERT INTO TransactionItems (bill\_number, product\_name, quantity, price)

   VALUES (@bill\_number, 'NonExistentProduct', 1, 100.00);

   ROLLBACK;

 

   ![A screen shot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.037.jpeg)

Figure 13.4 :   Fourth Transaction

**IMPLEMENTATION RESULT**

![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.038.png)


Figure 14.1 :   Admin Page





![A screenshot of a website

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.039.jpeg)



Figure 14.2 : Home Page




![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.040.jpeg)


Figure 14.3 : Categories Page


![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.041.jpeg)

Figure 14.4 : Products of one category

![A screenshot of a grocery store

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.042.jpeg)

Figure 14.5 : Cart Page


![A screenshot of a computer

AI-generated content may be incorrect.](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.043.jpeg)

Figure 14.6 : Checkout Page

**CODE FOR THE PROJECT**

one\_flask.py – authentication

import subprocess

import requests

import time

import os

from flask import Flask, render\_template, request, redirect, url\_for, flash, jsonify

import mysql.connector

import atexit

app = Flask(\_\_name\_\_)

\# List of microservice Flask apps with their expected ports

microservices = [

`    `{"name": "Chatbot", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\Fitness\_chatbot\app.py", "port": 3001},

`    `{"name": "OpenCV", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\opencv\app.py", "port": 3030},

`    `{"name": "Challenges", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\challenges\app.py", "port": 3009},

`    `{"name": "Injury", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\injury\injury\_app.py", "port": 5002},

`    `{"name": "Nutrition", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\Nutrition\_plan\app.py", "port": 3012},

`    `{"name": "Mental\_wellness", "path": r"D:\DBMS PROJECT\dbms\_fitness\_project\Backend\MentalWellness\well\_app.py", "port": 5001},

]

running\_processes = []

def launch\_microservices():

`    `for service in microservices:

`        `print(f"Launching {service['name']} on port {service['port']}...")

`        `try:

`            `# Normalize the path

`            `normalized\_path = os.path.normpath(service["path"])

`            `directory = os.path.dirname(normalized\_path)

`            `filename = os.path.basename(normalized\_path)



`            `if not os.path.exists(normalized\_path):

`                `print(f"❌ Error: File not found - {normalized\_path}")

`                `continue



`            `# Start the service

`            `process = subprocess.Popen(

`                `["python", filename],

`                `cwd=directory,

`                `stdout=subprocess.PIPE,

`                `stderr=subprocess.PIPE

`            `)

`            `running\_processes.append({"process": process, "service": service})

`            `print(f"✅ Started {service['name']}")

`        `except Exception as e:

`            `print(f"❌ Failed to start {service['name']}: {str(e)}")

def cleanup\_processes():

`    `print("\nTerminating microservices...")

`    `for proc in running\_processes:

`        `try:

`            `proc["process"].terminate()

`        `except:

`            `pass

`    `time.sleep(2)

`    `print("All microservices terminated.")

\# Register cleanup function

atexit.register(cleanup\_processes)

\# Launch microservices on startup

launch\_microservices()

app.secret\_key = 'cd0df92f92f997d5492f59872add022bf6c4473f1fee51ebacd4a76fa38c82ef'

\# Helper function to get a DB connection

def get\_db\_connection():

`    `return mysql.connector.connect(

`        `host="localhost",

`        `port=3306,

`        `user="root",

`        `password="root",

`        `database="pose"

`    `)

@app.route('/')

def index():

`    `return render\_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])

def signup():

`    `if request.method == 'POST':

`        `# Retrieve form data

`        `name = request.form.get('name')

`        `email = request.form.get('email')

`        `age = request.form.get('age')

`        `gender = request.form.get('gender')

`        `password = request.form.get('password')

`        `weight = request.form.get('weight')

`        `# Simple validation

`        `if not all([name, email, age, gender, password, weight]):

`            `flash('Please fill out all fields')

`            `return redirect(url\_for('signup'))

`        `try:

`            `conn = get\_db\_connection()

`            `cursor = conn.cursor()

`            `# Check if email already exists

`            `cursor.execute("SELECT email FROM users WHERE email = %s", (email,))

`            `if cursor.fetchone():

`                `flash('Email already exists')

`                `return redirect(url\_for('signup'))

`            `# Insert new user

`            `query = """

`                `INSERT INTO users (name, email, age, gender, password, weight)

`                `VALUES (%s, %s, %s, %s, %s, %s)

`            `"""

`            `cursor.execute(query, (name, email, age, gender, password, weight))

`            `conn.commit()

`            `flash('Sign up successful! Please login.')

`            `return redirect(url\_for('index'))

`        `except mysql.connector.Error as err:

`            `flash(f'Error: {err}')

`            `return redirect(url\_for('signup'))

`        `finally:

`            `if 'cursor' in locals():

`                `cursor.close()

`            `if 'conn' in locals():

`                `conn.close()

`    `return render\_template('signup.html')

@app.route('/login', methods=['POST'])

def login():

`    `email = request.form.get('email')

`    `password = request.form.get('password')



`    `try:

`        `conn = get\_db\_connection()

`        `cursor = conn.cursor(dictionary=True)

`        `# Fetch user details based on email

`        `query = "SELECT \* FROM users WHERE email = %s"

`        `cursor.execute(query, (email,))

`        `user = cursor.fetchone()

`        `if user and user['password'] == password:

`            `return jsonify({

`                `"success": True, 

`                `"message": "Login successful",

`                `"user": {

`                    `"id": user['User\_id'],

`                    `"name": user['name'],

`                    `"email": user['email']

`                `}

`            `})

`        `else:

`            `return jsonify({"success": False, "message": "Invalid email or password"})

`    `except mysql.connector.Error as err:

`        `return jsonify({"success": False, "message": f"Database error: {err}"})

`    `finally:

`        `if 'cursor' in locals():

`            `cursor.close()

`        `if 'conn' in locals():

`            `conn.close()

if \_\_name\_\_ == '\_\_main\_\_':

`    `try:

`        `app.run(debug=True, port=5000, host='0.0.0.0')

`    `finally:

`        `cleanup\_processes()

**

HOMEPAGE – index.html

<!DOCTYPE html>

<html lang="en">

<head>

`  `<meta charset="UTF-8">

`  `<meta name="viewport" content="width=device-width, initial-scale=1.0">

`  `<title>PoseFit - Perfect Your Form, Transform Your Life</title>

`  `<!-- Tailwind CSS -->

`  `<script src="https://cdn.tailwindcss.com"></script>

`  `<!-- Lucide Icons -->

`  `<script src="https://cdnjs.cloudflare.com/ajax/libs/lucide/0.72.0/lucide.min.js"></script>

`  `<!-- Chart.js -->

`  `<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>

`  `<style>

`    `@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

`    `body {

`      `font-family: 'Montserrat', sans-serif;

`    `}

.hero-pattern {

`      `background-image:

`        `linear-gradient(to right, rgba(99, 102, 241, 0.8), rgba(168, 85, 247, 0.8)),

`        `url('/api/placeholder/1600/900');

`      `background-size: cover;

`    `}

`  `</style>

</head>

<body class="bg-gray-50" onload="checkLoginStatus()">

`  `<!-- Navigation -->

`  `<nav class="bg-white shadow-md fixed w-full z-10">

`    `<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

`      `<div class="flex justify-between h-16">

`        `<div class="flex items-center">

`          `<span class="text-indigo-600 text-xl font-bold">PoseFit</span>

`          `<div class="hidden md:ml-6 md:flex md:space-x-8">

`            `<a href="#home"

`              `class="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">

`              `Home

`            `</a>

`            `<a href="#features"

`              `class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">

`              `Features

`            `</a>

`            `<a href="#dashboard"

`              `class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">

`              `Dashboard

`            `</a>

`          `</div>

`        `</div>

`        `<div class="flex items-center space-x-4">

`          `<a href="/signup"

`            `class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">

`            `Sign Up

`          `</a>

`          `<div id="auth-buttons">

`            `<button onclick="openLoginModal()"

`              `class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700">

`              `Login

`            `</button>

`          `</div>

`        `</div>

`      `</div>

`    `</div>

`  `</nav>

`  `<!-- Login Modal -->

`  `<div id="login-modal" class="hidden fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">

`    `<div class="bg-white p-6 rounded-lg shadow-lg w-96">

`      `<h2 class="text-xl font-bold mb-4">Login to PoseFit</h2>

`      `<form id="login-form" action="/login" method="POST">

`        `<label for="email" class="block text-sm font-medium text-gray-700">Email:</label>

`        `<input type="email" id="email" name="email" required class="w-full px-3 py-2 border rounded-md mb-3">

`        `<label for="password" class="block text-sm font-medium text-gray-700">Password:</label>

`        `<input type="password" id="password" name="password" required class="w-full px-3 py-2 border rounded-md mb-3">

`        `<button type="submit" class="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700">

`          `Login

`        `</button>

`      `</form>

`      `<button onclick="closeLoginModal()" class="mt-4 w-full bg-gray-400 text-white py-2 rounded-md hover:bg-gray-500">

`        `Cancel

`      `</button>

`      `<div id="login-error" class="mt-3 text-red-600 text-sm hidden"></div>

`    `</div>

`  `</div>

`  `<script>

`    `function openLoginModal() {

`      `document.getElementById('login-modal').classList.remove('hidden');

`      `document.getElementById('login-error').classList.add('hidden');

`    `}

`    `function closeLoginModal() {

`      `document.getElementById('login-modal').classList.add('hidden');

`    `}

`    `function checkLoginStatus() {

`      `const loggedInEmail = localStorage.getItem('loggedInUser');

`      `if (loggedInEmail) {

`        `document.getElementById('auth-buttons').innerHTML = `

`        `<span class="text-sm text-gray-700">Logged in as <strong>${loggedInEmail}</strong></span>

`        `<button onclick="logout()" class="ml-3 px-3 py-1 text-white bg-red-600 rounded-md hover:bg-red-700">

`          `Logout

`        `</button>

`      ``;

`      `}

`    `}

`    `document.getElementById('login-form').addEventListener('submit', async function (event) {

`      `event.preventDefault();

`      `const email = document.getElementById('email').value;

`      `const password = document.getElementById('password').value;

`      `try {

`        `const response = await fetch('/login', {

`          `method: 'POST',

`          `headers: {

`            `'Content-Type': 'application/x-www-form-urlencoded'

`          `},

`          `body: new URLSearchParams({ email: email, password: password })

`        `});

`        `// Get the response as JSON

`        `const result = await response.json();

`        `if (result.success) {

`          `localStorage.setItem('loggedInUser', email);

`          `closeLoginModal();

`          `checkLoginStatus();

`        `} else {

`          `document.getElementById('login-error').textContent = "Invalid email or password";

`          `document.getElementById('login-error').classList.remove('hidden');

`        `}

`      `} catch (error) {

`        `console.error('Login error:', error);

`        `document.getElementById('login-error').textContent = "An error occurred during login";

`        `document.getElementById('login-error').classList.remove('hidden');

`      `}

`    `});

`    `function logout() {

`      `localStorage.removeItem('loggedInUser');

`      `location.reload();

`    `}

`  `</script>

`  `<!-- Hero Section -->

`  `<section id="home" class="pt-16">

`    `<div class="hero-pattern min-h-[90vh] flex items-center">

`      `<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-white">

`        `<div class="lg:grid lg:grid-cols-12 lg:gap-8">

`          `<div class="sm:text-center md:max-w-2xl md:mx-auto lg:col-span-6 lg:text-left lg:flex lg:items-center">

`            `<div>

`              `<h1 class="text-4xl tracking-tight font-extrabold sm:text-5xl xl:text-6xl">

`                `Perfect Your Form,<br> Transform Your Life

`              `</h1>

`              `<p class="mt-3 text-base text-white sm:mt-5 sm:text-xl lg:text-lg xl:text-xl">

`                `AI-powered fitness analysis and personalized training plans to help you achieve your health goals safely

`                `and effectively.

`              `</p>

`              `<div class="mt-8 sm:mt-10">

`                `<a href="#features"

`                  `class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-indigo-700 bg-white hover:bg-gray-50 md:py-4 md:text-lg md:px-8">

`                  `Explore Features

`                `</a>

`              `</div>

`            `</div>

`          `</div>

`          `<div class="mt-12 lg:mt-0 lg:col-span-6">

`            `<div class="relative h-64 sm:h-72 md:h-96 lg:h-full">

`              `<!-- SVG Fitness Diagram -->

`              `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" class="w-full h-full">

`                `<style>

.figure {

`                    `fill: white;

`                  `}

.line {

`                    `stroke: rgba(255, 255, 255, 0.7);

`                    `stroke-width: 2;

`                  `}

.label {

`                    `fill: white;

`                    `font-size: 12px;

`                    `text-anchor: middle;

`                  `}

.highlight {

`                    `fill: #FCD34D;

`                    `opacity: 0.7;

`                  `}

`                `</style>

`                `<!-- Human figure outline -->

`                `<path class="figure"

`                  `d="M250,50 Q275,50 285,60 Q295,70 295,80 Q295,90 285,100 Q275,110 250,110 Q225,110 215,100 Q205,90 205,80 Q205,70 215,60 Q225,50 250,50 Z" />

`                `<path class="figure"

`                  `d="M250,110 L250,220 M230,220 L270,220 M250,150 L210,190 M250,150 L290,190 M250,220 L230,320 M250,220 L270,320 M230,320 L225,370 M270,320 L275,370" />

`                `<!-- Measurement lines -->

`                `<line class="line" x1="180" y1="80" x2="205" y2="80" />

`                `<line class="line" x1="295" y1="80" x2="320" y2="80" />

`                `<text class="label" x="165" y="85">Head</text>

`                `<text class="label" x="335" y="85">Alignment</text>

`                `<line class="line" x1="180" y1="150" x2="210" y2="150" />

`                `<line class="line" x1="290" y1="150" x2="320" y2="150" />

`                `<text class="label" x="165" y="155">Shoulders</text>

`                `<text class="label" x="335" y="155">Balanced</text>

`                `<line class="line" x1="180" y1="185" x2="210" y2="190" />

`                `<line class="line" x1="290" y1="190" x2="320" y2="185" />

`                `<text class="label" x="165" y="190">Arms</text>

`                `<text class="label" x="335" y="190">Engaged</text>

`                `<!-- Highlighted areas -->

`                `<circle class="highlight" cx="250" cy="80" r="15" />

`                `<circle class="highlight" cx="250" cy="150" r="12" />

`                `<rect class="highlight" x="245" y="170" width="10" height="50" rx="5" />

`                `<!-- Angle measurements -->

`                `<path class="line" d="M250,150 A40,40 0 0,1 290,170" fill="none" />

`                `<text class="label" x="275" y="140">95°</text>

`                `<path class="line" d="M250,220 A30,30 0 0,1 270,240" fill="none" />

`                `<text class="label" x="270" y="223">87°</text>

`              `</svg>

`            `</div>

`          `</div>

`        `</div>

`      `</div>

`    `</div>

`  `</section>

`  `<!-- Features Section -->

`  `<section id="features" class="py-20 bg-white">

`    `<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

`      `<div class="text-center">

`        `<h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">

`          `Comprehensive Fitness Features

`        `</h2>

`        `<p class="mt-4 text-xl text-gray-600">

`          `Everything you need to achieve your fitness goals in one place

`        `</p>

`      `</div>

`      `<div class="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

`        `<!-- Feature 1: Pose Analysis -->

`        `<a href="http://127.0.0.1:3030" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="activity" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">Pose Analysis</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `AI-powered analysis of your workout form to prevent injuries and maximize results

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`        `<!-- Feature 2: Nutrition Plans -->

`        `<a href="http://127.0.0.1:3012" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="apple" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">Nutrition Plans</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `Personalized meal plans and nutritional guidance based on your fitness goals

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`        `<!-- Feature 3: Water Intake -->

`        `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`          `<div class="px-4 py-5 sm:p-6">

`            `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`              `<i data-lucide="droplet" class="h-6 w-6"></i>

`            `</div>

`            `<h3 class="text-lg font-medium text-gray-900">Water Intake</h3>

`            `<p class="mt-2 text-base text-gray-600">

`              `Track your hydration levels and get reminders to stay properly hydrated throughout the day

`            `</p>

`          `</div>

`        `</div>

`        `<!-- Feature 4: Mental Wellness -->

`        `<a href="http://127.0.0.1:5001" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="brain" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">Mental Wellness</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `Guided meditation, stress management, and mood tracking to support overall well-being

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`        `<!-- Feature 5: Injury History -->

`        `<a href="http://127.0.0.1:5002" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="bandage" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">Injury History</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `Log past injuries to receive customized workout modifications that protect vulnerable areas

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`        `<!-- Feature 6: Heart Rate Monitor -->

`        `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`          `<div class="px-4 py-5 sm:p-6">

`            `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`              `<i data-lucide="heart-pulse" class="h-6 w-6"></i>

`            `</div>

`            `<h3 class="text-lg font-medium text-gray-900">Heart Rate Monitor</h3>

`            `<p class="mt-2 text-base text-gray-600">

`              `Connect your fitness devices to track heart rate zones during workouts for optimal training

`            `</p>

`          `</div>

`        `</div>

`        `<!-- Feature 7: Challenges -->

`        `<a href="http://127.0.0.1:3009" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="trophy" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">Challenges</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `Join community challenges to stay motivated and compete with friends

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`        `<!-- Feature 8: Workout Plans -->

`        `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`          `<div class="px-4 py-5 sm:p-6">

`            `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`              `<i data-lucide="dumbbell" class="h-6 w-6"></i>

`            `</div>

`            `<h3 class="text-lg font-medium text-gray-900">Workout Plans</h3>

`            `<p class="mt-2 text-base text-gray-600">

`              `Personalized training programs that adapt based on your progress and feedback

`            `</p>

`          `</div>

`        `</div>

`        `<!-- Feature 9: AI Fitness Chatbot -->

`        `<a href="http://127.0.0.1:3001" class="block">

`          `<div class="bg-white overflow-hidden shadow rounded-lg h-full hover:shadow-lg transition-shadow duration-300">

`            `<div class="px-4 py-5 sm:p-6">

`              `<div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white mb-5">

`                `<i data-lucide="message-circle" class="h-6 w-6"></i>

`              `</div>

`              `<h3 class="text-lg font-medium text-gray-900">AI Fitness Chatbot</h3>

`              `<p class="mt-2 text-base text-gray-600">

`                `24/7 support and guidance from our AI assistant to answer your fitness questions

`              `</p>

`            `</div>

`          `</div>

`        `</a>

`      `</div>

`    `</div>

`  `</section>

`  `<!-- Dashboard Section -->

`  `<section id="dashboard" class="py-20 bg-gray-50">

`    `<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

`      `<div class="text-center">

`        `<h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">

`          `Track Your Progress

`        `</h2>

`        `<p class="mt-4 text-xl text-gray-600">

`          `Visualize your fitness journey with our comprehensive dashboard

`        `</p>

`      `</div>

`      `<div class="mt-16 bg-white shadow-lg rounded-lg overflow-hidden">

`        `<div class="px-4 py-5 sm:p-6">

`          `<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

`            `<!-- Progress Overview -->

`            `<div class="lg:col-span-2">

`              `<h3 class="text-lg font-medium text-gray-900 mb-4">Workout Progress Overview</h3>

`              `<div class="h-80">

`                `<canvas id="progressChart"></canvas>

`              `</div>

`            `</div>

`            `<!-- Weekly Stats -->

`            `<div>

`              `<h3 class="text-lg font-medium text-gray-900 mb-4">This Week's Summary</h3>

`              `<div class="space-y-4">

`                `<div class="bg-gray-50 rounded-lg p-4">

`                  `<div class="flex justify-between items-center">

`                    `<span class="text-sm font-medium text-gray-500">Workouts Completed</span>

`                    `<span class="text-lg font-bold text-indigo-600">5/7</span>

`                  `</div>

`                  `<div class="w-full bg-gray-200 rounded-full h-2 mt-2">

`                    `<div class="bg-indigo-600 h-2 rounded-full" style="width: 71%"></div>

`                  `</div>

`                `</div>

`                `<div class="bg-gray-50 rounded-lg p-4">

`                  `<div class="flex justify-between items-center">

`                    `<span class="text-sm font-medium text-gray-500">Average Intensity</span>

`                    `<span class="text-lg font-bold text-indigo-600">7.8/10</span>

`                  `</div>

`                  `<div class="w-full bg-gray-200 rounded-full h-2 mt-2">

`                    `<div class="bg-indigo-600 h-2 rounded-full" style="width: 78%"></div>

`                  `</div>

`                `</div>

`                `<div class="bg-gray-50 rounded-lg p-4">

`                  `<div class="flex justify-between items-center">

`                    `<span class="text-sm font-medium text-gray-500">Water Goal</span>

`                    `<span class="text-lg font-bold text-indigo-600">2.5/3L</span>

`                  `</div>

`                  `<div class="w-full bg-gray-200 rounded-full h-2 mt-2">

`                    `<div class="bg-indigo-600 h-2 rounded-full" style="width: 83%"></div>

`                  `</div>

`                `</div>

`                `<div class="bg-gray-50 rounded-lg p-4">

`                  `<div class="flex justify-between items-center">

`                    `<span class="text-sm font-medium text-gray-500">Active Minutes</span>

`                    `<span class="text-lg font-bold text-indigo-600">187/150</span>

`                  `</div>

`                  `<div class="w-full bg-gray-200 rounded-full h-2 mt-2">

`                    `<div class="bg-indigo-600 h-2 rounded-full" style="width: 100%"></div>

`                  `</div>

`                `</div>

`              `</div>

`            `</div>

`          `</div>

`          `<!-- Activity Timeline -->

`          `<div class="mt-10">

`            `<h3 class="text-lg font-medium text-gray-900 mb-4">Recent Activity</h3>

`            `<div class="flow-root">

`              `<ul class="-mb-8">

`                `<li>

`                  `<div class="relative pb-8">

`                    `<span class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true"></span>

`                    `<div class="relative flex space-x-3">

`                      `<div>

`                        `<span

`                          `class="h-8 w-8 rounded-full bg-green-500 flex items-center justify-center ring-8 ring-white">

`                          `<i data-lucide="check" class="h-5 w-5 text-white"></i>

`                        `</span>

`                      `</div>

`                      `<div class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4">

`                        `<div>

`                          `<p class="text-sm text-gray-500">

`                            `Completed <span class="font-medium text-gray-900">Upper Body Strength</span> workout

`                          `</p>

`                        `</div>

`                        `<div class="text-right text-sm whitespace-nowrap text-gray-500">

`                          `<time>2h ago</time>

`                        `</div>

`                      `</div>

`                    `</div>

`                  `</div>

`                `</li>

`                `<li>

`                  `<div class="relative pb-8">

`                    `<span class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true"></span>

`                    `<div class="relative flex space-x-3">

`                      `<div>

`                        `<span

`                          `class="h-8 w-8 rounded-full bg-blue-500 flex items-center justify-center ring-8 ring-white">

`                          `<i data-lucide="droplet" class="h-5 w-5 text-white"></i>

`                        `</span>

`                      `</div>

`                      `<div class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4">

`                        `<div>

`                          `<p class="text-sm text-gray-500">

`                            `Reached <span class="font-medium text-gray-900">80%</span> of daily water goal

`                          `</p>

`                        `</div>

`                        `<div class="text-right text-sm whitespace-nowrap text-gray-500">

`                          `<time>6h ago</time>

`                        `</div>

`                      `</div>

`                    `</div>

`                  `</div>

`                `</li>

`                `<li>

`                  `<div class="relative pb-8">

`                    `<div class="relative flex space-x-3">

`                      `<div>

`                        `<span

`                          `class="h-8 w-8 rounded-full bg-purple-500 flex items-center justify-center ring-8 ring-white">

`                          `<i data-lucide="activity" class="h-5 w-5 text-white"></i>

`                        `</span>

`                      `</div>

`                      `<div class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4">

`                        `<div>

`                          `<p class="text-sm text-gray-500">

`                            `New personal record: <span class="font-medium text-gray-900">5K Run (22:45)</span>

`                          `</p>

`                        `</div>

`                        `<div class="text-right text-sm whitespace-nowrap text-gray-500">

`                          `<time>Yesterday</time>

`                        `</div>

`                      `</div>

`                    `</div>

`                  `</div>

`                `</li>

`              `</ul>

`            `</div>

`          `</div>

`        `</div>

`      `</div>

`    `</div>

`  `</section>

`  `<!-- Footer -->

`  `<footer class="bg-gray-800 text-white">

`    `<div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8">

`      `<div class="xl:grid xl:grid-cols-3 xl:gap-8">

`        `<div class="space-y-8 xl:col-span-1">

`          `<span class="text-2xl font-bold">PoseFit</span>

`          `<p class="text-gray-300 text-base">

`            `Transforming fitness through technology and personalization.

`          `</p>

`          `<div class="flex space-x-6">

`            `<a href="#" class="text-gray-400 hover:text-white">

`              `<span class="sr-only">Facebook</span>

`              `<i data-lucide="facebook" class="h-6 w-6"></i>

`            `</a>

`            `<a href="#" class="text-gray-400 hover:text-white">

`              `<span class="sr-only">Instagram</span>

`              `<i data-lucide="instagram" class="h-6 w-6"></i>

`            `</a>

`            `<a href="#" class="text-gray-400 hover:text-white">

`              `<span class="sr-only">Twitter</span>

`              `<i data-lucide="twitter" class="h-6 w-6"></i>

`            `</a>

`          `</div>

`        `</div>

`        `<div class="mt-12 grid grid-cols-2 gap-8 xl:mt-0 xl:col-span-2">

`          `<div class="md:grid md:grid-cols-2 md:gap-8">

`            `<div>

`              `<h3 class="text-sm font-semibold uppercase tracking-wider">

`                `Features

`              `</h3>

`              `<ul class="mt-4 space-y-4">

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Pose Analysis</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Nutrition Plans</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Water Tracking</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Workout Plans</a>

`                `</li>

`              `</ul>

`            `</div>

`            `<div class="mt-12 md:mt-0">

`              `<h3 class="text-sm font-semibold uppercase tracking-wider">

`                `Support

`              `</h3>

`              `<ul class="mt-4 space-y-4">

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">FAQ</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Contact Us</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Privacy Policy</a>

`                `</li>

`                `<li>

`                  `<a href="#" class="text-base text-gray-300 hover:text-white">Terms of Service</a>

`                `</li>

`              `</ul>

`            `</div>

`          `</div>

`        `</div>

`      `</div>

`      `<div class="mt-12 border-t border-gray-700 pt-8">

`        `<p class="text-base text-gray-400 xl:text-center">

`          `&copy; 2025 PoseFit. All rights reserved.

`        `</p>

`      `</div>

`    `</div>

`  `</footer>

`  `<script>

`    `// Initialize Lucide icons

`    `lucide.createIcons();

`    `// Initialize the progress chart

`    `const ctx = document.getElementById('progressChart').getContext('2d');

`    `const progressChart = new Chart(ctx, {

`      `type: 'line',

`      `data: {

`        `labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],

`        `datasets: [

`          `{

`            `label: 'Workouts Completed',

`            `data: [8, 12, 18, 15, 22, 25],

`            `borderColor: 'rgb(99, 102, 241)',

`            `backgroundColor: 'rgba(99, 102, 241, 0.1)',

`            `tension: 0.3,

`            `fill: true

`          `},

`          `{

`            `label: 'Average Intensity',

`            `data: [5.2, 5.8, 6.3, 6.7, 7.2, 7.8],

`            `borderColor: 'rgb(168, 85, 247)',

`            `backgroundColor: 'rgba(168, 85, 247, 0.1)',

`            `tension: 0.3,

`            `fill: true

`          `}

`        `]

`      `},

`      `options: {

`        `responsive: true,

`        `maintainAspectRatio: false,

`        `scales: {

`          `y: {

`            `beginAtZero: true,

`            `grid: {

`              `drawBorder: false

`            `}

`          `},

`          `x: {

`            `grid: {

`              `display: false

`            `}

`          `}

`        `},

`        `plugins: {

`          `legend: {

`            `position: 'bottom'

`          `}

`        `}

`      `}

`    `});

`    `// Smooth scrolling for anchor links

`    `document.querySelectorAll('a[href^="#"]').forEach(anchor => {

`      `anchor.addEventListener('click', function (e) {

`        `e.preventDefault();

`        `const targetId = this.getAttribute('href');

`        `const targetElement = document.querySelector(targetId);

`        `const navHeight = document.querySelector('nav').offsetHeight;

`        `if (targetElement) {

`          `window.scrollTo({

`            `top: targetElement.offsetTop - navHeight,

`            `behavior: 'smooth'

`          `});

`        `}

`      `});

`    `});

`  `</script>

</body>

</html>


LOGINPAGE –login.html

<!DOCTYPE html>

<html lang="en">

<head>

`  `<meta charset="UTF-8">

`  `<meta name="viewport" content="width=device-width, initial-scale=1.0">

`  `<title>PoseFit - Login</title>

`  `<!-- Tailwind CSS -->

`  `<script src="https://cdn.tailwindcss.com"></script>

`  `<style>

`    `@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

`    `body {

`      `font-family: 'Montserrat', sans-serif;

`    `}

`  `</style>

</head>

<body class="bg-gray-50 flex items-center justify-center min-h-screen">

`  `<div class="bg-white p-8 rounded-lg shadow-lg w-96">

`    `<div class="text-center mb-6">

`      `<span class="text-indigo-600 text-2xl font-bold">PoseFit</span>

`      `<h2 class="text-xl font-bold mt-4">Login to PoseFit</h2>

`    `</div>

`    `<form id="login-form" action="/login" method="POST">

`      `<div class="mb-4">

`        `<label for="email" class="block text-sm font-medium text-gray-700">Email:</label>

`        `<input type="email" id="email" name="email" required class="w-full px-3 py-2 border rounded-md mt-1">

`      `</div>

`      `<div class="mb-6">

`        `<label for="password" class="block text-sm font-medium text-gray-700">Password:</label>

`        `<input type="password" id="password" name="password" required class="w-full px-3 py-2 border rounded-md mt-1">

`      `</div>

`      `<button type="submit" class="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700">

`        `Login

`      `</button>

`    `</form>

`    `<div id="login-error" class="mt-3 text-red-600 text-sm hidden"></div>

`    `<div class="mt-4 text-center">

`      `<p class="text-sm text-gray-600">

`        `Don't have an account? <a href="/signup" class="text-indigo-600 hover:text-indigo-800">Sign Up</a>

`      `</p>

`    `</div>

`  `</div>

`  `<script>

`    `document.getElementById('login-form').addEventListener('submit', async function (event) {

`      `event.preventDefault();

`      `const email = document.getElementById('email').value;

`      `const password = document.getElementById('password').value;

`      `const errorElement = document.getElementById('login-error');

`      `try {

`        `const response = await fetch('/login', {

`          `method: 'POST',

`          `headers: {

`            `'Content-Type': 'application/x-www-form-urlencoded'

`          `},

`          `body: new URLSearchParams({ email: email, password: password })

`        `});

`        `// Get the response as JSON

`        `const result = await response.json();

`        `if (result.success) {

`          `localStorage.setItem('loggedInUser', email);

`          `window.location.href = '/dashboard'; // Redirect to dashboard after successful login

`        `} else {

`          `errorElement.textContent = "Invalid email or password!";

`          `errorElement.classList.remove('hidden');

`        `}

`      `} catch (error) {

`        `console.error('Login error:', error);

`        `errorElement.textContent = "An error occurred during login.";

`        `errorElement.classList.remove('hidden');

`      `}

`    `});

`  `</script>

</body>

</html>


SIGNUPAGE –Signup.html


<!DOCTYPE html>

<html lang="en">

<head>

`  `<meta charset="UTF-8" />

`  `<meta name="viewport" content="width=device-width, initial-scale=1.0" />

`  `<title>Sign Up - PoseFit</title>

`  `<script src="https://cdn.tailwindcss.com"></script>

</head>

<body class="bg-gray-50">

`  `<div class="max-w-md mx-auto mt-10 bg-white p-8 rounded shadow">

`    `<h2 class="text-2xl font-bold mb-6">Sign Up</h2>

`    `<form action="/signup" method="post" class="space-y-4">

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="name">Name</label>

`        `<input type="text" id="name" name="name" required class="mt-1 block w-full border-gray-300 rounded-md">

`      `</div>

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="email">Email</label>

`        `<input type="email" id="email" name="email" required class="mt-1 block w-full border-gray-300 rounded-md">

`      `</div>

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="age">Age</label>

`        `<input type="number" id="age" name="age" required class="mt-1 block w-full border-gray-300 rounded-md">

`      `</div>

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="gender">Gender</label>

`        `<select id="gender" name="gender" required class="mt-1 block w-full border-gray-300 rounded-md">

`          `<option value="">Select Gender</option>

`          `<option value="Male">Male</option>

`          `<option value="Female">Female</option>

`          `<option value="Other">Other</option>

`        `</select>

`      `</div>

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="password">Password</label>

`        `<input type="password" id="password" name="password" required class="mt-1 block w-full border-gray-300 rounded-md">

`      `</div>

`      `<div>

`        `<label class="block text-sm font-medium text-gray-700" for="weight">Weight (kg)</label>

`        `<input type="number" step="any" id="weight" name="weight" required class="mt-1 block w-full border-gray-300 rounded-md">

`      `</div>

`      `<div>

`        `<button type="submit" class="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700">Sign Up</button>

`      `</div>

`    `</form>

`  `</div>

</body>

</html>




FITNESS TRACKING BACKEND – model.py

import cv2

import mediapipe as mp

import numpy as np

\# Initialize MediaPipe

mp\_holistic = mp.solutions.holistic

mp\_drawing = mp.solutions.drawing\_utils

def calculate\_angle(a, b, c):

`    `"""

`    `Calculate angle between three points

`    `Args:

`        `a: first point [x, y]

`        `b: mid point [x, y]

`        `c: end point [x, y]

`    `Returns:

`        `angle in degrees

`    `"""

`    `a = np.array(a)

`    `b = np.array(b)

`    `c = np.array(c)



`    `radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])

`    `angle = np.abs(radians \* 180.0 / np.pi)



`    `if angle > 180.0:

`        `angle = 360 - angle



`    `return angle

\# Initialize Variables

counter = 0

stage = None

started = False

prev\_angle = 0

\# Thresholds

CURL\_DOWN\_ANGLE = 150  # Angle when arm is extended

CURL\_UP\_ANGLE = 70    # Angle when arm is curled

SMOOTHING\_FACTOR = 0.5  # For angle smoothing

\# Video capture

cap = cv2.VideoCapture(0)

with mp\_holistic.Holistic(

`    `min\_detection\_confidence=0.7,

`    `min\_tracking\_confidence=0.7) as holistic:

`    `while cap.isOpened():

`        `ret, frame = cap.read()

`        `if not ret:

`            `break



`        `# Convert BGR to RGB

`        `image = cv2.cvtColor(frame, cv2.COLOR\_BGR2RGB)



`        `# Make detection

`        `results = holistic.process(image)



`        `# Convert back to BGR

`        `image = cv2.cvtColor(image, cv2.COLOR\_RGB2BGR)



`        `# Extract landmarks

`        `try:

`            `if results.pose\_landmarks:

`                `# Get coordinates for right arm

`                `shoulder = [results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_SHOULDER].x,

`                          `results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_SHOULDER].y]

`                `elbow = [results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_ELBOW].x,

`                        `results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_ELBOW].y]

`                `wrist = [results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_WRIST].x,

`                        `results.pose\_landmarks.landmark[mp\_holistic.PoseLandmark.RIGHT\_WRIST].y]



`                `# Calculate angle with smoothing

`                `current\_angle = calculate\_angle(shoulder, elbow, wrist)

`                `smoothed\_angle = (current\_angle \* SMOOTHING\_FACTOR) + (prev\_angle \* (1 - SMOOTHING\_FACTOR))

`                `angle = smoothed\_angle

`                `prev\_angle = angle



`                `# Improved rep counting logic

`                `if not started and angle > CURL\_DOWN\_ANGLE:

`                    `started = True

`                    `stage = 'down'



`                `if started:

`                    `if stage == 'down' and angle < CURL\_UP\_ANGLE:

`                        `stage = 'up'

`                    `elif stage == 'up' and angle > CURL\_DOWN\_ANGLE:

`                        `stage = 'down'

`                        `counter += 1



`                `# Visual feedback

`                `color = (255, 0, 0) if stage == 'down' else (0, 255, 0)



`                `# Draw arm angle

`                `cv2.putText(image, f'Angle: {int(angle)}', 

`                           `(10, 30), 

`                           `cv2.FONT\_HERSHEY\_SIMPLEX, 1, color, 2)



`                `# Draw landmarks with custom style

`                `mp\_drawing.draw\_landmarks(

`                    `image,

`                    `results.pose\_landmarks,

`                    `mp\_holistic.POSE\_CONNECTIONS,

`                    `mp\_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle\_radius=2),

`                    `mp\_drawing.DrawingSpec(color=(245, 66, 230), thickness=2))



`        `except Exception as e:

`            `print(f"Error: {e}")

`            `pass



`        `# Display counter and stage

`        `cv2.putText(image, f'Reps: {counter}', 

`                    `(10, 80), 

`                    `cv2.FONT\_HERSHEY\_SIMPLEX, 1, (255, 255, 255), 2)

`        `cv2.putText(image, f'Stage: {stage}', 

`                    `(10, 130), 

`                    `cv2.FONT\_HERSHEY\_SIMPLEX, 1, (255, 255, 255), 2)



`        `# Add instruction text

`        `cv2.putText(image, 'Stand sideways to camera', 

`                    `(10, image.shape[0] - 60), 

`                    `cv2.FONT\_HERSHEY\_SIMPLEX, 0.7, (0, 255, 0), 2)

`        `cv2.putText(image, 'Press q to quit', 

`                    `(10, image.shape[0] - 30), 

`                    `cv2.FONT\_HERSHEY\_SIMPLEX, 0.7, (0, 255, 0), 2)



`        `# Show image

`        `cv2.imshow('Bicep Curl Counter', image)



`        `# Break loop

`        `if cv2.waitKey(10) & 0xFF == ord('q'):

`            `break

cap.release()

cv2.destroyAllWindows()


FITNESS CHATBOT- app.py

from flask import Flask, request, jsonify, render\_template

import os

from dotenv import load\_dotenv

from flask\_cors import CORS

import traceback

\# Load environment variables

load\_dotenv()

\# Check if API key is present

if not os.getenv('GROQ\_API\_KEY'):

`    `print("Warning: GROQ\_API\_KEY not found in environment variables")

app = Flask(\_\_name\_\_)

CORS(app)

\# Initialize nutrition agent

try:

`    `from phi.agent import Agent

`    `from phi.model.groq import Groq

`    `from phi.tools.wikipedia import WikipediaTools

`    `from phi.tools.duckduckgo import DuckDuckGo

`    `nutrition\_agent = Agent(

`        `name="Nutrition Diet Planner Agent",

`        `model=Groq(id="meta-llama/llama-4-maverick-17b-128e-instruct"),

`        `tools=[

`            `WikipediaTools(),

`            `DuckDuckGo()

`        `],

`        `instructions=[

`            `"ALWAYS respond using proper markdown formatting for all structured content.",

`            `"Use bullet points for lists and steps.",

`            `"Format headings using ## symbols.",

`            `"Use \*\*bold\*\* for important terms and metrics.",

`            `"Separate sections with horizontal rules (---)",

`            `"You are a certified nutrition specialist and diet planner with expertise in human nutrition, dietary sciences, and wellness.",

`            `"Create personalized meal plans based on user's goals, preferences, allergies, medical conditions, and dietary patterns.",

`            `"Always present meal plans and schedules in well-structured tables.",

`            `"Ask for key information if not provided: age, weight, height, gender, activity level, dietary preferences, medical conditions, food allergies, and specific goals.",

`            `"Calculate personalized caloric and macronutrient needs based on user information.",

`            `"Provide nutritional guidance for health goals like weight loss, muscle gain, energy boosting, or medical condition support.",

`            `"Suggest food item substitutions if necessary based on preferences or restrictions.",

`            `"Include recovery strategies such as hydration, gut health support, and mindful eating.",

`            `"Use markdown formatting to enhance readability of your responses.",

`            `"Cite reputable sources for any specific claims or dietary recommendations.",

`            `"Prioritize user safety and recommend professional consultation when appropriate.",

`            `"Track user progress and adjust plans based on feedback.",

`            `"Include measurement units in both metric and imperial when relevant.",

`            `"ONLY provide answers related to nutrition, dietary science, wellness, and human health.",

`            `"If a question is unrelated to nutrition or health, dont give any asnwers just respond with: '⚠️ I am a Nutrition and Health Specialist AI Agent. Please ask questions related only to nutrition, diet, or health-related wellness topics.'",

`        `],

`        `show\_tool\_calls=False,

`        `markdown=True,

`    `)

`    `print("Successfully initialized nutrition agent")

except Exception as e:

`    `print(f"Error initializing nutrition agent: {str(e)}")

`    `print(traceback.format\_exc())

`    `nutrition\_agent = None

\# Serve the frontend

@app.route('/')

def index():

`    `return render\_template('index.html')

\# Chatbot endpoint

@app.route('/chat', methods=['POST'])

def chat():

`    `try:

`        `# Check if nutrition\_agent was properly initialized

`        `if nutrition\_agent is None:

`            `return jsonify({'response': 'The nutrition agent failed to initialize. Check server logs.'}), 500

`        `data = request.json

`        `if not data:

`            `return jsonify({'response': 'No data received'}), 400

`        `user\_message = data.get('message', '')

`        `if not user\_message:

`            `return jsonify({'response': 'Please provide a message'}), 400

`        `# Get response from nutrition agent

`        `print(f"Processing message: {user\_message}")

`        `response\_obj = nutrition\_agent.run(user\_message)

`        `# Extract the string content from the RunResponse object

`        `print(f"Response type: {type(response\_obj)}")

`        `if hasattr(response\_obj, 'content'):

`            `response\_text = response\_obj.content

`        `elif hasattr(response\_obj, 'text'):

`            `response\_text = response\_obj.text

`        `elif hasattr(response\_obj, '\_\_str\_\_'):

`            `response\_text = str(response\_obj)

`        `else:

`            `response\_text = "Received a response from the AI but couldn't extract the text content."

`        `print(f"Response extracted: {response\_text[:100]}...")  # Print first 100 chars

`        `# Return the response

`        `return jsonify({'response': response\_text})

`    `except Exception as e:

`        `error\_traceback = traceback.format\_exc()

`        `print(f"Error in /chat endpoint: {str(e)}")

`        `print(error\_traceback)

`        `return jsonify({'response': f'Server error: {str(e)}. Please check server logs for details.'}), 500

if \_\_name\_\_ == '\_\_main\_\_':

`    `# Run the app

`    `app.run(debug=True, port=3001)


**

INURY HISTORY BACKEND – injury.py

from flask import Flask, request, jsonify, render\_template

import mysql.connector

app = Flask(\_\_name\_\_)

\# DB connection function

def get\_db\_connection():

`    `return mysql.connector.connect(

`        `host="localhost",

`        `user="root",

`        `password="root",

`        `database="pose"

`    `)

@app.route('/')

def index():

`    `return render\_template('index.html')  # Serve the index.html form

\# POST route for adding injury records

@app.route('/add\_injury', methods=['POST'])

def add\_injury():

`    `data = request.get\_json()

`    `user\_id = data.get('user\_id')

`    `injury\_type = data.get('injury\_type')

`    `recovery\_status = data.get('recovery\_status')

`    `if not injury\_type or not recovery\_status:

`        `return jsonify({'error': 'Missing required fields'}), 400

`    `try:

`        `conn = get\_db\_connection()

`        `cursor = conn.cursor()

`        `query = """

`            `INSERT INTO INJURY\_HISTORY (user\_id, injury\_type, recovery\_status)

`            `VALUES (%s, %s, %s)

`        `"""

`        `cursor.execute(query, (user\_id, injury\_type, recovery\_status))

`        `conn.commit()

`        `cursor.close()

`        `conn.close()

`        `return jsonify({'message': 'Injury record added successfully'}), 201

`    `except Exception as e:

`        `return jsonify({'error': str(e)}), 500

@app.route('/get\_injuries/<int:user\_id>', methods=['GET'])

def get\_injuries(user\_id):

`    `try:

`        `conn = get\_db\_connection()

`        `cursor = conn.cursor(dictionary=True)

`        `cursor.execute("""

`            `SELECT injury\_id, injury\_type, recovery\_status

`            `FROM INJURY\_HISTORY

`            `WHERE user\_id = %s

`        `""", (user\_id,))

`        `records = cursor.fetchall()

`        `cursor.close()

`        `conn.close()

`        `return jsonify(records)

`    `except Exception as e:

`        `return jsonify({'error': str(e)}), 500

if \_\_name\_\_ == '\_\_main\_\_':

`    `app.run(debug=True, port=5002)




MENTAL WELLNESS BACKEDN – wellapp.py

from flask import Flask, render\_template, request, jsonify

import mysql.connector

from datetime import datetime

app = Flask(\_\_name\_\_, static\_folder="static", template\_folder="templates")

\# MySQL Configuration

db\_config = {

`    `'host': 'localhost',

`    `'user': 'root',  # Replace with your MySQL username

`    `'password': 'root',  # Replace with your MySQL password

`    `'database': 'pose'  # Replace with your database name

}

@app.route('/')

def index():

`    `return render\_template('index.html')

@app.route('/submit\_booking', methods=['POST'])

def submit\_booking():

`    `try:

`        `# Get form data

`        `name = request.form.get('name')

`        `email = request.form.get('email')

`        `phone = request.form.get('phone')

`        `preferred\_date = request.form.get('date')

`        `preferred\_time = request.form.get('time')

`        `topic = request.form.get('topic')



`        `# Connect to MySQL database

`        `conn = mysql.connector.connect(\*\*db\_config)

`        `cursor = conn.cursor()



`        `# Insert data into wellness\_appointments table

`        `insert\_query = """

`        `INSERT INTO wellness\_appointments 

`        `(full\_name, email\_address, phone\_number, preferred\_date, preferred\_time, discussion\_topic) 

`        `VALUES (%s, %s, %s, %s, %s, %s)

`        `"""



`        `cursor.execute(insert\_query, (

`            `name, 

`            `email, 

`            `phone, 

`            `preferred\_date, 

`            `preferred\_time, 

`            `topic

`        `))



`        `# Commit the transaction

`        `conn.commit()



`        `# Close connection

`        `cursor.close()

`        `conn.close()



`        `return jsonify({"success": True, "message": "Booking submitted successfully!"})



`    `except Exception as e:

`        `return jsonify({"success": False, "message": f"Error: {str(e)}"})

if \_\_name\_\_ == '\_\_main\_\_':

`    `app.run(debug=True, port=5001)







NUTRITION CHATBOT – app.py

from flask import Flask, request, jsonify, render\_template

import os

from dotenv import load\_dotenv

from flask\_cors import CORS

import traceback

\# Load environment variables

load\_dotenv()

\# Check if API key is present

if not os.getenv('GROQ\_API\_KEY'):

`    `print("Warning: GROQ\_API\_KEY not found in environment variables")

app = Flask(\_\_name\_\_)

CORS(app)

\# Initialize nutrition agent

try:

`    `from phi.agent import Agent

`    `from phi.model.groq import Groq

`    `from phi.tools.wikipedia import WikipediaTools

`    `from phi.tools.duckduckgo import DuckDuckGo

`    `nutrition\_agent = Agent(

`        `name="Nutrition Diet Planner Agent",

`        `model=Groq(id="meta-llama/llama-4-maverick-17b-128e-instruct"),

`        `tools=[

`            `WikipediaTools(),

`            `DuckDuckGo()

`        `],

`        `instructions=[

`            `"ALWAYS respond using proper markdown formatting for all structured content.",

`            `"ONLY provide answers related to nutrition, dietary science, wellness, and human health.",

`            `"If a question is unrelated to nutrition or health, dont give any asnwers just respond with: '⚠️ I am a Nutrition and Health Specialist AI Agent. Please ask questions related only to nutrition, diet, or health-related wellness topics.'",

`            `"Use bullet points for lists and steps.",

`            `"Format headings using ## symbols.",

`            `"Use \*\*bold\*\* for important terms and metrics.",

`            `"Separate sections with horizontal rules (---)",

`            `"You are a certified nutrition specialist and diet planner with expertise in human nutrition, dietary sciences, and wellness.",

`            `"Create personalized meal plans based on user's goals, preferences, allergies, medical conditions, and dietary patterns.",

`            `"Always present meal plans and schedules in well-structured tables.",

`            `"Ask for key information if not provided: age, weight, height, gender, activity level, dietary preferences, medical conditions, food allergies, and specific goals.",

`            `"Calculate personalized caloric and macronutrient needs based on user information.",

`            `"Provide nutritional guidance for health goals like weight loss, muscle gain, energy boosting, or medical condition support.",

`            `"Suggest food item substitutions if necessary based on preferences or restrictions.",

`            `"Include recovery strategies such as hydration, gut health support, and mindful eating.",

`            `"Use markdown formatting to enhance readability of your responses.",

`            `"Cite reputable sources for any specific claims or dietary recommendations.",

`            `"Prioritize user safety and recommend professional consultation when appropriate.",

`            `"Track user progress and adjust plans based on feedback.",

`            `"Include measurement units in both metric and imperial when relevant.",

`        `],

`        `show\_tool\_calls=False,

`        `markdown=True,

`    `)

`    `print("Successfully initialized nutrition agent")

except Exception as e:

`    `print(f"Error initializing nutrition agent: {str(e)}")

`    `print(traceback.format\_exc())

`    `nutrition\_agent = None

\# Serve the frontend

@app.route('/')

def index():

`    `return render\_template('index.html')

\# Chatbot endpoint

@app.route('/chat', methods=['POST'])

def chat():

`    `try:

`        `# Check if nutrition\_agent was properly initialized

`        `if nutrition\_agent is None:

`            `return jsonify({'response': 'The nutrition agent failed to initialize. Check server logs.'}), 500

`        `data = request.json

`        `if not data:

`            `return jsonify({'response': 'No data received'}), 400

`        `user\_message = data.get('message', '')

`        `if not user\_message:

`            `return jsonify({'response': 'Please provide a message'}), 400

`        `# Get response from nutrition agent

`        `print(f"Processing message: {user\_message}")

`        `response\_obj = nutrition\_agent.run(user\_message)

`        `# Extract the string content from the RunResponse object

`        `print(f"Response type: {type(response\_obj)}")

`        `if hasattr(response\_obj, 'content'):

`            `response\_text = response\_obj.content

`        `elif hasattr(response\_obj, 'text'):

`            `response\_text = response\_obj.text

`        `elif hasattr(response\_obj, '\_\_str\_\_'):

`            `response\_text = str(response\_obj)

`        `else:

`            `response\_text = "Received a response from the AI but couldn't extract the text content."

`        `print(f"Response extracted: {response\_text[:100]}...")  # Print first 100 chars

`        `# Return the response

`        `return jsonify({'response': response\_text})

`    `except Exception as e:

`        `error\_traceback = traceback.format\_exc()

`        `print(f"Error in /chat endpoint: {str(e)}")

`        `print(error\_traceback)

`        `return jsonify({'response': f'Server error: {str(e)}. Please check server logs for details.'}), 500

if \_\_name\_\_ == '\_\_main\_\_':

`    `# Run the app

`    `app.run(debug=True, port=3012)








CHALLENGES BACKEND – app.py

from flask import Flask, jsonify, render\_template, send\_from\_directory

import os

import json

from datetime import datetime

app = Flask(\_\_name\_\_, static\_folder='static', template\_folder='templates')

\# File to store challenges

CHALLENGES\_FILE = 'data/challenges.json'

\# Ensure data directory exists

if not os.path.exists('data'):

`    `os.makedirs('data')

\# Initialize challenges or load existing ones

def init\_challenges():

`    `create\_new\_challenges = True



`    `if os.path.exists(CHALLENGES\_FILE):

`        `try:

`            `with open(CHALLENGES\_FILE, 'r') as f:

`                `challenges = json.load(f)



`            `# Verify the challenges data is valid and not empty

`            `if challenges and isinstance(challenges, list) and len(challenges) > 0:

`                `if isinstance(challenges[0], dict) and "date" in challenges[0]:

`                    `# Valid challenges exist

`                    `create\_new\_challenges = False



`                    `# Update the date to today to refresh challenges

`                    `today = datetime.now().strftime("%Y-%m-%d")

`                    `if challenges[0]["date"] != today:

`                        `for challenge in challenges:

`                            `challenge["date"] = today



`                        `with open(CHALLENGES\_FILE, 'w') as f:

`                            `json.dump(challenges, f)

`        `except (json.JSONDecodeError, KeyError, IndexError):

`            `# If any error occurs while reading or processing the file,

`            `# we'll create new challenges

`            `pass



`    `if create\_new\_challenges:

`        `# Sample daily challenges

`        `challenges = [

`            `{

`                `"id": "d1",

`                `"title": "Morning Stretch",

`                `"description": "Complete a 10-minute morning stretch routine to increase flexibility.",

`                `"points": 10,

`                `"difficulty": "Easy",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `},

`            `{

`                `"id": "d2",

`                `"title": "10,000 Steps",

`                `"description": "Walk at least 10,000 steps today to improve cardiovascular health.",

`                `"points": 15,

`                `"difficulty": "Medium",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `},

`            `{

`                `"id": "d3",

`                `"title": "Hydration Hero",

`                `"description": "Drink at least 8 glasses of water throughout the day.",

`                `"points": 10,

`                `"difficulty": "Easy",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `},

`            `{

`                `"id": "d4",

`                `"title": "HIIT Workout",

`                `"description": "Complete a 20-minute high intensity interval training session.",

`                `"points": 25,

`                `"difficulty": "Hard",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `},

`            `{

`                `"id": "d5",

`                `"title": "Healthy Meal",

`                `"description": "Prepare and eat a balanced, nutritious meal with protein, vegetables, and whole grains.",

`                `"points": 15,

`                `"difficulty": "Medium",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `},

`            `{

`                `"id": "d6",

`                `"title": "Mindful Meditation",

`                `"description": "Spend 10 minutes meditating to reduce stress and improve mental clarity.",

`                `"points": 10,

`                `"difficulty": "Easy",

`                `"date": datetime.now().strftime("%Y-%m-%d")

`            `}

`        `]



`        `with open(CHALLENGES\_FILE, 'w') as f:

`            `json.dump(challenges, f)



`    `return challenges

\# Routes

@app.route('/')

def index():

`    `return render\_template('index.html')

@app.route('/challenges')

def get\_challenges():

`    `challenges = init\_challenges()

`    `return jsonify(challenges)

\# Serve static files

@app.route('/static/<path:path>')

def send\_static(path):

`    `return send\_from\_directory('static', path)

if \_\_name\_\_ == '\_\_main\_\_':

`    `# Make sure the challenges file exists

`    `init\_challenges()

`    `app.run(debug=True, port=3009)















**RESULT AND DESCUSSION**




![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.044.png) 

Fig 7.1 frontend 



![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.045.png)

Fig 7.2 signup page





![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.046.png)

Fig 7.3 login page



![C:\Users\rohan\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\650F69C491959BAFE60C4FAD7D4FB7AC\WhatsApp Image 2025-05-05 at 22.40.47_0c44f801.jpg](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.047.jpeg)

Fig 7.4 fitness tracker (bicep curl)







![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.048.png)

Fig 7.5.1 mental wellness videos


![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.049.png)

Fig 7.5.2 mental wellness appointments






![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.050.png)

Fig 7.6.1 injury management 




![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.051.png)

Fig 7.6.2 injury history




![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.052.png)

Fig 7.7 nutrition chatbot



![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.053.png)

Fig 7.8 fitness chatbot



![](Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.054.png)

Fig 7.9  fitness challenges
86

[ref1]: Aspose.Words.e2a0e717-6590-4968-8f8e-caa0374cb6eb.019.png
