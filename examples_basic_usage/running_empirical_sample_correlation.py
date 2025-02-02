from precise.synthetic.generate import create_correlated_dataset
from precise.covariance.empirical import emp_pcov
from pprint import pprint
from precise.covariance.matrixfunctions import cov_to_corrcoef
from precise.covariance.statemutations import both_cov

# Basic example of running empirical sample correlation

if __name__=='__main__':
    xs = create_correlated_dataset(n=500)
    s = {}
    for x in xs:
        s = emp_pcov(s=s, x=x)
    s = both_cov(s)  # <--- Converts scov to pcov
    scorr = cov_to_corrcoef(s['scov'])
    pprint(scorr)    # Sample correlation
