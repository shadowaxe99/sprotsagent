import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('players.db')
cursor = conn.cursor()

# Create a table to store player profiles
cursor.execute('''CREATE TABLE IF NOT EXISTS players
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   sport TEXT,
                   team TEXT,
                   performance TEXT)''')

def add_player(name, sport, team, performance):
    # Insert a new player into the database
    cursor.execute("INSERT INTO players (name, sport, team, performance) VALUES (?, ?, ?, ?)",
                   (name, sport, team, performance))
    conn.commit()

def update_player(player_id, name=None, sport=None, team=None, performance=None):
    # Update player information in the database
    update_query = "UPDATE players SET"
    update_values = []

    if name:
        update_query += " name = ?,"
        update_values.append(name)
    if sport:
        update_query += " sport = ?,"
        update_values.append(sport)
    if team:
        update_query += " team = ?,"
        update_values.append(team)
    if performance:
        update_query += " performance = ?,"
        update_values.append(performance)

    # Remove the trailing comma
    update_query = update_query.rstrip(',')

    # Add the WHERE clause to update the specific player
    update_query += " WHERE id = ?"
    update_values.append(player_id)

    cursor.execute(update_query, tuple(update_values))
    conn.commit()

def delete_player(player_id):
    # Delete a player from the database
    cursor.execute("DELETE FROM players WHERE id = ?", (player_id,))
    conn.commit()

def retrieve_players(criteria=None):
    # Retrieve player information from the database based on criteria
    if criteria:
        query = "SELECT * FROM players WHERE " + criteria
    else:
        query = "SELECT * FROM players"

    cursor.execute(query)
    return cursor.fetchall()

# Example usage
task = AddPlayerTask("John Doe", "Basketball", "Team A", "Excellent performance")
task.start()
task = AddPlayerTask("Jane Smith", "Soccer", "Team B", "Average performance")
task.start()

update_player(1, name="John Doe Jr.", performance="Outstanding performance")

delete_player(2)

players = retrieve_players("sport = 'Basketball'")
for player in players:
    print(player)

# Close the database connection
conn.close()