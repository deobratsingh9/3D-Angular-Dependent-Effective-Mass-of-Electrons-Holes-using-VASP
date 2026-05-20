# 3D Angular Dependent Effective Mass of Electrons & Holes using VASP

This repository provides a workflow for calculating and visualizing the 3D angular dependent effective mass of electrons and holes using VASP and Python.

The workflow includes:

* Effective mass calculations
* Angular dependent effective-mass analysis
* 3D visualization of effective-mass surfaces
* Publication-quality plotting using Python

---

# ⚙️ Workflow Overview

```text
VASP Effective Mass Calculation
              ↓
Effective-Mass Data Extraction
              ↓
Angular Dependent Analysis
              ↓
3D Surface Visualization
              ↓
Publication-Quality Plots
```

---

# 📂 Step 1: Run Effective Mass Calculations in VASP

Perform electronic structure and effective-mass calculations using VASP.

After the calculation finishes, effective-mass data files are generated.

---

# 📁 Step 2: Collect Required Files

Keep the following files in the same directory:

```text
EMC_B0005.dat
effective_mass_3D.py
```

---

# 🐍 Step 3: Use Python Environment

```bash
Module load python3 version

```
---

# ▶️ Step 4: Run the Python Script

Run the workflow:

```bash
python effective_mass_3D.py
```

---

# 📊 Step 5: Data Processing

The workflow automatically:

* Reads angular dependent effective-mass data
* Interpolates effective-mass surfaces
* Converts spherical coordinates into Cartesian coordinates
* Generates smooth 3D surfaces
* Computes effective-mass anisotropy visualization

---

# 📈 Step 6: Generate 3D Visualization

The workflow generates:

* 3D electron effective-mass surfaces
* 3D hole effective-mass surfaces
* Angular dependent anisotropy plots
* Publication-quality visualization figures

---

# 💾 Step 7: Output Files

Generated figures are saved automatically.

Example:

```text
emc_3D_elec.png
```

---

# 🔬 Applications

This workflow is useful for:

* Semiconductor physics
* Carrier transport
* Electron mobility analysis
* Hole mobility analysis
* Anisotropic materials
* Electronic structure analysis
* Computational materials science

---

# 🚀 Final Workflow Summary

```text
VASP → Effective Mass → Angular Analysis → 3D Visualization → Publication-Quality Plots
```

---

# 📁 Repository Contents

```text
README.md
effective_mass_3D.py
EMC_B0005.dat
example_outputs/
```

---

# ⭐ Citation

If you use this workflow in your research, please cite:

VASP

and relevant effective-mass methodology references.
