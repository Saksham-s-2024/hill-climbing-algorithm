import random

def deceptive_objective_function(bitstring):
    score = sum(bitstring)
    
    if bitstring[:5] == [1, 1, 1, 1, 1] and bitstring[5:] == [0, 0, 0, 0, 0]:
        return 15  
    return score

def get_neighbors(bitstring):
    neighbors = []
    for i in range(len(bitstring)):
        neighbor = bitstring.copy()
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)
    return neighbors

def hill_climbing(length=10):
    current_state = [random.choice([0, 1]) for _ in range(length)]
    current_score = deceptive_objective_function(current_state)
    
    print(f"  Initial State: {current_state} | Score: {current_score}")
    
    steps = 0
    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_score = current_score
        
        for neighbor in neighbors:
            score = deceptive_objective_function(neighbor)
            if score > best_score:
                best_score = score
                best_neighbor = neighbor
                
        if best_score <= current_score:
            break
            
        current_state = best_neighbor
        current_score = best_score
        steps += 1
        
    return current_state, current_score

if __name__ == "__main__":
    random.seed(7)
    
    print("--- Running Simple Hill Climbing on Deceptive Landscape ---")
    final_state, final_score = hill_climbing(length=10)
    
    print(f"\nFinal Result: State = {final_state} | Score = {final_score}")