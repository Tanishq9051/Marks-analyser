print("===== MARKS ANALYSER V1 =====")

name = input("Enter student name: ")

physics_max = float(input("Enter Physics maximum marks: "))
chemistry_max = float(input("Enter Chemistry maximum marks: "))
biology_max = float(input("Enter Biology maximum marks: "))

physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))

physics_percentage = (physics / physics_max) * 100
chemistry_percentage = (chemistry / chemistry_max) * 100
biology_percentage = (biology / biology_max) * 100

total_marks = physics + chemistry + biology
total_maximum = physics_max + chemistry_max + biology_max

overall_percentage = (total_marks / total_maximum) * 100

print("\n===== RESULT =====")

print(f"Student: {name}")

print(
    f"Physics: {physics}/{physics_max} "
    f"({physics_percentage:.2f}%)"
)

print(
    f"Chemistry: {chemistry}/{chemistry_max} "
    f"({chemistry_percentage:.2f}%)"
)

print(
    f"Biology: {biology}/{biology_max} "
    f"({biology_percentage:.2f}%)"
)

print(
    f"\nTotal: {total_marks}/{total_maximum}"
)

print(
    f"Overall Percentage: "
    f"{overall_percentage:.2f}%"
)