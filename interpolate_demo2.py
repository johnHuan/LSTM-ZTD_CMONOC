# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 21:26
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : interpolate_demo2.py
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt


def func(x, y, z):
    return x ** 2 + y ** 2 + z ** 2

# Nx, Ny, Nz = 181, 181, 421
Nx, Ny, Nz = 18, 18, 42

subsample = 2
Mx, My, Mz = Nx // subsample, Ny // subsample, Nz // subsample

# Define irregularly spaced arrays
x = np.random.random(Nx)
y = np.random.random(Ny)
z = np.random.random(Nz)

# Compute the matrix D of shape (Nx, Ny, Nz).
# D could be experimental data, but here I'll define it using func
# D[i,j,k] is associated with location (x[i], y[j], z[k])
X_irregular, Y_irregular, Z_irregular = (
    x[:, None, None], y[None, :, None], z[None, None, :])
D = func(X_irregular, Y_irregular, Z_irregular)

# Create a uniformly spaced grid
xi = np.linspace(x.min(), x.max(), Mx)
yi = np.linspace(y.min(), y.max(), My)
zi = np.linspace(y.min(), y.max(), Mz)
X_uniform, Y_uniform, Z_uniform = (
    xi[:, None, None], yi[None, :, None], zi[None, None, :])

# To use griddata, I need 1D-arrays for x, y, z of length
# len(D.ravel()) = Nx*Ny*Nz.
# To do this, I broadcast up my *_irregular arrays to each be
# of shape (Nx, Ny, Nz)
# and then use ravel() to make them 1D-arrays
X_irregular, Y_irregular, Z_irregular = np.broadcast_arrays(
    X_irregular, Y_irregular, Z_irregular)
D_interpolated = interpolate.griddata(
    (X_irregular.ravel(), Y_irregular.ravel(), Z_irregular.ravel()),
    D.ravel(),
    (X_uniform, Y_uniform, Z_uniform),
    method='linear')

print(D_interpolated.shape)
# (90, 90, 210)

# Make plots
fig, ax = plt.subplots(2)

# Choose a z value in the uniform z-grid
# Let's take the middle value
zindex = Mz // 2
z_crosssection = zi[zindex]

# Plot a cross-section of the raw irregularly spaced data
X_irr, Y_irr = np.meshgrid(sorted(x), sorted(y))
# find the value in the irregular z-grid closest to z_crosssection
z_near_cross = z[(np.abs(z - z_crosssection)).argmin()]
ax[0].contourf(X_irr, Y_irr, func(X_irr, Y_irr, z_near_cross))
ax[0].scatter(X_irr, Y_irr, c='white', s=20)
ax[0].set_title('Cross-section of irregular data')
ax[0].set_xlim(x.min(), x.max())
ax[0].set_ylim(y.min(), y.max())

# Plot a cross-section of the Interpolated uniformly spaced data
X_unif, Y_unif = np.meshgrid(xi, yi)
ax[1].contourf(X_unif, Y_unif, D_interpolated[:, :, zindex])
ax[1].scatter(X_unif, Y_unif, c='white', s=20)
ax[1].set_title('Cross-section of downsampled and interpolated data')
ax[1].set_xlim(x.min(), x.max())
ax[1].set_ylim(y.min(), y.max())

plt.show()