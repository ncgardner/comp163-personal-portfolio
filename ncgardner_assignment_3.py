personal_info = {"Full name": "Nathan Gardner", "Student email": "ncgardner@aggies.ncat.edu","Hometown": "Reidsville, NC",
"Graduation semester": "Spring 2027", "Major": "Computer Science"}

current_courses = ["COMP 163", "MATH 104", "BIO 100","HIS 106"]
completed_courses = ["Public Speaking", "Chemistry", "Calculus", "Intro to Python"]
credit_hours = [3, 3, 4, 3]
GPA_history = [3.8, 3.9, 3.6, 3.7]
cumulative_GPA = (sum(GPA_history) / 4)

emergency_contacts = ("Mom", "Cameron Gardner", "336-999-9999")
home_address = ("274 Riverwood Drive", "Reidsville", "NC", "27214")
instagram_info = ("Instagram", "@nathan_gardner31", 900)
twitter_info = ("Twitter", "N/A", 0)
birthday = ("Birthday", "7", "06", "2004")

current_skills = {"Python basics", "Problem solving", "Time management", "Guitar", "Piano"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Public speaking", "Web design"}
career_interests = {"Software development", "Web development", "Game development"}
hobbies = {"Dancing", "Hunting", "Reading", "Fishing", "Music", "Golf"}
entertainment_backlog = {"Supernatural", "Breaking Bad", "The Walking Dead", "HIMYM", "New Girl"}

course_credits = {"COMP 163": 3, "MATH 104": 3, "BIO 100": 4, "HIS 106": 3}
course_prof = {"COMP 163": "Prof. Rhodes", "MATH 104": "Mrs. Nelson", 
"BIO 100": "Dr. Scott", "HIS 106": "Dr. Devoe"}
course_rooms = {"COMP 163": "Gibbs 337", "MATH 104": "Marteena 214", "BIO 100": "Barnes 110", 
"HIS 106": "Online"}
monthly_budget = {"Food": 300, "Entertainment": 100, "Books": 25, "Transportation": 400}
study_hours_per_subject = {"Programming": 3, "Math": 1, "Biology": 1, "History": 1}
contact_directory = {"Mom": "336-999-9999", "Roommate": "336-999-9998", "Academic Advisor": "336-999-9997"}

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {personal_info["Full name"]} | Email: {personal_info["Student email"]}")
print(f"From: {home_address[1]}, {home_address[2]} | Graduating: {personal_info["Graduation semester"]}")
print(f"Major: {personal_info["Major"]}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {sum(credit_hours)} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_GPA:.2f}")
print(f"Weekly Study Time: {sum(study_hours_per_subject.values())} hours")
print(f"Academic Investment: ${(monthly_budget["Books"] / sum(study_hours_per_subject.values())):.1f} per study hour\n")

print(f"""Current Courses:
{current_courses[0]} - {credit_hours[0]} credits - {course_prof["COMP 163"]} - {course_rooms["COMP 163"]}
{current_courses[1]} - {credit_hours[1]} credits - {course_prof["MATH 150"]} - {course_rooms["MATH 150"]}
{current_courses[2]} - {credit_hours[2]} credits - {course_prof["ENG 101"]} - {course_rooms["ENG 101"]}
{current_courses[3]} - {credit_hours[3]} credits - {course_prof["HIS 105"]} - {course_rooms["HIS 105"]}\n""")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${sum(monthly_budget.values())}")
print(f"Food: ${monthly_budget["Food"]} (${monthly_budget["Food"] / 30:.1f}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${(sum(monthly_budget.values()) * 12)}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contacts[1]} ({emergency_contacts[0]}) - {emergency_contacts[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {instagram_info[2] + twitter_info[2]} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory.keys())} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {sum(credit_hours) + sum(study_hours_per_subject.values())} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")




