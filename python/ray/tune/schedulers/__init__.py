from ray.tune.schedulers.trial_scheduler import TrialScheduler, FIFOScheduler
from ray.tune.schedulers.hyperband import HyperBandScheduler
from ray.tune.schedulers.hb_bohb import HyperBandForBOHB
from ray.tune.schedulers.async_hyperband import (AsyncHyperBandScheduler,
                                                 ASHAScheduler)
from ray.tune.schedulers.median_stopping_rule import MedianStoppingRule
from ray.tune.schedulers.pbt import (PopulationBasedTraining,
                                     PopulationBasedTrainingReplay)
from ray.tune.schedulers.pb2 import PB2

def create_scheduler(
        scheduler,
        **kwargs,
):
    """Instantiate a scheduler based on the given string.

    This is useful for swapping between different schedulers.

    Args:
        scheduler (str): The scheduler to use.
        **kwargs: Scheduler parameters.
            These keyword arguments will be passed to the initialization
            function of the chosen scheduler.
    Returns:
        ray.tune.schedulers.trial_scheduler.TrialScheduler: The scheduler.
    Example:
        >>> scheduler = tune.create_scheduler('pbt', **pbt_kwargs)
    """

    SCHEDULER_IMPORT = {
        "fifo": FIFOScheduler,
        "async_hyperband": AsyncHyperBandScheduler,
        "asynchyperband": AsyncHyperBandScheduler,
        "median_stopping_rule": MedianStoppingRule,
        "medianstopping": MedianStoppingRule,
        "hyperband": HyperBandScheduler,
        "hb_bohb": HyperBandForBOHB,
        "pbt": PopulationBasedTraining,
        "pbt_replay": PopulationBasedTrainingReplay,
        "pb2": PB2,
    }
    scheduler = scheduler.lower()
    if scheduler not in SCHEDULER_IMPORT:
        raise ValueError(
            f"Search alg must be one of {list(SCHEDULER_IMPORT)}. "
            f"Got: {scheduler}")

    SchedulerClass = SCHEDULER_IMPORT[scheduler]
    return SchedulerClass(**kwargs)


__all__ = [
    "TrialScheduler", "HyperBandScheduler", "AsyncHyperBandScheduler",
    "ASHAScheduler", "MedianStoppingRule", "FIFOScheduler",
    "PopulationBasedTraining", "PopulationBasedTrainingReplay",
    "HyperBandForBOHB", "PB2"
]
