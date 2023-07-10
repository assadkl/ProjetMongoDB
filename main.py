import os
from scripts.models.ProblemSolver import ProblemSolver
from scripts.models.GraphDesigner import GraphDesigner
from scripts.models.UI import UI

from dotenv import load_dotenv
load_dotenv()

def main():
    # Your code goes here
    ma_fenetre = UI()
    # user_input = input('Quelle problématique voulez-vous résoudre ? ')
    # graph_designer = GraphDesigner()
    # solver = ProblemSolver()
    # while(user_input != 'Non'):
    #     results = solver.solveIssue(user_input)
    #     graph_designer.designGraph(user_input, results)
    #     user_input = input('Quelle problématique voulez-vous résoudre ? ')
    
if __name__ == "__main__":
    main()