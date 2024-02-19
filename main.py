class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        if count < 0:
            raise ValueError("Enter number of students : ")
        self.total_strength += count

        print("Students Enrolled successfully!")

    def dropStudents(self, count):
        if count < 0:
            raise ValueError("Number of students to drop must be non-negative.")
        if count > self.total_strength:
            raise ValueError("Cannot drop more students than enrolled.")
        self.total_strength -= count
        print("Students Dropped successfully!")
        
    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

# Example usage:
if __name__ == "__main__":
    mlops = StudentsInMLOps()
    mlops.enrollStudents(50)
    print("Total strength after enrollment:", mlops.getTotalStrength())
    mlops.dropStudents(6)
    print("Total strength after dropping students:", mlops.getTotalStrength())
