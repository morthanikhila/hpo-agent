import random
from hpo_engine.sampler import sample_config

def random_search(objective_fn, search_space, num_trials, seed=42):
    random.seed(seed)

    results = []
    best_score = float("-inf")
    best_config = None

    for trial in range(num_trials):
        config = sample_config(search_space)
        score = objective_fn(config, seed=trial)

        results.append({
            "trial": trial,
            "config": config,
            "score": score
        })

        if score > best_score:
            best_score = score
            best_config = config

        print(f"Trial {trial}: score={score:.3f}")

    return best_config, best_score, results
