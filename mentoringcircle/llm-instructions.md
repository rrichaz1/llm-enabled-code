## Experiment with prompts to generate code. 

Even with very simple prompts, got pretty good results. Additional tweaks needed to be done as the circle creation code did not account for circle already exists and hence add mentees to the circle. 


System Message

```You are an AI coding expert in Python data science libraries and proficient with NLP```




Scenario 1.
1. Get distinct value strings/phrases for a column where there are multiple semicolon delimited strings/phrases 

```
import pandas as pd  
  
# Create a sample DataFrame  
df = pd.DataFrame({'categories': ['Career in Data Analytics;Data Analytics Skill Development Resources;Networking;',  
                                  'Career in Data Science;Data Science Skill Development Resources;Machine Learning;',  
                                  'Career in Data Engineering;Data Engineering Skill Development Resources;Big Data;']})  
  
# Extract and split the strings in the 'categories' column  
df['categories'] = df['categories'].str.split(';')  
  
# Create an empty list to store the distinct values  
distinct_values = []  
  
# Iterate over each row in the DataFrame  
for row in df['categories']:  
    # Iterate over each category in the row  
    for category in row:  
        # Check if the category is not already in the distinct_values list  
        if category not in distinct_values:  
            # Append the category to the distinct_values list  
            distinct_values.append(category)  
  
# Print the distinct values  
print(distinct_values)  
```
This code splits the strings in the 'categories' column using the str.split() method. Then, it iterates over each row and each category in the row, checking if it's already in the distinct_values list. If not, it appends the category to the list. Finally, it prints the distinct values.

Note that in this example, the distinct values will be printed as a list.




2. I have 2 pandas dataframes one mentor and one mentee, I have some inclusion and exclusion criteria for matching multiple mentees to a mentor. How do I assign mentoring circles based on the best match where 1 mentor can have 8-9 mentees?

>>>
To assign mentoring circles based on the best match between a mentor and multiple mentees, you can use various techniques such as matching algorithms, scoring systems, or optimization methods. Here is a general approach you can follow:
Preprocess and clean the mentor and mentee dataframes, ensuring they have the necessary columns and consistent formats for the inclusion and exclusion criteria.
Define your inclusion and exclusion criteria. These could be specific attributes, skills, interests, or any other relevant factors that determine a good match between a mentor and mentee. Assign weights or importance factors to each criterion based on their relative significance.
Calculate a match score for each mentor-mentee pair based on the inclusion and exclusion criteria. You can use various techniques like similarity metrics, weighted scores, or rule-based systems to calculate these scores.
Sort the mentor-mentee pairs based on the match scores in descending order. This will help you identify the best matches first.
Iterate through the sorted mentor-mentee pairs and assign mentees to mentors based on the maximum number of mentees per mentor (8-9 in your case) and the match scores. Keep track of the assigned mentees and mentors to avoid duplicate assignments.
Continue the assignment process until all mentors have their maximum number of mentees or there are no more eligible mentees left.

Here's a high-level code snippet to illustrate this approach:

import pandas as pd  
  
# Preprocess and clean mentor and mentee dataframes  
  
# Define inclusion and exclusion criteria  
  
# Calculate match scores for mentor-mentee pairs  
  
# Sort mentor-mentee pairs based on match scores  
  
# Assign mentees to mentors based on maximum number of mentees per mentor and match scores  
```
mentoring_circles = []  
assigned_mentees = set()  
assigned_mentors = set()  
  
for _, row in sorted_pairs.iterrows():  
    mentor = row['mentor']  
    mentee = row['mentee']  
    if mentor not in assigned_mentors and mentee not in assigned_mentees:  
        if len(mentoring_circles) < num_mentors:  
            mentoring_circles.append({'mentor': mentor, 'mentees': [mentee]})  
            assigned_mentors.add(mentor)  
            assigned_mentees.add(mentee)  
        else:  
            for circle in mentoring_circles:  
                if len(circle['mentees']) < max_mentees_per_mentor:  
                    circle['mentees'].append(mentee)  
                    assigned_mentees.add(mentee)  
                    break  
  
# Print the mentoring circles  
for circle in mentoring_circles:  
    print(circle)  
```    
 
This is a simplified example, and you may need to adapt and customize the code based on your specific requirements and data structures.

**Prompt:** Create code snippet to merge and rank mentor and mentee dataframes

Here's a code snippet to merge mentor and mentee data frames using the merge() function in pandas:
```
import pandas as pd  
  
# Assume you have two data frames: mentor_df and mentee_df  
  
# Merge mentor and mentee data frames based on shared attributes or criteria  
merged_df = pd.merge(mentor_df, mentee_df, on='shared_attribute')  
  
# Print the merged data frame  
print(merged_df)  
```
 
In this code snippet, the merge() function is used to merge the mentor_df and mentee_df data frames based on a shared attribute or criteria. The on parameter specifies the column name on which the merge operation is performed. You need to replace 'shared_attribute' with the actual column name that represents the shared attribute between the mentor and mentee data frames.

The resulting merged data frame, merged_df, will contain all the columns from both the mentor and mentee data frames, where the rows are merged based on the shared attribute. You can further customize the merge operation by using additional parameters of the merge() function, such as how, left_on, right_on, etc., depending on your specific requirements.

Remember to adjust the code according to the actual column names and shared attributes in your mentor and mentee data frames.

**Prompt:** There is no shared attribute, i want to do a cross join of the dataframes and score each pair 

If there is no shared attribute between the mentor and mentee data frames, and you want to perform a cross join of the data frames and score each pair, you can create a dummy column in both data frames and perform the merge based on that. Here's an example code snippet:
```
import pandas as pd  
  
# Assume you have two data frames: mentor_df and mentee_df  
  
# Add a dummy column to both data frames  
mentor_df['dummy'] = 1  
mentee_df['dummy'] = 1  
  
# Perform a cross join by merging on the dummy column  
cross_join_df = pd.merge(mentor_df, mentee_df, on='dummy')  
  
# Remove the dummy column  
cross_join_df = cross_join_df.drop(columns=['dummy'])  
  
# Calculate the match score for each mentor-mentee pair  
# You can implement your own scoring algorithm or use any other method here  
  
# Print the resulting data frame with match scores  
print(cross_join_df)  
```
 
In this code snippet, a dummy column named 'dummy' is added to both the mentor and mentee data frames. The value of this column is set to 1 for all rows. The merge operation is then performed on this dummy column, resulting in a cross join of the two data frames. After merging, you can remove the dummy column if it is not needed in the final result.

Next, you can calculate the match score for each mentor-mentee pair using your scoring algorithm or any other method you prefer. You need to implement the scoring logic based on the attributes or criteria relevant to your case.

Finally, the resulting data frame with the match scores is printed.

Please note that a cross join can result in a large number of rows if the mentor and mentee data frames are large. Ensure that your system has enough memory and processing power to handle the resulting data frame.

