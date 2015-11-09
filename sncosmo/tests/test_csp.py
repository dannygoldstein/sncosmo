
import sncosmo
from numpy.testing import assert_allclose
import numpy as np
from astropy.utils.data import get_pkg_data_filename
import numpy as np

def test_csp_magsys_calibration_inaccurate():
    
    csp = sncosmo.get_magsystem('csp')
    csp_info_path = get_pkg_data_filename('data/csp_filter_info.dat')

    # read it into a numpy array
    csp_filter_data = np.genfromtxt(csp_info_path, names=True, dtype=None,
                                    skip_header=3)

    answers = csp_filter_data['natural_mag']
    bands   = csp_filter_data['name']
    
    for band, answer in zip(bands, answers):
        mag = csp.standard_mag(band, accurate=False)
        print band, mag, answer
        assert_allclose(mag, answer, atol=0.015)

def test_csp_magsys_calibration_accurate():
    
    csp = sncosmo.get_magsystem('csp')
    csp_info_path = get_pkg_data_filename('data/csp_filter_info.dat')

    # read it into a numpy array
    csp_filter_data = np.genfromtxt(csp_info_path, names=True, dtype=None,
                                    skip_header=3)

    answers = csp_filter_data['natural_mag']
    bands   = csp_filter_data['name']
    
    for band, answer in zip(bands, answers):
        mag = csp.standard_mag(band, accurate=True)
        print band, mag, answer 
        assert_allclose(mag, answer, atol=0.015)
