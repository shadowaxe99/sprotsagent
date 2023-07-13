from execution_engine import ExecutionEngine
from player_database import add_player

class AddPlayerTask(ExecutionEngine):
    def __init__(self, name, sport, team, performance):
        self.name = name
        self.sport = sport
        self.team = team
        self.performance = performance

    async def start(self):
        add_player(self.name, self.sport, self.team, self.performance)

# Example usage
# task = AddPlayerTask("John Doe", "Basketball", "Team A", "Excellent performance")
# task.start()