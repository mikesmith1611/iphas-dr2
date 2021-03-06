#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Constants used in the IPHAS Data Release modules."""
import os
from astropy.io import fits

DEBUGMODE = False

# What is the data release version name?
VERSION = 'iphas-dr2-rc6'
# Where are the CASU pipeline-produced images and detection tables?
RAWDATADIR = '/car-data/gb/iphas'
# Where to write the output data products?
DESTINATION = '/car-data/gb/'+VERSION
# Where can we write a large amount of temporary files?
TMPDIR = '/home/gb/tmp'

# Use a different configuration for development machines:
HOSTNAME = os.uname()[1]
if HOSTNAME == 'uhppc11.herts.ac.uk':
    DEBUGMODE = True
    RAWDATADIR = '/run/media/gb/0133d764-0bfe-4007-a9cc-a7b1f61c4d1d/iphas'
    DESTINATION = '/home/gb/tmp/'+VERSION
if HOSTNAME == 'gvm':
    DEBUGMODE = True
    RAWDATADIR = '/media/uh/run/media/gb/0133d764-0bfe-4007-a9cc-a7b1f61c4d1d/iphas'
    DESTINATION = '/home/gb/tmp/'+VERSION

# Where to store processing logs?
LOGDIR = os.path.join(DESTINATION, 'log')
# Make sure destination and logging dir exist
if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)


PACKAGEDIR = os.path.dirname(os.path.abspath(__file__))
LIBDIR = os.path.join(PACKAGEDIR, 'lib')

CALIBDIR = os.path.join(DESTINATION, 'calibration')
PATH_BANDMERGED = os.path.join(DESTINATION, 'bandmerged')
PATH_BANDMERGED_CALIBRATED = os.path.join(DESTINATION, 'bandmerged-calibrated')
PATH_SEAMED = os.path.join(DESTINATION, 'seamed')
PATH_CONCATENATED = os.path.join(DESTINATION, 'concatenated')
PATH_IMAGES = os.path.join(DESTINATION, 'images')


# Where is the IPHAS quality control table?
IPHASQC = fits.getdata('/home/gb/dev/iphas-qc/qcdata/iphas-qc.fits', 1)
IPHASQC_COND_RELEASE = (IPHASQC['is_best'] & (IPHASQC['qflag'] != 'D'))

# How to execute stilts?
STILTS = 'nice java -Xmx2000M -XX:+UseConcMarkSweepGC -jar {0}'.format(
                                os.path.join(LIBDIR, 'stilts.jar'))

# How to execute funpack?
FUNPACK = '/home/gb/bin/cfitsio3310/bin/funpack'

# Fields within this radius will be considered to overlap
FIELD_MAXDIST = 0.8  # degrees

# Width of the Galactic Plane strip to process
STRIPWIDTH = 5  # degrees galactic longitude

# Detections within this radius will be considered identical
MATCHING_DISTANCE = 1.0 # 0.5  # arcsec

 #INT/WFC CCD pixel scale
PXSCALE = 0.333  # arcsec/pix

# Filter names
BANDS = ['r', 'i', 'ha']

# Which extensions to expect in the fits catalogues?
EXTENSIONS = [1, 2, 3, 4]

# Which are the possible filenames of the confidence maps?
CONF_NAMES = {'Halpha': ['Ha_conf.fits', 'Ha_conf.fit',
                         'Halpha_conf.fit',
                         'ha_conf.fits', 'ha_conf.fit',
                         'h_conf.fits', 'h_conf.fit',
                         'Halpha:197_iphas_aug2003_cpm.fit',
                         'Halpha:197_iphas_sep2003_cpm.fit',
                         'Halpha:197_iphas_oct2003_cpm.fit',
                         'Halpha:197_iphas_nov2003_cpm.fit',
                         'Halpha:197_nov2003b_cpm.fit',
                         'Halpha:197_dec2003_cpm.fit',
                         'Halpha:197_jun2004_cpm.fit',
                         'Halpha:197_iphas_jul2004a_cpm.fit',
                         'Halpha:197_iphas_jul2004_cpm.fit',
                         'Halpha:197_iphas_aug2004a_cpm.fit',
                         'Halpha:197_iphas_aug2004b_cpm.fit',
                         'Halpha:197_iphas_dec2004b_cpm.fit'],
              'r': ['r_conf.fit', 'r_conf.fits',
                    'r:214_iphas_aug2003_cpm.fit',
                    'r:214_dec2003_cpm.fit',
                    'r:214_iphas_nov2003_cpm.fit',
                    'r:214_nov2003b_cpm.fit',
                    'r:214_iphas_sep2003_cpm.fit',
                    'r:214_iphas_aug2004a_cpm.fit',
                    'r:214_iphas_aug2004b_cpm.fit',
                    'r:214_iphas_jul2004a_cpm.fit',
                    'r:214_iphas_jul2004_cpm.fit',
                    'r:214_jun2004_cpm.fit'],
              'i': ['i_conf.fit', 'i_conf.fits',
                    'i:215_iphas_aug2003_cpm.fit',
                    'i:215_dec2003_cpm.fit',
                    'i:215_iphas_nov2003_cpm.fit',
                    'i:215_nov2003b_cpm.fit',
                    'i:215_iphas_sep2003_cpm.fit',
                    'i:215_iphas_aug2004a_cpm.fit',
                    'i:215_iphas_aug2004b_cpm.fit',
                    'i:215_iphas_jul2004a_cpm.fit',
                    'i:215_iphas_jul2004_cpm.fit',
                    'i:215_jun2004_cpm.fit']}
