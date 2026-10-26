students = []
marks_matrix = []

student_count = int(input("Number of students: "))
subject_count = int(input("Number of subjects: "))

if student_count <= 0 or subject_count <= 0:
    print("Counts must be greater than zero.")
else:
    valid = True
    for i in range(student_count):
        name = input(f"Student {i + 1} name: ")
        row = []
        for j in range(subject_count):
            mark = float(input(f"Mark for subject {j + 1}: "))
            if not 0 <= mark <= 100:
                print("Invalid mark. Restart with valid marks.")
                valid = False
                break
            row.append(mark)
        if not valid:
            break
        students.append(name)
        marks_matrix.append(row)

    if valid:
        averages = []
        for i in range(student_count):
            avg = sum(marks_matrix[i]) / subject_count
            averages.append(avg)
            print(f"{students[i]} average: {avg:.2f}")

        print("\nSubject averages:")
        for j in range(subject_count):
            total = 0
            for i in range(student_count):
                total += marks_matrix[i][j]
            print(f"Subject {j + 1}: {total / student_count:.2f}")

        top = averages.index(max(averages))
        print("Top student:", students[top])
