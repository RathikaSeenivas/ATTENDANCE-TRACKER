from attendance_manager import AttendanceManager
from report import generate_report
import json
import os

DATA_FILE = "attendance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"students": {}, "subjects": [], "records": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def main():
    data = load_data()
    manager = AttendanceManager(data)

    print("=" * 50)
    print("     📊 Student Attendance Tracker System")
    print("=" * 50)

    while True:
        print("\n📋 MAIN MENU")
        print("1.  Add Student")
        print("2.  Add Subject")
        print("3.  Mark Attendance")
        print("4.  View Attendance (by Student)")
        print("5.  View Attendance (by Subject)")
        print("6.  Attendance % Summary (All Students)")
        print("7.  Low Attendance Alert (below 75%)")
        print("8.  Generate Full Report")
        print("9.  View All Students")
        print("10. Delete Student")
        print("11. Exit")
        print("-" * 40)

        choice = input("Enter your choice: ").strip()

        if   choice == "1":  manager.add_student()
        elif choice == "2":  manager.add_subject()
        elif choice == "3":  manager.mark_attendance()
        elif choice == "4":  manager.view_by_student()
        elif choice == "5":  manager.view_by_subject()
        elif choice == "6":  manager.attendance_summary()
        elif choice == "7":  manager.low_attendance_alert()
        elif choice == "8":  generate_report(data)
        elif choice == "9":  manager.view_all_students()
        elif choice == "10": manager.delete_student()
        elif choice == "11":
            save_data(manager.data)
            print("\n💾 Data saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

        save_data(manager.data)

if __name__ == "__main__":
    main()
