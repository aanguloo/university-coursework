import pygame
from player import HumanPlayer, MinimaxPlayer
from ui import UI
from score import evaluate, strategic_eval, custom_eval


EXPERIMENTOS = 10
def main():
    
    # Cambia aqui la combinacion de jugadores:
    #player1 = HumanPlayer("Player 1")
    #player2 = HumanPlayer("Player 2")

    # player1 = HumanPlayer("Player 1")
    # player2 = MinimaxPlayer("AI", depth=2, eval_fun=evaluate, use_alphabeta=True)

    # player1 = MinimaxPlayer("AI 1", depth=3, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=strategic_eval, use_alphabeta=True)

    # headless = False si se muestra la UI siempre
    # headless = True oculta la UI solo si ambos jugadores son AI
    
    
    """Actividad 2"""
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=evaluate, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=2, eval_fun=evaluate, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=2, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=evaluate, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=3, eval_fun=evaluate, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=3, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=evaluate, use_alphabeta=True)

    """Actividad 3"""
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=strategic_eval, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=strategic_eval, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=evaluate, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=1, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=3, eval_fun=strategic_eval, use_alphabeta=True)
    
    # player1 = MinimaxPlayer("AI 1", depth=3, eval_fun=evaluate, use_alphabeta=True)
    # player2 = MinimaxPlayer("AI 2", depth=1, eval_fun=strategic_eval, use_alphabeta=True)
    
    
    """Actividad 4"""
    
    player1 = MinimaxPlayer("AI 1", depth=3, eval_fun=custom_eval, use_alphabeta=True)
    player2 = MinimaxPlayer("AI 2", depth=3, eval_fun=strategic_eval, use_alphabeta=True)
    for i in range(EXPERIMENTOS):
        ui = UI(player1, player2, headless=True)
        ui.run()


if __name__ == "__main__": 
    main()


