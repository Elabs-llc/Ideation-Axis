# List of people at Ideation Axis
ideation_db = [
    {"name": "Edwin", "position": "Intern @ Ideation Axis", "id": 22},
    {"name": "Joseph Nyarko", "position": "Facilitator @  Ideation Axis", "id": 25},
    {"name": "Esegbe Able Katapu", "position": "Facilitator @  Ideation Axis", "id": 25},
    {"name": "Philip Appiah Gyima", "position": "CEO @  Ideation Axis", "id": 35}
]

# Sort the list by id using a lambda function
sorted_interns = sorted(ideation_db, key=lambda intern: intern['id'])

# Print the sorted list
for intern in sorted_interns:
    if(intern["id"] == 22):
        print('Interns: \n')
        print(f"{intern['name']}: {intern['position']} | ID : {intern['id']}  \n")
    