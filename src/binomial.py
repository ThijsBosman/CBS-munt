import numpy as np
from scipy.stats import binom
from scipy.stats._distn_infrastructure import rv_frozen
from scipy.stats import binom_test


def get_binom_distribution(n: int = 100, p: float = 0.5) -> rv_frozen:
    """This function returns the binomial distribution of a given n and p

    Args:
        n (int): number of trials
        p (float): probability of success

    Returns:
        rv_frozen: binomial distribution
    """
    if n < 0:
        raise ValueError('The number of trials must be non-negative.')

    if p < 0 or p > 1:
        raise ValueError('The probability of success must be between 0 and 1.')

    return binom(n, p)


def get_binom_pdf(distribution: rv_frozen) -> np.ndarray:
    """This function returns the probability density function of a given binomial distribution

    Args:
        distribution (rv_frozen): binomial distribution

    Returns:
        numpy.ndarray: probability density function
    """
    if distribution is None:
        raise ValueError('The distribution must be provided.')

    return distribution.pmf(np.arange(distribution.args[0] + 1))


def get_binom_cdf(distribution: rv_frozen = None) -> np.ndarray:
    """This function returns the cumulative density function of a given binomial distribution

    Args:
        distribution (rv_frozen): binomial distribution

    Returns:
        numpy.ndarray: cumulative density function
    """
    if distribution is None:
        raise ValueError('The distribution must be provided.')

    return distribution.cdf(np.arange(distribution.args[0] + 1))


def get_rejecting_boundries(distribution: rv_frozen = None, alpha: float = 0.05) -> tuple:
    """This function returns the rejecting boundries of a given binomial distribution.
    Values lower than the first boundry and higher than the second boundry are rejected.
    Note that the boundries are not inclusive.

    Args:
        distribution (rv_frozen): binomial distribution
        alpha (float): significance level

    Returns:
        tuple: the lower and upper rejecting boundries
    """
    if distribution is None:
        raise ValueError('The distribution must be provided.')

    if alpha < 0 or alpha > 1:
        raise ValueError('The significance level must be between 0 and 1.')

    return distribution.ppf(alpha / 2), distribution.ppf(1 - alpha / 2)


def get_p_value(distribution: rv_frozen = None, n_succes=0):
    """This function returns the p-value of a given binomial distribution

    Args:
        distribution (rv_frozen): binomial distribution
        n_succes (int): number of successes

    Returns:
        float: p-value
    """
    if distribution is None:
        raise ValueError('The distribution must be provided.')

    if n_succes < 0 or n_succes > distribution.args[0]:
        raise ValueError(
            'The number of succes must be between 0 and the number of trials.')

    return binom_test(n_succes, distribution.args[0], distribution.args[1], alternative='two-sided')
