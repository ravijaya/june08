def tuner(**kwargs):
    """syntax for the keyword arguments"""
    print(kwargs)


tuner()
tuner(brightness=.79, hue=.79)
tuner(brightness=.8, contrast=.78, hue=.69)  # keyword arguments
