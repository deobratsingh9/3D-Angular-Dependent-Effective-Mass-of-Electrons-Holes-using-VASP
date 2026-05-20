import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# ==========================================================
# ====== HIGH-QUALITY 3D ARROW =============================
# ==========================================================
def draw_arrow(ax, start, direction, length, color):
    direction = np.array(direction)
    direction = direction / np.linalg.norm(direction)

    stem_length = 0.8 * length
    cone_length = 0.2 * length
    stem_radius = 0.02 * length
    cone_radius = 0.05 * length

    theta = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(0, stem_length, 10)
    theta, z = np.meshgrid(theta, z)

    x_cyl = stem_radius * np.cos(theta)
    y_cyl = stem_radius * np.sin(theta)
    z_cyl = z

    z2 = np.linspace(stem_length, length, 10)
    theta2, z2 = np.meshgrid(theta[0], z2)
    r2 = cone_radius * (length - z2) / cone_length

    x_cone = r2 * np.cos(theta2)
    y_cone = r2 * np.sin(theta2)
    z_cone = z2

    def rotation_matrix(vec):
        z_axis = np.array([0, 0, 1])
        v = np.cross(z_axis, vec)
        c = np.dot(z_axis, vec)
        s = np.linalg.norm(v)

        if s == 0:
            return np.eye(3)

        vx = np.array([[0, -v[2], v[1]],
                       [v[2], 0, -v[0]],
                       [-v[1], v[0], 0]])

        return np.eye(3) + vx + vx @ vx * ((1 - c) / (s**2))

    R = rotation_matrix(direction)

    def transform(x, y, z):
        pts = np.vstack((x.flatten(), y.flatten(), z.flatten()))
        pts = R @ pts
        pts[0] += start[0]
        pts[1] += start[1]
        pts[2] += start[2]
        return pts.reshape(3, *x.shape)

    x_cyl, y_cyl, z_cyl = transform(x_cyl, y_cyl, z_cyl)
    x_cone, y_cone, z_cone = transform(x_cone, y_cone, z_cone)

    ax.plot_surface(x_cyl, y_cyl, z_cyl, color=color, linewidth=0)
    ax.plot_surface(x_cone, y_cone, z_cone, color=color, linewidth=0)


# ==========================================================
# ====== INPUT FILE ========================================
# ==========================================================
file = "EMC_B0004.dat"
data = np.loadtxt(file, skiprows=1)

phi = data[:, 0] * np.pi / 180
theta = data[:, 1] * np.pi / 180
R = data[:, 2]

# ==========================================================
# ====== HIGH-RES GRID =====================================
# ==========================================================
nphi = 500
ntheta = 500

phinew = np.linspace(0, np.pi, nphi)
thetanew = np.linspace(0, 2*np.pi, ntheta)

phi_grid, theta_grid = np.meshgrid(phinew, thetanew)

Rnew = griddata(
    (phi, theta),
    R,
    (phi_grid, theta_grid),
    method='cubic'
)

Rnew = np.nan_to_num(Rnew, nan=np.nanmean(R))

# ==========================================================
# ====== SPHERICAL → CARTESIAN =============================
# ==========================================================
x = Rnew * np.cos(theta_grid) * np.sin(phi_grid)
y = Rnew * np.sin(theta_grid) * np.sin(phi_grid)
z = Rnew * np.cos(phi_grid)

# ==========================================================
# ====== PLOT ==============================================
# ==========================================================
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

# Color normalization
norm = plt.Normalize(vmin=np.min(Rnew), vmax=np.max(Rnew))
colors = plt.cm.jet(norm(Rnew))

# Surface plot
ax.plot_surface(
    x, y, z,
    facecolors=colors,
    rstride=1,
    cstride=1,
    linewidth=0,
    antialiased=True,
    shade=False
)

# ==========================================================
# ====== COLORBAR (FIXED + SAFE FOR 3D) ====================
# ==========================================================
mappable = plt.cm.ScalarMappable(cmap='jet', norm=norm)
mappable.set_array([])

cbar = fig.colorbar(
    mappable,
    ax=ax,
    shrink=0.45,   # size of colorbar
    pad=0.00001,      # 🔥 distance control (smaller = closer)
    aspect=18
)

cbar.ax.tick_params(labelsize=10)
cbar.set_label("Effective Mass", fontsize=12)

# ==========================================================
# ====== AXES SETTINGS =====================================
# ==========================================================
ax.set_box_aspect([1, 1, 1])
ax.set_axis_off()
ax.view_init(elev=35, azim=135)

# ==========================================================
# ====== HIGH-QUALITY ARROWS ===============================
# ==========================================================
maxR = np.max(R)
flex = 1.6 * maxR

draw_arrow(ax, [0,0,0], [1,0,0], flex, 'red')
draw_arrow(ax, [0,0,0], [0,1,0], flex, 'green')
draw_arrow(ax, [0,0,0], [0,0,1], flex, 'blue')

ax.text(flex, 0, 0, 'x', fontsize=16)
ax.text(0, flex, 0, 'y', fontsize=16)
ax.text(0, 0, flex, 'z', fontsize=16)

# ==========================================================
# ====== FINAL =============================================
# ==========================================================
plt.tight_layout()

plt.savefig("emc_3D_hole.png", dpi=800, bbox_inches='tight')
#plt.savefig("emc_3D_elec.pdf", bbox_inches='tight')

#plt.show()
