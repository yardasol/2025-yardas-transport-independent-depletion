# Slide 1 (title) 
- Introduce self, universiy, topic of research?
- SciPy Committee

# Slide 2 (outline)
- Mention we want to motivate this work and give some background on the physics

# Slide 3 
- New reactors need to be simulated before we can build them
- 7D NTE (ADD BONUS SLIDE FOR THIS)
- Two categories of methods used to solve NTE:
    1. Deterministic methods (FE, FD, Nodal, etc)
    2. Monte Carlo method (this method was actually invented by John von Neumann
       and Stansilaw Ulam to model neutron transport back in the 1940s, and now
       describes a large category of stochastic methods used in many 
       computational scientific domains)
- Regardess of method, reactor geometries are complicated: thousands of surfaces,
    regions (Point out the ATR)
- Low errors on 1:1 models require lots of computational power (supercomputers)

# Slide 4
- The driving mechanism of a nuclear reator is the fission chain reaction.
- neutron hits uranium, causing it to split.
- Releases new elements, neutrons, energy in form of heat
- Some nuclei will absorb a neutron becoming a different isotope of the same
    elment, or convert that neutron into a proton and become a new elment
    entirely
- Some of the nuclei produced are unstable and will spontaneously decay.
    Sometimes this releasses a neutron.
- Reactors designed to ensure neutrons consumed = neutrons released
- Cocnentration of nuclides in reactor is constantly changing due to fission,
    neutron capture, and radioactive decay

# Slide 5
- While the reactor is running, Uranium is used up, elements released from
    fission build up -> The composition fof the reactor at day 1 is not the
    composition oat day 2 or 3, and so on.
- Figure: We have capture breeding Plutonium, and fission utilziing Uranium. 
- why do we care about this?
    1) Neutron poisions (Xe 135, Sm 149) effect neutron economy -> absorbs
    neutrons before they can cause a fission. This informs reactor design to
    mitigate these effects
    2) Fissile Plutonium buildup changes the energy distribution of fission neutrons
    -> Reactors designed for low energy neutrons, more plutonium 
    3) Fission products in the fuel continue to decay long after fuel is removed
    from the reactor reaction -> informs practices for fuel handling, storage,
    and reprocessing

- Transition to the next slide: from a computational perspetive, depletion makes
   everything more expensive

# Slide 6
- Depletion calculations must track thousands of nuclides
- recall the ATR: each fuel element is in a different place in the reactor, and
    will have a difference concentration from each other fuel element.
- Axial differences in neutron population -> axial discretization -> orders of
    magnitude to calculation
- These kinds of problems can occupy clusters for days
- otr: small example of how reactions can link up in a chain

# Slide 7
- Let's take a closer look at depletion to see if there is a way we can make it
    cheaper (spoiler alert: we can (based on the title of the presentation))

# slide 8
- apologize for the math 
- mention the 4 terms
- Define te quantities and their units
   - XS is reaction target area
- Transition: We need a neutron transport code to implement this equation in

# Slide 9
- OpenMC, developed at MIT, now ANL
- Monte Carlo
- Python API for generating input, postprocessing, open source!
- Let's talk a little bit about the implementation of depletion in a code like
    OpenMC

# Slide 10
- basically read the first block slide
- So where do we go from here? Which one of these quantities can 
- What if instead of solving for the flux at each timestep, we assume the flux
    is stable? What are the effects of this?
- Transition: We need a neutron transport code to try this in.

# Slide 11
- MicroXS: container to store cross sections on an energy grid for a specific
  domain

- function: run an OpenMC simulation to get XS + flux on energy grid; can
  define multiple domains

- IndependentOperator: Drop-in replacement for Operator class that is
     responsible for running OpenMC and processing the results.
  - performs step 2 in the simplifid algorithm using static mg fluxes and
     MicroXS to get prodiction and consumption terms

# Slide 13
- Read the slide
- Xenon poisioning: buildup of Xe 135 in the reactor can cause power
    fluctuations.
- Long timesteps: not as coupled to transport

# Slide 14
- Let's get into the results. First we will look at the actinides, which include
    Uranium and elements near it such Plutonium and Thorium that are created via
    neutron absorption. Actinides are interesting as they drive nuclear
    chain reactions (or produce fissile elements that do so)

# Slide 15
- Error is relative to case 1
- Notice the diference scales bewteen Case 2 error and Case 3 error
- Immediately see that case 3 is more accurate than case 2 (good!)
- General trend of increasing error w/ increasing time, but dependent on
    specific nuclides, timestep size (as we will see)
- Two groups of nuclides: more and less abundant
- General trend of more abundant nuclides having low (5 percent or less) concentration errors (U,
    Np239, Pu239, Pu240)
- Less abundant nuclides have high (10 percent or more) errors

# Slide 17
- Same trend w case 3 and 2
- Overprediction of Pu 241, other actinides

# Slide 16
- Specific analysis requires looking at the reaction rates
- Pu241 comes from n,gamma of Pu240
- Overprediction error matches the trend in the concentration errror

# Slide 18
- Fission product error is much lower
- The low concentration error of u235 propagates to the fission products!

# Slide 19
- same

# Slide 20 and 21
- No significant difference with larger group structures

# Slide 22
