
# See also https://osqp.org/docs/examples/portfolio.html
import numpy as np
from precise.covariance.util import make_symmetric, dense_weights_from_dict, normalize, nearest_pos_def

# sum(w)=1
# 0 < w < 1


def long_from_cov( cov, as_dense=True ):
    """ Long only cov minimizing portfolio with weights summing to unity """
    import pypfopt
    cov = make_symmetric(cov)
    cov = nearest_pos_def(cov)
    n_dim = np.shape(cov)[0]
    from pypfopt import EfficientFrontier
    ef = EfficientFrontier(None, cov, weight_bounds=(0, 1))
    ef.min_volatility()
    weights = ef.clean_weights()
    return normalize( dense_weights_from_dict(weights,  n_dim=n_dim)) if as_dense else weights


def long_from_pre(pre, as_dense=True):
    pre = make_symmetric(pre)
    cov = np.linalg.inv(pre)
    return long_from_cov(cov=cov, as_dense=as_dense )

