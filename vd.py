import heapq

def min_turns_to_beat_boss(t, test_cases):
    results = []
    
    for case in test_cases:
        h, n = case['h'], case['n']
        a = case['a']
        c = case['c']
        
        pq = []  # Priority queue for cooldowns
        for i in range(n):
            heapq.heappush(pq, (0, a[i], c[i]))  # (next_available_turn, damage, cooldown)
        
        turns = 0
        current_health = h
        
        while current_health > 0:
            turns += 1
            total_damage = 0
            temp = []
            
            # Collect all attacks that can be used this turn
            while pq and pq[0][0] <= turns:
                next_available_turn, damage, cooldown = heapq.heappop(pq)
                total_damage += damage
                temp.append((turns + cooldown, damage, cooldown))
            
            # Push them back with updated cooldown
            for item in temp:
                heapq.heappush(pq, item)
            
            # Apply the total damage of this turn
            current_health -= total_damage
        
        results.append(turns)
    
    return results

# Example usage:
t = 1
test_cases = [
    {
        'h': 10,
        'n': 3,
        'a': [3, 2, 1],
        'c': [3, 2, 1]
    }
]

print(min_turns_to_beat_boss(t, test_cases))  # Example output
