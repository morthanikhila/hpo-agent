import sys
from pathlib import Path

# Add project root to PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from hpo_engine.objective import objective_function
from hpo_engine.search_space import SEARCH_SPACE
from hpo_engine.engine import random_search

if __name__ == "__main__":
    best_config, best_score, results = random_search(
        objective_fn=objective_function,
        search_space=SEARCH_SPACE,
        num_trials=20
    )

    print("\nBest configuration found:")
    print(best_config)
    print("Best score:", best_score)
