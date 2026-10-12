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
    
    steps = 0
    print(f"Initial State: {current_state} | Score: {current_score}\n")
    
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
            print(f"Optimization finished. Reached peak at step {steps}.")
            break
            
        current_state = best_neighbor
        current_score = best_score
        steps += 1
        print(f"Step {steps}: {current_state} | Score: {current_score}")
        
    return current_state, current_score

if __name__ == "__main__":
    random.seed(42)
    
    print("--- Starting Hill Climbing Optimization ---")
    final_state, final_score = hill_climbing(length=10)
    
    print("\n--- Final Results ---")
    print(f"Optimal State Found: {final_state}")
    print(f"Final Score (Number of 1s): {final_score}")