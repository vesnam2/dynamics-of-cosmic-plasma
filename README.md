# Dynamics of Cosmic Plasma – Programming Projects

This repository contains a collection of programming projects completed as part of the
*Dynamics of Cosmic Plasma* course from summer semester 2024. The projects focus on numerical simulation of charged
particle motion in magnetic and electromagnetic fields relevant to space and astrophysical
plasma physics.


## Repository Structure

.
├── Project1/
├── Project2/
├── Project3/
├── Project4/
└── README.md


Each project directory contains the corresponding source code, numerical results, and
visualizations produced during the simulations.

---

## Projects Description

### Project 1: Motion of Charged Particles in a Homogeneous Magnetic Field

Numerical simulation of the trajectories of an electron, a proton, and an alpha particle in a
homogeneous magnetic field. In addition to tracking particle trajectories, the time evolution
of their kinetic energies is analyzed in order to illustrate fundamental properties of charged
particle motion in magnetic fields.

---

### Project 2: Particle Motion in Prescribed Magnetic and Electromagnetic Fields

Simulation of charged particle trajectories in:
- a spatially varying magnetic field with a single non-zero component along the z-axis, and
- a homogeneous and stationary electromagnetic field configuration.

The magnetic field is defined with a linear spatial dependence, while the electric field is
introduced consistently to study its influence on particle dynamics.

---

### Project 3: Particle Trajectories in Non-Uniform Magnetic Field Configurations

Numerical study of particle motion in a non-uniform, stationary magnetic field with multiple
spatial dependencies. The project investigates how spatial gradients in the magnetic field
affect particle trajectories, extending the analysis beyond homogeneous field configurations.

A comparison with motion in combined homogeneous electric and magnetic fields is also included.

---

### Project 4: Motion of Non-Relativistic Particles in the Earth's Dipole Magnetic Field

Numerical modeling of non-relativistic charged particle motion in the approximation of a
time-independent dipole magnetic field of the Earth. The equations of motion are integrated
using the fourth-order Runge–Kutta (RK4) method.

This project is based on a reference implementation provided during the course and follows
the methodology presented in the literature:
- Garcia-Farieta & Hurtado (2019)
- Physical constants adopted from Ozturk (2012)

---

## Numerical Methods and Implementation

The projects employ standard numerical integration techniques for solving the equations of
motion of charged particles in electromagnetic fields. In particular:
- explicit time integration schemes
- fourth-order Runge–Kutta (RK4) method
- analysis of particle trajectories and kinetic energy evolution

The initial code framework and problem setup were provided by the course instructor. The
implementation, modification, parameter studies, and analysis were carried out independently
as part of the course assignments.

---

## References

- Garcia-Farieta, J. E., & Hurtado, A. (2019), *Revista Mexicana de Física E*
- Ozturk, S. (2012), *American Journal of Physics*
