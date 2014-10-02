import numpy as np

def ps2nm(t,
          lambda0,
          chirp = 0,
          out = 'nm'):
    """t is the duration of pulse(FWHM) in ps, lambda0 is the center-wavelength of input pulse in nm"""
    
    c = 299792458                   # in m/s
    
    bandwidth = 0.32 * np.sqrt(1 + chirp**2) / t * 1e12 # in Hz

    if out == 'nm':
        return bandwidth * lambda0**2 / c * 1e-9 # in nm

    if out == 'cm-1':
        return bandwidth / c * 1e-2 # in cm^-1

def nm2tbp(bandwidth_nm,
           lambda0,
           t):
    
    c = 299792458                   # in m/s
    bandwidth_Hz = bandwidth_nm * c / lambda0**2 * 1e-3        #in THz
    
    return t * bandwidth_Hz
    