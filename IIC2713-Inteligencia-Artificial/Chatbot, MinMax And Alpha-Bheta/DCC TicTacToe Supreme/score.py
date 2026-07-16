from board import EMPTY, X, O, LINES


def _player_mark(player_idx):
    return X if player_idx == 0 else O


def _count_two_in_a_row(grid, mark):
    count = 0
    for line in LINES:
        vals = [grid[r][c] for r, c in line]
        if vals.count(mark) == 2 and vals.count(EMPTY) == 1:
            count += 1
    return count


def _count_one_in_a_row(grid, mark):
    count = 0
    for line in LINES:
        vals = [grid[r][c] for r, c in line]
        if vals.count(mark) == 1 and vals.count(EMPTY) == 2:
            count += 1
    return count


def evaluate(game, player_idx):
    if game.winner is not None:
        return 1e9 if game.winner == player_idx else -1e9

    opp_idx = 1 - player_idx
    my_mark = _player_mark(player_idx)
    opp_mark = _player_mark(opp_idx)

    my_boards = 0
    opp_boards = 0
    my_cells = 0
    opp_cells = 0

    for br in range(3):
        for bc in range(3):
            mini = game.board.get_mini(br, bc)
            if mini.winner == my_mark:
                my_boards += 1
            elif mini.winner == opp_mark:
                opp_boards += 1
            for cr in range(3):
                for cc in range(3):
                    if mini.cells[cr][cc] == my_mark:
                        my_cells += 1
                    elif mini.cells[cr][cc] == opp_mark:
                        opp_cells += 1

    tempo = 0.01 if (game.turn % 2) == player_idx else -0.01
    score = 3.0 * (my_boards - opp_boards) + 0.1 * (my_cells - opp_cells) + tempo
    return score


def strategic_eval(game, player_idx):
    if game.winner is not None:
        return 1e9 if game.winner == player_idx else -1e9

    opp_idx = 1 - player_idx
    my_mark = _player_mark(player_idx)
    opp_mark = _player_mark(opp_idx)

    my_boards = 0
    opp_boards = 0
    my_mini_threats = 0
    opp_mini_threats = 0
    my_mini_ones = 0
    opp_mini_ones = 0

    for br in range(3):
        for bc in range(3):
            mini = game.board.get_mini(br, bc)
            if mini.winner == my_mark:
                my_boards += 1
            elif mini.winner == opp_mark:
                opp_boards += 1
            elif not mini.is_done():
                my_mini_threats += _count_two_in_a_row(mini.cells, my_mark)
                opp_mini_threats += _count_two_in_a_row(mini.cells, opp_mark)
                my_mini_ones += _count_one_in_a_row(mini.cells, my_mark)
                opp_mini_ones += _count_one_in_a_row(mini.cells, opp_mark)

    board_score = 5.0 * (my_boards - opp_boards)
    mini_threat_score = 0.6 * (my_mini_threats - opp_mini_threats)
    mini_ones_score = 0.15 * (my_mini_ones - opp_mini_ones)

    meta = game.board.meta
    my_meta_threats = _count_two_in_a_row(meta, my_mark)
    opp_meta_threats = _count_two_in_a_row(meta, opp_mark)
    meta_threat_score = 3.0 * (my_meta_threats - opp_meta_threats)

    my_meta_ones = _count_one_in_a_row(meta, my_mark)
    opp_meta_ones = _count_one_in_a_row(meta, opp_mark)
    meta_ones_score = 0.4 * (my_meta_ones - opp_meta_ones)

    tempo = 0.05 if (game.turn % 2) == player_idx else -0.05

    return (board_score + mini_threat_score + mini_ones_score +
            meta_threat_score + meta_ones_score + tempo)


# Aca defines tus funciones de evaluacion

def contar_vacias(mini):
    celdas_vacias = 0
    for cr in range(3):
        for cc in range(3):
            if mini.cells[cr][cc] == EMPTY:
                celdas_vacias += 1
    return celdas_vacias

# Idea: Penalizar movimientos. Costos por tablero.
def custom_eval(game, player_idx):
    if game.winner is not None:
            return 1e9 if game.winner == player_idx else -1e9

    opp_idx = 1 - player_idx
    my_mark = _player_mark(player_idx)
    opp_mark = _player_mark(opp_idx)

    my_boards = 0
    opp_boards = 0
    my_mini_threats = 0
    opp_mini_threats = 0
    my_mini_ones = 0
    opp_mini_ones = 0
    
    posible_robos: int = 0
    dos_en_raya: int = 0  
    # Pesos de casillas en el tablero meta. (Fila, Columna): Peso
    pesos: dict[tuple[int, int], float] = {
        (1, 1): 3.0,
        (0, 0): 2.0,
        (0, 2): 2.0,
        (2, 0): 2.0,
        (2, 2): 2.0,
        (0, 1): 1.0,
        (2, 1): 1.0,
        (1, 0): 1.0,
        (1, 2): 1.0,
    }
    

    for br in range(3):
        for bc in range(3):
            mini = game.board.get_mini(br, bc)
            if mini.winner == my_mark:
                my_boards += pesos[(br, bc)]
            elif mini.winner == opp_mark:
                opp_boards += pesos[(br, bc)]
            elif not mini.is_done():
                my_mini_threats += _count_two_in_a_row(mini.cells, my_mark)
                opp_mini_threats += _count_two_in_a_row(mini.cells, opp_mark)
                my_mini_ones += _count_one_in_a_row(mini.cells, my_mark)
                opp_mini_ones += _count_one_in_a_row(mini.cells, opp_mark)
                
                # Vemos cuantas celdas estan ocupadas
                celdas_ocupadas: int = 9 - contar_vacias(mini)
                # Si son muy cercanas a 9, entonces sumar amenazada de robo.
                if celdas_ocupadas >= 7:
                    posible_robos += 1

    board_score = 5.0 * (my_boards - opp_boards)
    mini_threat_score = 0.6 * (my_mini_threats - opp_mini_threats)
    mini_ones_score = 0.15 * (my_mini_ones - opp_mini_ones)
    robo: float = -0.5 * posible_robos  # Penalizamos por riesgo de robo
    
    meta = game.board.meta
    my_meta_threats = _count_two_in_a_row(meta, my_mark)
    opp_meta_threats = _count_two_in_a_row(meta, opp_mark)
    meta_threat_score = 3.0 * (my_meta_threats - opp_meta_threats)
    
    # Si hay dos en raya en el tablero meta, se suma o resta un bonus/penalización.
    if my_meta_threats >= 2:
        dos_en_raya += 1
    if opp_meta_threats >= 2:
        dos_en_raya -= 1
    
    # Bonificación o penalización por tener dos en raya en el tablero meta.
    amenaza_dos_en_raya: float = 5.0 * dos_en_raya 
    
    my_meta_ones = _count_one_in_a_row(meta, my_mark)
    opp_meta_ones = _count_one_in_a_row(meta, opp_mark)
    meta_ones_score = 0.4 * (my_meta_ones - opp_meta_ones)

    tempo = 0.05 if (game.turn % 2) == player_idx else -0.05

    return (board_score + mini_threat_score + mini_ones_score +
            meta_threat_score + meta_ones_score + tempo + robo + 
            amenaza_dos_en_raya)
