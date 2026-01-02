import random

def sample_config(search_space):
    config = {}

    lr_min, lr_max = search_space["learning_rate"]
    config["learning_rate"] = random.uniform(lr_min, lr_max)

    config["batch_size"] = random.choice(search_space["batch_size"])

    layers_min, layers_max = search_space["num_layers"]
    config["num_layers"] = random.randint(layers_min, layers_max)

    return config
