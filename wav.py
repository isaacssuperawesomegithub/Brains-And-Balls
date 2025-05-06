from enemy import Enemy


class Wave:
    def __init__(self, enemy: Enemy, count: int, interval: int, map):
        self.enemy = enemy
        
        self.count = count
        self.added = 0
        
        self.map = map
        
        self.interval = interval
        self.timer = 0


    def update(self):
        """
        Goes to next wave if finished, creates enemies at specified interval.

        :return: Returns nothing.
        """
        
        if self.added >= self.count:
            self.map.current_wave += 1
            return
        
        self.timer += 1
        if self.timer >= self.interval:
            self.timer = 0
            self.map.add_enemy(self.enemy())
            self.added += 1