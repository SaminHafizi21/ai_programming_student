import numpy as np
import matplotlib.pyplot as plt

def epsilon_greedy(num_arms, epsilon, num_iterations):
    """
    Voer het epsilon-greedy algoritme uit.

    Args:
        num_arms (int): Het aantal bandits.
        epsilon (float): De kans om te exploreren (tussen 0 en 1).
        num_iterations (int): Het aantal iteraties om uit te voeren.

    Returns:
        tuple: Gemiddelde beloningen per iteratie, ware beloningen, geselecteerde arm.
    """
    true_rewards = np.random.normal(0, 1, num_arms)  # True rewards voor elke bandit
    estimated_rewards = np.zeros(num_arms)  # geschatte rewards per bandit
    arm_counts = np.zeros(num_arms)  # aantal keren dat een bandit werd gebruikt
    total_reward = 0
    average_rewards = []

    for iteration in range(0, num_iterations):
        # Kiezen tussen exploreren en exploiteren
        if np.random.rand() < epsilon:
            # Explore: kies een willekeurige arm
            selected_arm = np.random.randint(num_arms)
        else:
            # Exploit: kies de arm met de hoogste geschatte reward
            selected_arm = np.argmax(estimated_rewards)

        # Simulatie van het spelen op een bandit en update van rewards
        # De reward is een random trekking, met de true_rewards parameter als gemiddelde
        reward = np.random.normal(true_rewards[selected_arm], 1)

        # Update van tellingen en totale reward
        arm_counts[selected_arm] += 1
        total_reward += reward

        # Update geschatte beloningen (incremental average)
        n = arm_counts[selected_arm]
        estimated_rewards[selected_arm] = estimated_rewards[selected_arm] + (1/n) * (reward - estimated_rewards[selected_arm])

        # Berekening van gemiddelde winst
        average_rewards.append(total_reward / (iteration + 1))

    return average_rewards, true_rewards, np.argmax(estimated_rewards)

def plot_results(average_rewards, true_rewards, selected_arm):
    """
    Plot de resultaten van het epsilon-greedy algoritme.
    
    Args:
        average_rewards (list): Gemiddelde rewards over tijd.
        true_rewards (np.array): True rewards van elke arm.
        selected_arm (int): De uiteindelijk geselecteerde bandit.
    """
    plt.plot(average_rewards, label='Gemiddelde Reward')
    plt.plot(true_rewards[selected_arm] * np.ones_like(average_rewards), linestyle='--', label='True Reward (Gekozen Bandit)')
    plt.xlabel('Iteratie')
    plt.ylabel('Reward')
    plt.title('Epsilon-Greedy Algorithm voor Multi-Armed Bandit')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Parameters
    num_arms = 5
    epsilon = 0.1
    num_iterations = 1000

    # Run epsilon-greedy algorithm
    average_rewards, true_rewards, selected_arm = epsilon_greedy(num_arms, epsilon, num_iterations)

    # Plot results
    plot_results(average_rewards, true_rewards, selected_arm)
