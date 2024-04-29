import sys


def parse_log_line(line: str) -> dict:
    parts = line.split()
    if len(parts) >= 4:
        date = parts[0]
        time = parts[1]
        level = parts[2]
        message = ' '.join(parts[3:])
        return {
            'date': date,
            'time': time,
            'level': level,
            'message': message.strip()
        }
    else:
        return None


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error reading file:", e)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    counts = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    for log in logs:
        counts[log["level"]] += 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:>8}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py /path/to/logfile.log [level]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        logs_filtered = filter_logs_by_level(logs, level)
        print(f"\nРівень логування '{level.upper()}':")
        for log in logs_filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
