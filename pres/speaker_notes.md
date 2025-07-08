# Slide 1 (title) 
- Introduce self, universiy, topic of research?
- SciPy Committee

# Slide 2 (outline)
- Mention we want to motivate this work and give some background on the physics

# Slide 3 
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
- Reactors designed to ensure neutrons consumed = neutrons released

# Slide 5
- While the reactor is running, Uranium is used up, elements released from
    fission build up -> The composition fof the reactor at day 1 is not the
    composition oat day 2 or 3, and so on.
- Figure: We have capture breeding Plutonium, and fission utilziing Uranium. 
- why do we care about this?
    1) Neutron poisions (Xe 135, Sm 149) effect neutron economy -> absorbs
    neutrons before they can cause a fission. This informs practices like fuel
    2) Fissile Plutonium buildup changes the energy distribution of fission neutrons
    over time  (maybe take this out)
    3) Long-livded fission products in the fuel continue to give off heat and
    radiation after the fuel is removed from reaction -> important for waste
    disposal and reprocessing

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
- Transition: Let's focus on the quantities we need to solve

# Slide 9
- basically read the first block slide
- So where do we go from here? Which one of these quantities can 
- What if instead of solving for the flux at each timestep, we assume the flux
    is stable? What are the effects of this?
- Transition: We need a neutron transport code to try this in.

# Slide 10
- OpenMC, developed at MIT, now ANL
- Monte Carlo
- Python API for generating input, postprocessing, open source!


# Slide 11
- Does include a depletion module in python
- The basic flow is as follows

# Slide 12
- MicroXS: container to store cross sections on an energy grid for a specific
    domain
- function: run an OpenMC simulation to get XS + flux on energy grid; can define
    multiple domains
- IndependentOperator: Drop-in replacement for Operator class that is
    responsible for running OpenMC and processing the results.
   - skips that, uses static mg fluxes and MicroXS to get reaction rates

# Slide 13
- Read the slide

# Slide 14
- Let's get into the results

# Slide 15
- Error is relative to case 1
- Immediately see that case 3 is more accurate than case 2 (good!)
- General trend of increasing error w/ increasing time, but dependent on
    specific nuclides, timestep size (as we will see)
- Two groups of nuclides: more and less abundant
- General trend of more abundant nuclides having low (5 percent or less) concentration errors (U,
    Np239, Pu239, Pu240)
- Less abundant nuclides have high (10 percent or more)

# Slide 16
- Same trend w case 3 and 2
- Overprediction of Pu 241, other actinides

# Slide 17
- Specific analysis requires looking at the reaction rates
- Pu241 comes from n,gamma of Pu240
- Overprediction error matches the trend in the concentration errror

# Slide 18
- Fission product error is much lower
- The low concentration error of u235 propogates to the fission products!

# Slide 19
- same

# Slide 20 and 21
- No significant difference with larger group structures
