#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Produces IPHAS Data Release 2 using an MPI computing cluster."""
from IPython import parallel
from astropy import log

__author__ = 'Geert Barentsen'

# Create the cluster view
client = parallel.Client('/home/gb/.config/ipython/profile_mpi/security/ipcontroller-pipeline-client.json')
#client = parallel.Client(profile='mpi')

#cluster = client.load_balanced_view()
cluster = client[:]
log.info('Using {0} cores'.format(len(cluster)))

# Sync imports across all nodes
with client[:].sync_imports():
    # Make sure the IPHAS DR2 module is in the path
    import os
    import sys
    sys.path.append('/home/gb/dev/iphas-dr2')
    client[:].execute("sys.path.append('/home/gb/dev/iphas-dr2')", block=True)
    # Import DR2 generation modules
    from dr2 import constants
    from dr2 import detections
    from dr2 import offsets
    from dr2 import calibration
    from dr2 import bandmerging

client[:].execute('reload(constants)', block=True)
client[:].execute('reload(detections)', block=True)
client[:].execute('reload(offsets)', block=True)
client[:].execute('reload(calibration)', block=True)
client[:].execute('reload(bandmerging)', block=True)

#detections.create_index(cluster)
#detections.sanitise_zeropoints()         # Produces zeropoint-overrides.csv
detections.convert_catalogues(cluster)
bandmerging.bandmerge(cluster)
#offsets.compute_offsets(cluster)
calibration.calibrate()
calibration.apply_calibration(cluster)
