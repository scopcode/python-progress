def make_models(finished_models,unfinished_models):
    while unfinished_models:
        current_model = unfinished_models.pop()
        print(f"{current_model} is being prepared")
        finished_models.append(current_model)
    return finished_models
