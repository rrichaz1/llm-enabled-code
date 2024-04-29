import numpy as np
import re
import pandas as pd




timezonemap ={'PHT':0,'IST': 1,'GMT': 2,'EST': 3, 'CST': 4, 'MST': 5, 'PST':6, 'XXX':99}



mentee_mentor_interest_crosswalk = {
'Networking':'Networking',
'Leadership Skills Development':'Develop Leadership Skills',
'Story Telling':'Learn Story Telling', 
'Business Acumen':'Business Acumen', 
'Career in Data Analytics': 'Career in Data Analytics', 
'Career Change': 'Career Change', 
'Communication Skills':'Communication Skills', 
'Career in Data Science':'Career in Data Science', 
'Personal Branding':'Create Personal Brand',
'Public Speaking':'Public Speaking',
'Data Science Skill Development Resources':'Data Science Skill Development Resources',}


mentor_mentee_interest_crosswalk = {
    'Networking': 'Networking', 
    'Develop Leadership Skills': 'Leadership Skills Development', 
    'Learn Story Telling': 'Story Telling', 
    'Business Acumen': 'Business Acumen',
    'Career in Data Analytics': 'Career in Data Analytics', 
    'Career Change': 'Career Change',
    'Communication Skills': 'Communication Skills', 
    'Career in Data Science': 'Career in Data Science', 
    'Create Personal Brand': 'Personal Branding', 
    'Public Speaking': 'Public Speaking', 
    'Data Science Skill Development Resources': 'Data Science Skill Development Resources',
    'Data Analytics Skill Development Resources': 'Data Analytics Skill Development Resources'
    }
#function to swap the keys and values of a dictionary mentee_mentor_interest_crosswalk
def swap_dict(dictionary):
    return {v: k for k, v in dictionary.items()}
 
 #function to assign numeric timezone to timezone acronym
def assignnumericTimeZone(timezone):
     #add try except block to handle exception if timezone acronym is not found
        timeZoneAcronym = 'XXX'
        try:
            timeZoneAcronym = re.search(r'\(([^)]+)', timezone).group(1)
        except:
            print('Timezone acronym not found for timezone: ', timezone)        
        return timezonemap[timeZoneAcronym]


#create a function that takes list of mentee interests and list of mentor interests, strips whitespaces, maps mentee interests to mentor interests in crosswalk and returns a count of intersection interests
def common_interests (mentor_interests, mentee_interests):
    mentee_interests = [x.strip() for x in mentee_interests if x != ''] 
    mentor_interests = [x.strip() for x in mentor_interests if x != '']
    mentee_interests_mapped = [mentor_mentee_interest_crosswalk[x] for x in mentee_interests if x in mentor_mentee_interest_crosswalk.keys()]
    interectionset=set(mentee_interests_mapped).intersection(set(mentor_interests))
    # print(interectionset)
    return interectionset

#create a function that takes mentor  and mentee , splits the s, subsets the last 3 s of mentee and first 3 s of mentor, and returns the matching s
def matchGrowth(mentor_, mentee_):
    mentor_s = mentor_.replace('"','').split(';')
    mentee_s = mentee_.replace('"','').split(';')
    #subset the last 3 s of mentee and first 3 s of mentor
    mentee_3 = [mentee for mentee in mentee_s if mentee] [-3:]
    mentor_3 = [mentor for mentor in mentor_s if mentor] [0:3]
    matching = set(mentee_3).intersection(set(mentor_3))
    return matching

#create main function to call the other functions
def main():
    print("Hello World!")
    print(swap_dict(mentee_mentor_interest_crosswalk))
    print(assignnumericTimeZone('Asia/Manila (PHT)'))
    mentor_interests = ['Networking', 'Leadership Skills Development', 'Story Telling', 'Business Acumen\xa0', '']
    mentee_interests= ['Develop Leadership Skills', 'Learn Story Telling', 'Career in Data Analytics', 'Business Acumen']
    common_interests(mentee_interests, mentor_interests)
    1='Communicating with Others;Taking Initiative and Risks;Growth Mindset;Collaborating;Using Time and Resources Effectively;Self-Management;Managing Ambiguity and Uncertainty;Developing Others;Influencing Others;Managing Conflict;'
    2='Self-Management;Collaborating;Using Time and Resources Effectively;Communicating with Others;Growth Mindset;Managing Conflict;Taking Initiative and Risks;Managing Ambiguity and Uncertainty;Influencing Others;Developing Others;'
    matchGrowth(1, 2) 
    



# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main()    