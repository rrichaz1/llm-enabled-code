## Purpose

The purpose of the repository is to create mentor-mentee circles. 





## Philospohy

**Scoring Criteria**
-Circle size - max circle size determined as Number of mentees/number of mentors
-Time Zones – Fit circles into similar time zones or within 2-hour differences. *International participants placed in eastern time zone groups.
-Mentees with experience level 8 years or less placed in Early Career otherwise in Mid career. Circles created with Mid career or Early Career
-Grade level - Mentor gradelevel to be higher than mentee gradelevel. Keep similar gradelevels together.
-Grwoth areas Sort – Mentors strengths match the Mentees growth areas.
-Areas of interest/Goals – Maximum match on areas of interest within a circle.

Mentor-mentee match score was created based on above and circles were assigned based on maximum match.


### About the code

1. The matching logic and goal similarity code was written using simple prompts to open AI GPT35 turbo model
2. Github Copilot aided in code syntax

### Areas for improvement

1. This is one shot matching. It can be refined to tweak the scores and apply Monte carlo simulation
2. Visualizations to show different circles



### Local Machine Setup Instructions
 

Python: Ensure that you have Python 3.x installed on your local machine. You can download and install it from the official Python website.
```brew upgrade pyenv``` 
``` pyenv install 3.11.7

Package Manager: You will need pip to install the required packages. It's typically included with the Python installation.
Virtual Environment (Optional): It's a good practice to create a virtual environment for your project to manage dependencies. You can create one using venv:

python3 -m venv mentorenv  
source mentorenv/bin/activate   
 
4. Install Libraries: Install the necessary libraries using pip in your virtual environment:
```pip install -r requirements.txt```  

5. Run the mentor_mentee_match.ipynb



