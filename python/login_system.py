import json
import os

ADMIN_PASSWORD = "admin123"
STUDENTS_FILE = "../data/students.json"

def load_students():
    """Load students from the existing JSON file, returning a dictionary by ID."""
    if not os.path.exists(STUDENTS_FILE):
        return {}
    
    try:
        with open(STUDENTS_FILE, 'r') as f:
            students_list = json.load(f)
            # Reconstruct dict map
            return {s['id']: s for s in students_list}
    except Exception as e:
        print(f"  [WARN] Could not load saved data: {e}")
        return {}

def save_student(student, students):
    """Save the updated student catalog back to JSON."""
    students[student['id']] = student
    os.makedirs(os.path.dirname(STUDENTS_FILE), exist_ok=True)
    with open(STUDENTS_FILE, 'w') as f:
        json.dump(list(students.values()), f, indent=2)

def create_student_profile(students):
    """Flow for creating a new profile inside the login sequence."""
    print("\n  --- Create New Student Profile ---")
    id_val = input("  Student ID: ").strip()
    if not id_val:
        print("  [!] Student ID cannot be empty.")
        return None
    if id_val in students:
        print("  [!] Student ID already exists.")
        return None
        
    name = input("  Full Name : ").strip()
    if not name:
        print("  [!] Name cannot be empty.")
        return None
        
    major = input("  Major     : ").strip()
    if not major:
        major = "Undeclared"
        
    new_student = {
        "id": id_val,
        "name": name,
        "major": major,
        "enrolledCourses": [],
        "completedCourses": []
    }
    
    save_student(new_student, students)
    print(f"  [✓] New student profile created: Student{{id='{id_val}', name='{name}', major='{major}'}}")
    return new_student

def student_login(students):
    """Student login logic mapped from Java studentLogin()."""
    print("\n  --- Student Login ---")
    id_val = input("  Enter your Student ID (or 'new' to create a new profile):\n  > ").strip()
    
    if id_val.lower() == 'new':
        student = create_student_profile(students)
        if student:
            print(f"  Welcome, {student['name']}! (Proceeding to Student Menu...)")
        return

    student = students.get(id_val)
    if not student:
        print("  [!] Student ID not found. Type 'new' to create a new profile.")
        return
        
    print(f"  Welcome, {student['name']}! (Proceeding to Student Menu...)")

def admin_login():
    """Admin login logic mapped from Java adminLogin()."""
    print("\n  --- Admin Login ---")
    pwd = input("  Password: ").strip()
    
    if pwd != ADMIN_PASSWORD:
        print("  [!] Incorrect password.")
        return
        
    print("  Welcome, Administrator! (Proceeding to Admin Menu...)")

def login_menu():
    """Main continuous loop replicating Java loginMenu() -> Main context."""
    students = load_students()
    
    while True:
        print("\n" + "="*70)
        print("  LOGIN")
        print("="*70)
        print("  [1] Login as Student")
        print("  [2] Login as Admin")
        print("  [3] Exit")
        print("-" * 70)
        
        choice = input("  Select option: ").strip()
        
        if choice == '1':
            student_login(students)
        elif choice == '2':
            admin_login()
        elif choice == '3':
            print("\n  Thank you for using the Course Enrollment System. Goodbye!")
            print("="*70)
            break
        else:
            print("  [!] Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    print("="*70)
    print("       COURSE ENROLLMENT SYSTEM (Python Login Demo)")
    print("="*70)
    login_menu()
