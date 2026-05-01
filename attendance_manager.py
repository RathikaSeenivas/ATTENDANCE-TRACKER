from datetime import datetime

class AttendanceManager:
    def __init__(self, data):
        self.data = data
        if "students" not in self.data:   self.data["students"] = {}
        if "subjects" not in self.data:   self.data["subjects"] = []
        if "records"  not in self.data:   self.data["records"]  = []

    # ────────────────────────────────────────────
    # ADD STUDENT
    # ────────────────────────────────────────────
    def add_student(self):
        print("\n➕ ADD STUDENT")
        roll = input("Roll Number: ").strip().upper()
        if roll in self.data["students"]:
            print("❌ Student already exists.")
            return
        name = input("Name: ").strip()
        dept = input("Department: ").strip()
        year = input("Year (1-4): ").strip()
        self.data["students"][roll] = {"name": name, "department": dept, "year": year}
        print(f"✅ Student {name} ({roll}) added successfully!")

    # ────────────────────────────────────────────
    # ADD SUBJECT
    # ────────────────────────────────────────────
    def add_subject(self):
        print("\n📚 ADD SUBJECT")
        subject = input("Subject Name: ").strip().title()
        if subject in self.data["subjects"]:
            print("❌ Subject already exists.")
            return
        self.data["subjects"].append(subject)
        print(f"✅ Subject '{subject}' added!")

    # ────────────────────────────────────────────
    # MARK ATTENDANCE
    # ────────────────────────────────────────────
    def mark_attendance(self):
        if not self.data["subjects"]:
            print("❌ No subjects found. Please add subjects first.")
            return
        if not self.data["students"]:
            print("❌ No students found. Please add students first.")
            return

        print("\n✅ MARK ATTENDANCE")
        print("Subjects:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(self.data["subjects"])))
        try:
            sub_idx = int(input("Choose subject number: ").strip()) - 1
            subject = self.data["subjects"][sub_idx]
        except (ValueError, IndexError):
            print("❌ Invalid subject choice.")
            return

        date_input = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
        if not date_input:
            date_input = datetime.today().strftime("%Y-%m-%d")

        # Check duplicate
        already_marked = [
            r for r in self.data["records"]
            if r["subject"] == subject and r["date"] == date_input
        ]
        if already_marked:
            print(f"⚠️  Attendance for '{subject}' on {date_input} already marked.")
            redo = input("Re-mark? (yes/no): ").strip().lower()
            if redo == "yes":
                self.data["records"] = [
                    r for r in self.data["records"]
                    if not (r["subject"] == subject and r["date"] == date_input)
                ]
            else:
                return

        print(f"\nMarking attendance for: {subject} | Date: {date_input}")
        print("Enter P = Present, A = Absent, L = Leave\n")

        for roll, info in self.data["students"].items():
            while True:
                status = input(f"  {roll} - {info['name']}: ").strip().upper()
                if status in ("P", "A", "L"):
                    self.data["records"].append({
                        "roll": roll,
                        "subject": subject,
                        "date": date_input,
                        "status": status
                    })
                    break
                else:
                    print("    ❌ Enter P, A, or L only.")

        print(f"\n✅ Attendance marked for {len(self.data['students'])} students!")

    # ────────────────────────────────────────────
    # VIEW BY STUDENT
    # ────────────────────────────────────────────
    def view_by_student(self):
        print("\n🔍 VIEW ATTENDANCE BY STUDENT")
        roll = input("Enter Roll Number: ").strip().upper()
        if roll not in self.data["students"]:
            print("❌ Student not found.")
            return

        student = self.data["students"][roll]
        records = [r for r in self.data["records"] if r["roll"] == roll]

        if not records:
            print("No attendance records found.")
            return

        print(f"\n  Student : {student['name']} ({roll})")
        print(f"  Dept    : {student['department']} | Year: {student['year']}")
        print(f"\n  {'Date':<14} {'Subject':<25} {'Status'}")
        print("  " + "-" * 50)

        for r in sorted(records, key=lambda x: x["date"]):
            symbol = "✅" if r["status"] == "P" else ("🟡" if r["status"] == "L" else "❌")
            print(f"  {r['date']:<14} {r['subject']:<25} {symbol} {r['status']}")

        # Per-subject percentage
        print(f"\n  📊 Subject-wise Attendance %")
        print("  " + "-" * 40)
        for subject in self.data["subjects"]:
            sub_records = [r for r in records if r["subject"] == subject]
            if not sub_records:
                continue
            present = sum(1 for r in sub_records if r["status"] == "P")
            pct = (present / len(sub_records)) * 100
            bar = self._bar(pct)
            alert = " ⚠️ LOW" if pct < 75 else ""
            print(f"  {subject:<22} {pct:5.1f}%  {bar}{alert}")

    # ────────────────────────────────────────────
    # VIEW BY SUBJECT
    # ────────────────────────────────────────────
    def view_by_subject(self):
        print("\n📚 VIEW ATTENDANCE BY SUBJECT")
        if not self.data["subjects"]:
            print("No subjects found.")
            return

        print("Subjects:", ", ".join(f"{i+1}.{s}" for i, s in enumerate(self.data["subjects"])))
        try:
            sub_idx = int(input("Choose subject: ").strip()) - 1
            subject = self.data["subjects"][sub_idx]
        except (ValueError, IndexError):
            print("❌ Invalid choice.")
            return

        records = [r for r in self.data["records"] if r["subject"] == subject]
        if not records:
            print("No records found.")
            return

        dates = sorted(set(r["date"] for r in records))
        print(f"\n  Subject: {subject}")
        print(f"  {'Roll':<10} {'Name':<20}", end="")
        for d in dates:
            print(f"  {d[5:]}", end="")  # show MM-DD
        print(f"  {'Present':>8}  {'%':>6}")
        print("  " + "-" * (35 + len(dates) * 9))

        for roll, info in self.data["students"].items():
            print(f"  {roll:<10} {info['name']:<20}", end="")
            present = 0
            for d in dates:
                rec = next((r for r in records if r["roll"] == roll and r["date"] == d), None)
                if rec:
                    symbol = "P" if rec["status"] == "P" else ("L" if rec["status"] == "L" else "A")
                    if rec["status"] == "P": present += 1
                else:
                    symbol = "-"
                print(f"  {symbol:^7}", end="")
            pct = (present / len(dates)) * 100 if dates else 0
            print(f"  {present:>6}/{len(dates)}  {pct:>5.1f}%")

    # ────────────────────────────────────────────
    # OVERALL SUMMARY
    # ────────────────────────────────────────────
    def attendance_summary(self):
        print("\n📊 ATTENDANCE SUMMARY — ALL STUDENTS")
        if not self.data["students"]:
            print("No students found.")
            return

        print(f"\n  {'Roll':<10} {'Name':<20} {'Present':>8} {'Total':>7} {'%':>7}  Status")
        print("  " + "-" * 65)

        for roll, info in self.data["students"].items():
            records = [r for r in self.data["records"] if r["roll"] == roll]
            total   = len(records)
            present = sum(1 for r in records if r["status"] == "P")
            pct     = (present / total * 100) if total > 0 else 0
            status  = "✅ OK" if pct >= 75 else "⚠️ LOW"
            print(f"  {roll:<10} {info['name']:<20} {present:>8} {total:>7} {pct:>6.1f}%  {status}")

    # ────────────────────────────────────────────
    # LOW ATTENDANCE ALERT
    # ────────────────────────────────────────────
    def low_attendance_alert(self):
        print("\n🚨 LOW ATTENDANCE ALERT (Below 75%)")
        print("=" * 55)

        found = False
        for roll, info in self.data["students"].items():
            records = [r for r in self.data["records"] if r["roll"] == roll]
            if not records:
                continue
            present = sum(1 for r in records if r["status"] == "P")
            pct     = (present / len(records)) * 100

            if pct < 75:
                found = True
                classes_needed = self._classes_to_attend(present, len(records))
                print(f"\n  ⚠️  {info['name']} ({roll})")
                print(f"     Department : {info['department']}")
                print(f"     Attendance : {present}/{len(records)} = {pct:.1f}%")
                print(f"     📧 ALERT   : Your attendance is below 75%!")
                print(f"     📌 ACTION  : Attend {classes_needed} more class(es) continuously to reach 75%.")

        if not found:
            print("\n  ✅ All students have attendance above 75%. Great!")

    # ────────────────────────────────────────────
    # VIEW ALL STUDENTS
    # ────────────────────────────────────────────
    def view_all_students(self):
        if not self.data["students"]:
            print("No students found.")
            return
        print(f"\n  {'Roll':<10} {'Name':<20} {'Department':<20} {'Year'}")
        print("  " + "-" * 55)
        for roll, info in self.data["students"].items():
            print(f"  {roll:<10} {info['name']:<20} {info['department']:<20} {info['year']}")

    # ────────────────────────────────────────────
    # DELETE STUDENT
    # ────────────────────────────────────────────
    def delete_student(self):
        roll = input("Enter Roll Number to delete: ").strip().upper()
        if roll not in self.data["students"]:
            print("❌ Student not found.")
            return
        name = self.data["students"][roll]["name"]
        del self.data["students"][roll]
        self.data["records"] = [r for r in self.data["records"] if r["roll"] != roll]
        print(f"✅ Student {name} ({roll}) and all records deleted.")

    # ────────────────────────────────────────────
    # HELPERS
    # ────────────────────────────────────────────
    def _bar(self, pct):
        filled = int(pct / 5)
        return "█" * filled + "░" * (20 - filled)

    def _classes_to_attend(self, present, total):
        needed = 0
        p, t = present, total
        while (p / t * 100) < 75 and needed < 100:
            p += 1
            t += 1
            needed += 1
        return needed
