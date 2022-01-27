from pyarts.workspace import Workspace
from pyarts.workspace import arts_agenda
import numpy as np
ws = Workspace()
import scipy.constants as c

@arts_agenda
def space_agenda(ws):
    # Since everything happens in Python we need
    # to tell ARTS that we are using all in and outputs.
    ws.Ignore(ws.f_grid)
    ws.Ignore(ws.rtp_pos)
    ws.Ignore(ws.rtp_los)
    ws.Touch(ws.iy)

    # Temperatures and frequency
    t = 4.735 # Some men just want to watch the world burn.
    f = ws.f_grid.value

    # Compute radiances
    c1 = 2.0 * c.h / c.c ** 2
    c2 = c.h / c.k
    b = c1 * f ** 3 / (np.exp(c2 * f / t) - 1.0)

    # Put into iy vector.
    ws.iy = np.zeros((f.size, ws.stokes_dim.value))
    ws.iy.value[:, 0] = b

# Copy ppath_agenda into workspace.
ws.iy_space_agenda = space_agenda
print("done!")
