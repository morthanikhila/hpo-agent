import random
import math

def objective_function(config, seed=None):
    if seed is not None:
        random.seed(seed)

    lr = config["learning_rate"]
    batch_size = config["batch_size"]
    num_layers = config["num_layers"]

    score = (
        -math.log10(lr)
        + (batch_size / 64)
        + (num_layers * 0.5)
    )

    noise = random.uniform(-0.5, 0.5)
    return score + noise
