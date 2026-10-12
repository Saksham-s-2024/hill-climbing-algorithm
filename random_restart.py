import random

def objective_function(bitstring):

    return sum(bitstring)

def get_neighbors(bitstring):

    neighbors = []
    for i in range(len(bitstring)):
        neighbor = bitstring.copy()
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)
    return neighbors

def hill_climbing(length=10):
    
    current_state = [random.choice([0, 1]) for _ in range(length)]
    current_score = objective_function(current_state)
    
    print(f"  Initial State: {current_state} | Score: {current_score}")
    
    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_score = current_score
        
        for neighbor in neighbors:
            score = objective_function(neighbor)
            if score > best_score:
                best_score = score
                best_neighbor = neighbor
                
        if best_score <= current_score:
            break
            
        current_state = best_neighbor
        current_score = best_score
        
    return current_state, current_score

def random_restart_hill_climbing(length=10, max_restarts=3):
    
    best_overall_state = None
    best_overall_score = -1
    
    for restart in range(max_restarts):
        print(f"\n--- Restart Attempt {restart + 1} ---")
        final_state, final_score = hill_climbing(length)
        print(f"  Peak Reached: {final_state} | Score: {final_score}")
        
        if final_score > best_overall_score:
            best_overall_score = final_score
            best_overall_state = final_state
            
        if best_overall_score == length:
            print("  Global optimum (10/10) reached!")
            break
            
    return best_overall_state, best_overall_score

if __name__ == "__main__":
    random.seed(42)
    
    print("--- Starting Random-Restart Hill Climbing Optimization ---")
    best_state, best_score = random_restart_hill_climbing(length=10, max_restarts=3)
    
    print("\n--- Final Results ---")
    print(f"Best State Found Across All Restarts: {best_state}")
    print(f"Final Score: {best_score}")