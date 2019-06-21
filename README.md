# FEL-CaseStudy-SS19

Semester Project for the master course Accelerator Physics (SS19) at KIT.
Design/ Scratch of a Free Electron Laser (FEL).

## Requirements

Specification of the laser to be produced:

* Light wavelength: &nbsp; ![](https://latex.codecogs.com/gif.latex?%5Clambda%20%5Cleqslant%200.5%20%5C%2C%5Ctextup%7B%5CAA%7D)

* Exposure time: &nbsp;&nbsp; ![](https://latex.codecogs.com/gif.latex?t%20%5Cleqslant%2010%20%5C%2C%5Ctextup%7Bfs%7D)

* Repetition Rate: &nbsp; ![](https://latex.codecogs.com/gif.latex?f%20%5Cgeqslant%20100%20%5C%2C%5Ctextup%7BHz%7D)


Energy efficiency and total length of the machine should also be optimised. (to be considered later)

## Ideas and TODO

Use electron source from European XFEL^[[1](#references)]

- [ ] **Lattice Design**:
    - [ ] focusing, optic functions
    - [ ] in accelerating sector
    - [ ] also in undulator
- [ ] **Undulator Design**:
    - [ ] length, magnetic field strength...
    - [ ] undulator strength parameter
- [ ] **Acceleration, RF Cavity**:
    - [ ] required energy of electrom beam at entrance of undulator
    - [ ] length/ strength of the cavity (constrained by power supply)
- [ ] **Bunch Compressor**:
    - [ ] length, B field
    - [ ] bunch length/spacing at entrance (after acceleration)
    - [ ] bunch length/spacing needed at exit


---
_Side Notes:_
    The parameters all depend on each other and form a subspace in high dimensional parameter space.
    Maybe first fix some typical (physical realisable) values and start calculating others. E.g. magnet field strength should <1.5T...

## Useful Packages



- [ELEGANT](https://ops.aps.anl.gov/manuals/elegant_latest/elegant.html), [source code and executables](https://www.aps.anl.gov/Accelerator-Operations-Physics/Software#elegant)
    > elegant is an accelerator code that computes beta functions, matrices, orbits, floor coordinates, amplification factors, dynamic aperture, and more. It does 6-D tracking with matrices and/or canonical integrators, and supports a variety of time-dependent elements. It also does optimization (e.g., matching), including optimization of tracking results. It is the principle accelerator code used at APS.

- [Accelerator Toolbox](http://atcollab.sourceforge.net/),and the new [github page](https://github.com/atcollab/at)
    >Accelerator Toolbox (AT) is collection of tools to model storage rings and beam transport lines in **MatLab**.
    With AT it is possible to:
    > - create and manipulate accelerator lattice elements, which are stored in a MatLab structure usually called “THERING”.
    > - track particles through the lattice, selecting the more convenient integrator to represent the element physics.
    > - compute accelerator parameters and beam properties, generating new scripts or taking advantage of the existing ones

- [MAD-X](http://mad.web.cern.ch/mad/)
    > MAD-X is a project with a long history, aiming to be at the forefront of computational physics in the field of particle accelerator design and simulation. Its scripting language is de facto the standard to describe particle accelerators, simulate beam dynamics and optimize beam optics at CERN.
    > MAD-X is released for the Linux, Mac OS X and Windows platforms for 32 bit (on demand) and 64 bit architectures ([see releases](http://mad.web.cern.ch/mad/releases.html)). The source code is written in C, C++, Fortan77 and Fortran90.



## References

- [FEL wikipedia page](https://en.wikipedia.org/wiki/Free-electron_laser)

- [European XFEL](https://www.xfel.eu/facility/overview/index_eng.html)

-  More to come

and maybe some papers/design reports with machine parameters
