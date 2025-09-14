unfinished_models = ["mobile cover", "figurine", "pyramid"]
finished_models = []
def make_models(finished_models,unfinished_models):
    while unfinished_models:
        current_model = unfinished_models.pop()
        print(f"{current_model} is being prepared")
        finished_models.append(current_model)
    return finished_models

def model_prepared(models_done):
    print(f"Models prepare today are :")
    for model in models_done:
        print(f"-{model}")

make_models(finished_models,unfinished_models)
model_prepared(finished_models)

