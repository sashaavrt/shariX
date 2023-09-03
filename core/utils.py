def setup(local_namespace: dict, config_class):
    """setup(local_namespace: dict, config_class)

    Adds all attributes of the configuration class
    to the passed namespace as ordinary variables.
    
    """
    local_namespace.update(vars(config_class))