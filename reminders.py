import subprocess


cmd = [
    "osascript",
    "-e",
    'tell application "Reminders" to get name of (reminders of list "미리 알림" whose completed is false)'

]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0: # 0이 아니면 실패했다는 뜻
    print(f"에러 발생!: {result.stderr}")
else:
    reminders = result.stdout.strip().split(", ")
    for r in reminders:
        print(r)