import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
from LunarLanderAgent import LunarLanderAgent

# Parámetros de entrenamiento final
NUM_EPISODES = 70_000
PRINT_EVERY = 100

#Parametros para experimento 1 y 2.
#NUM_EPISODES = 30_000
#PRINT_EVERY = 100
def train(save_npy_path, save_csv_path, save_png_path):
    # Entrena un agente Q-Learning para LunarLander y guarda los resultados
    env = make_env()
    agent = LunarLanderAgent(env)

    mean_scores = []
    block_rewards = []
    best_block_mean = -np.inf

    for episode in range(1, NUM_EPISODES + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            block_best = float(np.max(recent_rewards))
            pct_negative = float(np.mean(recent_rewards < 0.0) * 100.0)
            pct_solutions = float(np.mean(recent_rewards > 200.0) * 100.0)

            mean_scores.append(block_mean)
            best_block_mean = max(best_block_mean, block_mean)
            print(
                f"Episode {episode:6d} | mean score: {block_mean:8.2f} | "
                f"best score: {block_best:8.2f} | % reward < 0: {pct_negative:6.2f}% | "
                f"% solutions: {pct_solutions:6.2f}% | epsilon: {agent.exploration_rate:.4f}"
            )

    np.save(save_npy_path, agent.q_table)
    agent.export_q_table_csv(save_csv_path)
    plot_learning_curve(mean_scores, save_png_path)
    env.close()
    print(f"Gráfico de aprendizaje guardado en {save_png_path}")
    return agent

def make_env():
    # Crea el entorno de LunarLander con parámetros fijos
    env = gym.make("LunarLander-v3", continuous=False, gravity=-10.0, enable_wind=False,
                   wind_power=15.0, turbulence_power=1.5)
    return gym.wrappers.RecordEpisodeStatistics(env, buffer_length=NUM_EPISODES)

def plot_learning_curve(mean_scores, output_path):
    # Grafica la curva de aprendizaje y la guarda como imagen
    plt.figure(figsize=(10, 5))
    plt.plot(mean_scores)
    plt.xlabel(f"Bloques de {PRINT_EVERY} episodios")
    plt.ylabel("Mean score")
    plt.title("Aprendizaje de LunarLander con Q-Learning")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# TODO: Puedes definir más funciones para generar gráficos y tablas de resultados (Actividad 3)
#par este experimento se utilizó 30.000 episodios, y un discount factor de 0 y de 0.95.
def experimento_1():
    
    mean_scores_agente_miope = []
    mean_scores_agente_previsor = []
    
    # Entrena un agente con discount factor 0.0 (miope)
    env = make_env()
    agent = LunarLanderAgent(env)
    block_rewards = []
    agent.discount_factor = 0.0
    
    for episode in range(1, 30000 + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            mean_scores_agente_miope.append(block_mean)
    env.close()
    
    # Entrena un agente con discount factor 0.95 (no miope)
    env = make_env()
    agent = LunarLanderAgent(env)
    block_rewards = []
    agent.discount_factor = 0.95
    
    for episode in range(1, 30000 + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            mean_scores_agente_previsor.append(block_mean)
    env.close()
    
    # Graficaremos haciendo un procedimiento similar al de la función plot_learning_curve, pero con ambas curvas en el mismo gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(mean_scores_agente_miope, label="Agente miope (discount factor = 0.0)")
    plt.plot(mean_scores_agente_previsor, label="Agente previsor (discount factor = 0.95)")
    plt.xlabel(f"Bloques de {PRINT_EVERY} episodios")
    plt.ylabel("Mean score")
    plt.title("Comparación de agentes con diferentes discount factors")
    plt.legend()
    plt.tight_layout()
    plt.savefig("comparacion_agentes.png")
    plt.close()

#se utilizara un discount factor de 0.95, y se entrenara los agente durante 30.000 episodios. Ademas se utilizo IA para poder crear la tabla de resultados.
def experimento_2():
    
    mean_scores_agente_lr_bajo = []
    mean_scores_agente_lr_alto = []
    mejores_scores_agente_lr_bajo = []
    mejores_scores_agente_lr_alto = []
    # Entrena con learning rate 0.01
    env = make_env()
    agent = LunarLanderAgent(env)
    block_rewards = []
    agent.learning_rate = 0.01
    
    for episode in range(1, 30000 + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            mean_scores_agente_lr_bajo.append(block_mean)
            block_best = float(np.max(recent_rewards))
            mejores_scores_agente_lr_bajo.append(block_best)
    env.close()
    
    # Entrena un agente con learning rate 0.7
    env = make_env()
    agent = LunarLanderAgent(env)
    block_rewards = []
    agent.learning_rate = 0.7
    
    for episode in range(1, 30000 + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            mean_scores_agente_lr_alto.append(block_mean)
            block_best = float(np.max(recent_rewards))
            mejores_scores_agente_lr_alto.append(block_best)
    env.close()
    
    #tabla de resultados 
    
    filas = []
    for i in range(0, 300, 20):
        filas.append([
            f"{np.mean(mean_scores_agente_lr_bajo[i:i+20]):.2f}",
            f"{np.mean(mean_scores_agente_lr_alto[i:i+20]):.2f}",
            f"{np.max(mejores_scores_agente_lr_alto[i:i+20]):.2f}",
            f"{np.max(mejores_scores_agente_lr_bajo[i:i+20]):.2f}"
        ])
    
    for fila in filas:
        print(" | ".join(fila))
        
    _, ax = plt.subplots(figsize=(14, 7))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=filas, colLabels=["Mean score LR BAJO", "Mean score LR ALTO", "Mejor score LR ALTO", "Mejor score LR BAJO"], loc='center')
    plt.savefig("tabla_resultados.png")
    plt.close()

#Para ambos experimentos se utilizaron 50.000 episodios. En el experimento 3a se utilizo un decay rate de 0.05, mientras que en el experimento 3b se igualo el max y el min epsilon en 0.8.
def experimento_3a():
    # Entrena un agente Q-Learning para LunarLander y guarda los resultados
    env = make_env()
    agent = LunarLanderAgent(env)
    agent.epsilon_decay_rate = 0.05
    mean_scores = []
    block_rewards = []
    best_block_mean = -np.inf

    for episode in range(1, NUM_EPISODES + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            block_best = float(np.max(recent_rewards))
            pct_negative = float(np.mean(recent_rewards < 0.0) * 100.0)
            pct_solutions = float(np.mean(recent_rewards > 200.0) * 100.0)

            mean_scores.append(block_mean)
            best_block_mean = max(best_block_mean, block_mean)
            print(
                f"Episode {episode:6d} | mean score: {block_mean:8.2f} | "
                f"best score: {block_best:8.2f} | % reward < 0: {pct_negative:6.2f}% | "
                f"% solutions: {pct_solutions:6.2f}% | epsilon: {agent.exploration_rate:.4f}"
            )
    plt.figure(figsize=(10, 5))
    plt.plot(mean_scores)
    plt.xlabel(f"Bloques de {PRINT_EVERY} episodios")
    plt.ylabel("Mean score")
    plt.title("Aprendizaje de LunarLander con Q-Learning")
    plt.tight_layout()
    plt.savefig("curva_aprendizaje_experimento_3a.png")
    plt.close()
    env.close()

def experimento_3b():
    # Entrena un agente Q-Learning para LunarLander y guarda los resultados
    env = make_env()
    agent = LunarLanderAgent(env)
    agent.min_epsilon = 0.8
    agent.max_epsilon = 0.8
    mean_scores = []
    block_rewards = []
    best_block_mean = -np.inf

    for episode in range(1, NUM_EPISODES + 1):
        observation, _ = env.reset()
        state = agent.get_state(observation)
        terminated = False
        truncated = False
        episode_reward = 0.0

        while not (terminated or truncated):
            action = agent.get_action(state, training=True)
            next_observation, reward, terminated, truncated, _ = env.step(action)
            next_state = agent.get_state(next_observation)

            done = terminated or truncated
            agent.update_q_value(state, action, reward, next_state, done)

            state = next_state
            episode_reward += reward

        agent.n_games += 1
        agent.decay_exploration_rate()
        block_rewards.append(episode_reward)

        if episode % PRINT_EVERY == 0:
            recent_rewards = np.array(block_rewards[-PRINT_EVERY:], dtype=np.float32)
            block_mean = float(np.mean(recent_rewards))
            block_best = float(np.max(recent_rewards))
            pct_negative = float(np.mean(recent_rewards < 0.0) * 100.0)
            pct_solutions = float(np.mean(recent_rewards > 200.0) * 100.0)

            mean_scores.append(block_mean)
            best_block_mean = max(best_block_mean, block_mean)
            print(
                f"Episode {episode:6d} | mean score: {block_mean:8.2f} | "
                f"best score: {block_best:8.2f} | % reward < 0: {pct_negative:6.2f}% | "
                f"% solutions: {pct_solutions:6.2f}% | epsilon: {agent.exploration_rate:.4f}"
            )
    plt.figure(figsize=(10, 5))
    plt.plot(mean_scores)
    plt.xlabel(f"Bloques de {PRINT_EVERY} episodios")
    plt.ylabel("Mean score")
    plt.title("Aprendizaje de LunarLander con Q-Learning")
    plt.tight_layout()
    plt.savefig("curva_aprendizaje_experimento_3b.png")
    plt.close()
    env.close()

#Experimento 4 se realizara directamente en el main.py con los hiperparametros modificados.


#descomentaar para correr el experimento correspondiente, se recomienda correr cada experimento por separado para evitar tiempos de entrenamiento excesivos
if __name__ == "__main__":
    #experimento_1()
    #experimento_2()
    #experimento_3a()
    #experimento_3b()
    pass
