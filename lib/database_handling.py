import psycopg2


def db_init(
    set_timezone,
):
    # Connect to the SQLite database
    global conn, cursori
    conn = psycopg2.connect(
        user="postgres",
        password="devserver",
        host="127.0.0.1",
        port="5432",
        database="coffee-roaster",
    )
    cursor = conn.cursor()

    # Set the timezone
    cursor.execute(f"SET TIME ZONE '{set_timezone}';")

    # Create the database tables if they don't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS roast_profiles (
            id SERIAL PRIMARY KEY,
            name TEXT,
            description TEXT,
            roast_level TEXT,
            created_at TIMESTAMP with time zone DEFAULT CURRENT_TIMESTAMP,
            modified_at TIMESTAMP with time zone DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS roasts (
            id SERIAL PRIMARY KEY,
            roast_profile_id INTEGER,
            start_time TIMESTAMP with time zone DEFAULT CURRENT_TIMESTAMP,
            end_time TIMESTAMP with time zone DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (roast_profile_id) REFERENCES roast_profiles(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS target_roast_profile_values (
            id SERIAL PRIMARY KEY,
            roast_profile_id INTEGER,
            target_time INTEGER,
            target_temperature REAL,
            FOREIGN KEY (roast_profile_id) REFERENCES roast_profiles(id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS roaster_temp_readings (
            id SERIAL PRIMARY KEY,
            roast_id INTEGER,
            timestamp INTEGER,
            temperature REAL,
            FOREIGN KEY (roast_id) REFERENCES roasts(id)
        )
    """
    )

    conn.commit()

    return conn, cursor


def fetch_profile_data(
    cursor,
    roast_profile_id,
):

    cursor.execute(
        f"SELECT target_time, target_temperature, target_RPM, target_power, target_fan FROM target_roast_profile_values WHERE roast_profile_id = {roast_profile_id} ORDER BY target_time;"
    )

    return cursor.fetchall()
