import importlib, pkgutil


def register_modules(app):
    pkg = __name__
    for _, name, is_pkg in pkgutil.iter_modules(__path__):
        if is_pkg:
            mod = importlib.import_module(f"{pkg}.{name}.routes")
            if hasattr(mod, "init_routes"):
                mod.init_routes(app)
