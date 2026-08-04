import os
import time
import modules.parser as parser
import modules.database as database


def main():
    print("Welcome to Sentinel v1!")

    filepath = input("Enter the path to the authentication log: ")

    if not os.path.isfile(filepath):
        print("Error: The specified file does not exist.")
        return

    print("Processing the authentication log...")
    time.sleep(1)

    database.create_database()

    event_count = 0

    with open(filepath, "r", encoding="utf-8") as log_file:
        for line in log_file:

            if not line.strip():
                continue

            event = parser.parse_auth_log(line)

            database.insert_event(event)

            event_count += 1

    print("Processing complete.")
    print(f"Stored {event_count} events in Sentinel database.")


if __name__ == "__main__":
    main()