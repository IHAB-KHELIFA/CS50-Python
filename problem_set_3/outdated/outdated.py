def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Check if date is in month/day/year format
            if "/" in date:
                month, day, year = date.split("/")
                # Convert to integers to validate
                month = int(month)
                day = int(day)
                year = int(year)
                # Validate month and day ranges
                if month < 1 or month > 12 or day < 1 or day > 31:
                    continue

            # Check if date is in Month Day, Year format
            else:
                try:
                    month_str, rest = date.split(" ", 1)
                    day, year = rest.split(", ")
                    # Remove any trailing spaces
                    day = day.strip()
                    year = year.strip()

                    # Validate month name
                    if month_str not in months:
                        continue
                    month = months.index(month_str) + 1

                    # Convert day and year to integers
                    day = int(day)
                    year = int(year)

                    # Validate day range
                    if day < 1 or day > 31:
                        continue
                except ValueError:
                    continue

            # Format the date in ISO 8601 format
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except ValueError:
            continue

if __name__ == "__main__":
    main()
