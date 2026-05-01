from datetime import datetime

def generate_report(data):
    """Generate a full text-based attendance report and save to file."""
    filename = f"attendance_report_{datetime.today().strftime('%Y%m%d_%H%M%S')}.txt"

    lines = []
    lines.append("=" * 60)
    lines.append("       STUDENT ATTENDANCE REPORT")
    lines.append(f"       Generated on: {datetime.today().strftime('%d-%m-%Y %H:%M:%S')}")
    lines.append("=" * 60)

    if not data["students"]:
        lines.append("No student data found.")
    else:
        lines.append(f"\nTotal Students : {len(data['students'])}")
        lines.append(f"Total Subjects : {len(data['subjects'])}")
        lines.append(f"Total Records  : {len(data['records'])}")
        lines.append(f"Subjects       : {', '.join(data['subjects'])}")
        lines.append("\n" + "-" * 60)
        lines.append(f"  {'Roll':<10} {'Name':<20} {'Present':>8} {'Total':>7} {'%':>7}  Status")
        lines.append("-" * 60)

        low_students = []

        for roll, info in data["students"].items():
            records = [r for r in data["records"] if r["roll"] == roll]
            total   = len(records)
            present = sum(1 for r in records if r["status"] == "P")
            pct     = (present / total * 100) if total > 0 else 0
            status  = "OK" if pct >= 75 else "LOW ATTENDANCE"

            lines.append(f"  {roll:<10} {info['name']:<20} {present:>8} {total:>7} {pct:>6.1f}%  {status}")

            if pct < 75:
                low_students.append((roll, info["name"], pct))

        lines.append("-" * 60)

        if low_students:
            lines.append("\n⚠️  LOW ATTENDANCE ALERTS:")
            lines.append("-" * 60)
            for roll, name, pct in low_students:
                lines.append(f"  ALERT: {name} ({roll}) — {pct:.1f}% — Below 75%!")
                lines.append(f"  ACTION REQUIRED: Please attend more classes.")
        else:
            lines.append("\n✅ All students have satisfactory attendance.")

    lines.append("\n" + "=" * 60)
    lines.append("           END OF REPORT")
    lines.append("=" * 60)

    report_text = "\n".join(lines)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(report_text)
    print(f"\n📄 Report saved to: {filename}")
