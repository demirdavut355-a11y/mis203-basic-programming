total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")
    if name == "q":
        break

    score_input = input("Enter score: ")
    score = float(score_input)

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Not tam sayıysa ondalıksız gösterim (örn: 85 -> B)
    displayed_score = int(score) if score.is_integer() else score
    print(f"{name}: {displayed_score} -> {grade}")

    total_score += score
    student_count += 1

if student_count == 0:
    print("No students entered.")
else:
    average = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average:.2f}")
