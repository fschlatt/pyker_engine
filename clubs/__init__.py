__version__ = "0.1.3"
__author__ = "Ferdinand Schlatt"
__license__ = "GPL-3.0"
__copyright__ = f"Copyright (c) 2021, {__author__}."
__homepage__ = "https://github.com/fschlatt/clubs"
__docs__ = (
    "clubs is a general purpose python poker engine for running arbitrary poker "
    "configurations with a built-in fast hand evaluator."
)

try:
    # This variable is injected in the __builtins__ by the build
    # process. It is used to enable importing subpackages when
    # the binaries are not built
    __CLUBS_SETUP__  # type: ignore
except NameError:
    __CLUBS_SETUP__ = False

if __CLUBS_SETUP__:  # type: ignore
    pass  # pragma: no cover
else:
    from . import configs, poker, render
    from .poker import Card, Dealer, Deck, Evaluator, LookupTable

__all__ = [
    "configs",
    "poker",
    "render",
    "Card",
    "Dealer",
    "Deck",
    "Evaluator",
    "LookupTable",
]
