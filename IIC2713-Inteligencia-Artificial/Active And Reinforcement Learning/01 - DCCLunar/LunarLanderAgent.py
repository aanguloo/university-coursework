import numpy as np
from random import uniform
# Hiperparámetros Q-Learning

#hiperparametros ocupados para entrenar el modelo final
LR = 0.0275
DISCOUNT_RATE = 0.99
MAX_EXPLORATION_RATE = 1.0
MIN_EXPLORATION_RATE = 0.01
EXPLORATION_DECAY_RATE = 0.00012

# Valores originales de los hiperparámetros utilizados para los experimentos realizados
#LR = 0.03
#DISCOUNT_RATE = 0.95
#MAX_EXPLORATION_RATE = 1.0
#MIN_EXPLORATION_RATE = 0.02
#EXPLORATION_DECAY_RATE = 0.00015

class LunarLanderAgent:
    # Clase de agente Q-Learning para LunarLander

    def __init__(self, env):
        self.env = env

        # Inicializamos los hiperparámetros
        self.learning_rate = LR
        self.discount_factor = DISCOUNT_RATE
        self.max_epsilon = MAX_EXPLORATION_RATE
        self.min_epsilon = MIN_EXPLORATION_RATE
        self.epsilon_decay_rate = EXPLORATION_DECAY_RATE

        # Inicializamos los juegos realizados por el agente en 0
        self.n_games = 0

        # Inicializamos el exploration rate
        self.exploration_rate = self.max_epsilon
        self.training_error = []

        # Definimos cortes internos para discretizar el espacio de estados
        self.x_bins = np.array([-0.40, -0.15, 0.15, 0.40], dtype=np.float32)
        self.y_bins = np.array([0.05, 0.20, 0.45, 0.80], dtype=np.float32)
        self.vx_bins = np.array([-0.50, -0.15, 0.15, 0.50], dtype=np.float32)
        self.vy_bins = np.array([-0.90, -0.35, -0.10, 0.10], dtype=np.float32)
        self.angle_bins = np.array([-0.30, -0.10, 0.10, 0.30], dtype=np.float32)
        self.angular_bins = np.array([-1.00, -0.20, 0.20, 1.00], dtype=np.float32)

        # Diccionario con el estado del agente como key y su indice en la q_table como value
        self.states_index = {}
        index = 0
        
        #Se hacen varios ciclos anidados para generar todas las combinaciones posibles de estados y asignarles un indice unico en la q_table
        for pos_x in range(5):
            for pos_y in range(5):
                for vel_x in range(5):
                    for vel_y in range(5):
                        for angulo in range(5):
                            for vel_angular in range(5):
                                for estado_patas in range(4):
                                    estado = (pos_x, pos_y, vel_x, vel_y, angulo, vel_angular, estado_patas)
                                    self.states_index[estado] = index
                                    index += 1  
        
        # Inicializamos la q_table que pose 625000 filas.
        self.q_table = np.zeros((index, self.env.action_space.n), dtype=np.float32)

    def digitize(self, value, bins):
        # Mapea un float a un índice discreto válido
        return int(np.digitize(value, bins))

    def get_state(self, observation):
        # Retorna un estado discreto
        x, y, vx, vy, angle, angular_velocity, left_leg, right_leg = observation

        x_bin = self.digitize(float(np.clip(x, -1.0, 1.0)), self.x_bins)
        y_bin = self.digitize(float(np.clip(y, -0.2, 1.2)), self.y_bins)
        vx_bin = self.digitize(float(np.clip(vx, -1.5, 1.5)), self.vx_bins)
        vy_bin = self.digitize(float(np.clip(vy, -2.0, 0.5)), self.vy_bins)
        angle_bin = self.digitize(float(np.clip(angle, -1.0, 1.0)), self.angle_bins)
        angular_bin = self.digitize(float(np.clip(angular_velocity, -3.0, 3.0)), self.angular_bins)
        leg_state = int(bool(left_leg)) * 2 + int(bool(right_leg))

        return (x_bin, y_bin, vx_bin, vy_bin, angle_bin, angular_bin, leg_state)

    #Codigo utilizado sacado de https://www.datacamp.com/es/tutorial/introduction-q-learning-beginner-tutorial
    def get_action(self, state, training = True):
        # Recibe un estado del agente y usa epsilon-greedy para seleccionar una acción
        numero_aleatorio = uniform(0, 1)
        if training and numero_aleatorio > self.exploration_rate:
            action = np.argmax(self.q_table[self.states_index[state]])
            return int(action)
        return int(self.env.action_space.sample())
    # Información obtenida de https://medium.com/@goldengrisha/a-beginners-guide-to-q-learning-understanding-with-a-simple-gridworld-example-2b6736e7e2c9
    def update_q_value(self, state, action, reward, next_state, done):
        # Actualiza la Q-table usando la fórmula de Q-Learning

        # a) Busca los índices de los estados en la tabla de estados
        
        state_index = self.states_index[state]
        next_state_index = self.states_index[next_state]

        # b) Calcula best_next_q
        if done:
            best_next_q = 0
        else:
            best_next_q = np.max(self.q_table[next_state_index])

        # c) Calcula td_target (La formula t = r + gamma * max(Q(s', a'))
        td_target = reward + self.discount_factor * best_next_q

        # d) Calcula td_error
        td_error = td_target - self.q_table[state_index,action]

        # e) Actualiza self.q_table[state_index, action]
        self.q_table[state_index, action] += self.learning_rate * td_error

        # f) Guarda el error de entrenamiento para seguimiento
        self.training_error.append(td_error)

    def decay_exploration_rate(self):
        # Actualiza el exploration rate una vez por episodio
        self.exploration_rate = (self.min_epsilon + 
                            (self.max_epsilon - self.min_epsilon) 
                            * np.exp(-self.epsilon_decay_rate * self.n_games))


    def export_q_table_csv(self, filepath):
        # Exporta la Q-table obtenida a un archivo CSV
        rows = []
        for state, idx in self.states_index.items():
            rows.append(list(state) + self.q_table[idx].tolist())
        np.savetxt(filepath, np.asarray(rows, dtype=np.float32), delimiter=",", fmt="%.6f")