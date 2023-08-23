import os
import shutil
import sqlite3
from datetime import datetime

def fetch_chrome_history():
    # Get the current user's username
    username = os.getlogin()

    # Path to the original Chrome history database
    original_db = fr"C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\History"

    # Destination path for the copied database file
    destination_dir = fr"C:\Users\{username}\AppData\Local\Temp"
    copied_db = os.path.join(destination_dir, "HistoryCopy")

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copy the original database file to the destination
    shutil.copy2(original_db, copied_db)

    # Connect to the copied database
    connection = sqlite3.connect(copied_db)
    cursor = connection.cursor()

    # Query to fetch the browsing history
    query = "SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10;"

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print the browsing history
    for title, url, timestamp in results:
        # Format the timestamp
        formatted_timestamp = datetime.fromtimestamp(timestamp // 1000000).strftime("%d-%m-%Y %H:%M")

        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Timestamp: {formatted_timestamp}")
        print("")

    # Close the database connection
    cursor.close()
    connection.close()

    # Delete the copied database file
    os.remove(copied_db)

# Call the function to fetch the Chrome history
fetch_chrome_history()
