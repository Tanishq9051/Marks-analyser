import matplotlib.pyplot as plt

while True:
    try:
        n = int(input("enter the total number of students: "))
        if n>0:
            break
        else:
            print("please enter a number greater then zero")

    except ValueError:
        print("please enter a valid number.")

while True:
    try:
        physics_max = float(input("Enter the maximum marks of physics "))
        if physics_max > 0:
            break
        print("please enter a number greater then zero" )
    except ValueError:
        print("please enter a valid number")

while True:
    try:
        chemistry_max = float(input("Enter the maximum marks of chemistry "))
        if chemistry_max > 0:
            break
        print("please enter a number greater then zero" )
    except ValueError:
        print("please enter a valid number")

while True:
    try:
        biology_max = float(input("Enter the maximum marks of biology "))
        if biology_max > 0:
            break
        print("please enter a number greater then zero" )
    except ValueError:
        print("please enter a valid number")

names = []
physics = []
chemistry = []
biology = []

physics_percentages = []
chemistry_percentages = []
biology_percentages =[]
overall_percentage =[]


for i in range(n):
    print("\nStudents", i+1)

    name = (input("Enter your name "))

    while name == "":
        print("name can not be empty")
        name = input("enter your name")
    while True:
            try:   
                physics_marks = float(input("Enter your physics marks"))

                if 0<= physics_marks <= physics_max:
                    break
                else:
                    print("marks must be between 0 and ", physics_max)
            except ValueError:
                print("please enter a valid number")

    while True:
        try:   
            chemistry_marks = float(input("Enter your chemistry marks"))

            if 0<= chemistry_marks <= chemistry_max:
                break
            else:
                print("marks must be between 0 and ", chemistry_max)
        except ValueError:
            print("please enter a valid number")             


    while True:
        try:   
            biology_marks = float(input("Enter your biology marks"))
    
            if 0<= biology_marks <= biology_max:
                break
            else:
                print("marks must be between 0 and ", biology_max)
        except ValueError:
            print("please enter a valid number")             

    chemistry_marks = float(input("Enter your chemistry marks"))
    biology_marks = float(input("Enter your biology marks"))

    names.append(name)
    physics.append(physics_marks)
    chemistry.append(chemistry_marks)
    biology.append(biology_marks)

excellent_count = 0
very_good_count = 0
good_count = 0
average_count = 0
needs_improvement_count = 0


    
for i in range(n):
    physics_percentage = (physics[i]/physics_max)*100

    chemistry_percentage = (chemistry[i]/chemistry_max)*100

    biology_percentage = (biology[i]/biology_max)*100

    physics_percentages.append(physics_percentage)
    chemistry_percentages.append(chemistry_percentage)
    biology_percentages.append(biology_percentage)

    total_marks = physics[i] + chemistry[i] + biology[i]
    total_max = physics_max + chemistry_max + biology_max

    total_percentage = (total_marks/total_max)*100
    overall_percentage.append(total_percentage)

    if total_percentage >=90:
        peformance = "Excellent"
        excellent_count += 1

    elif total_percentage >=75:
        peformance = "very good" 
        very_good_count += 1

    elif total_percentage >=60:
        peformance = "good"
        good_count +=1

    elif total_percentage >=50:
        peformance = "average"  
        average_count +=1

    elif total_percentage <50:
        peformance = "needs improvement"
        needs_improvement_count +=1


    print("\n--- Peformance Report ---")
    print("Name:", names[i])
    print("Chemistry Percentage:", round(chemistry_percentage, 2), "%")
    print("Physics Percentage:", round(physics_percentage, 2), "%")
    print("Biology Percentage:", round(biology_percentage, 2), "%")
    print("Overall Percentage:", round(total_percentage, 2), "%")
    print("Remarks:", peformance)

ranking = sorted(range(n), key=lambda i: overall_percentage[i], reverse=True)    

print("\n--- Students Ranking ---")
for rank, i in enumerate(ranking, start=1):
    print(rank, names[i], "-", f"{overall_percentage[i]:.2f}", "%")

best_index = overall_percentage.index(max(overall_percentage))

print("\n--- Best student ---")
print("name:", names[best_index])
print("Percentage:", f"{overall_percentage[best_index]:.2f}%")

physics_average = sum(physics) / n
chemistry_average = sum(chemistry) / n
biology_average = sum(biology) / n
print("\n--- Subject wise average ---")
print("physics average: ", f"{physics_average:.2f}%")
print("chemistry average: ", f"{chemistry_average:.2f}%")
print("biology average: ", f"{biology_average:.2f}%")

class_average = sum(overall_percentage) / n
print("class average: ", f"{class_average:.2f}%")

if class_average >= 75:
    class_remark = "excellent class peformance"      
elif class_average >= 60:
    class_remark = "good class peformance"    
elif class_average >= 45:
    class_remark = "average class peformance"    
else:
    class_remark = "needs improvement"       

print("class remarks: ", class_remark)

plt.figure(figsize=(10, 5))
bars = plt.bar(names, overall_percentage)
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )
plt.xlabel("students")
plt.ylabel("overall percentage")
plt.title("class peformance comparision")
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()   

highest_percentage = max(overall_percentage)
lowest_percentage = min(overall_percentage)
print("\n=================================================")
print("          final peformance report")
print("\n=================================================")

print("\nClass overview")
print("total student: ", n)
print("class average: ", f"{class_average:.2f}%")
print("highest percentage: ", f"{highest_percentage:.2f}%")
print("lowest percentage: ", f"{lowest_percentage:.2f}%")

print("\n Top 3 students")
for rank, i in enumerate(ranking[:3], start=1):
    print(rank, names[i], "-", f"{overall_percentage[i]:.2f}%")

print("\nSUBJECT ANALISYS")
print("physics average: ", f"{physics_average:.2f}%")
print("chemistry average: ", f"{chemistry_average:.2f}%")
print("biology average: ", f"{biology_average:.2f}%")

subject_average = {
    "physics": physics_average,
    "chemistry": chemistry_average,
    "biology": biology_average
}

best_subject = max(subject_average, key=subject_average.get)
weakest_subject = min(subject_average, key=subject_average.get)

print("best subject: ", best_subject)
print("weakest subject: ", weakest_subject)

print("\nPEFORMANCE REPORT")
print("Excellent ", excellent_count)
print("very good ", very_good_count)
print("good", good_count)
print("average", average_count)
print("needs improvement", needs_improvement_count)

print("\n best student")
print("name: ", names[best_index])
print("percentage:", f"{overall_percentage[best_index]:.2f}%")

print("\nclass remark")

print("\n=======================================")
print("            end of report")
print("\n=======================================")


for i in range(n):
    subjects = ["physics", "chemistry", "biology"]
    percentages = [physics_percentages[i], chemistry_percentages[i], biology_percentages[i]]

    bars = plt.bar(subjects, percentages)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.2f}%", 
                ha="center",
                va="bottom"
                )
    plt.xlabel("subjects")
    plt.ylabel("percentagezs")
    plt.title("subject wise performance") 
    plt.show()