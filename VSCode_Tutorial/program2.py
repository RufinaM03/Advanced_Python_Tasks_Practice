import matplotlib.pyplot as plt
subjects = ["Python", "C", "Java", "C++"]
scores = [88, 92, 79, 85]
plt.bar(subjects, scores, color='blue')
plt.title("Student Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()