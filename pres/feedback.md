
# General
- Add authors to title slide
- include scipy position in introduction
- typos
- make set spell always on
- Think about how the slides will set up the points you make in the conclusion
- replace multigroup with discrete energy group

# Slide 3
- audience doesn't know the space
- Need to explain how the ATR is a complicated geometry
- Add commentary where I explain the image, set the foundation for things I'm
    going to talk about in later slides
- Say what the fuel is
- Talk about in a time dependent simulation things can change


# Slide 4
- well done

# Slide 5
- Get rid of the D&H quote, use my own words
- Find a better version of the fig (should be digital)
- Find a complimentary fig that shows the buildup of fission products
- "The relative concentrations are changing. There's capture and fission. Things
    are changing. Compostiion of reactor at day 1 is not the compostion at day
    2,3,etc"
    Ties depletion into the presentation
- Flowcharts exist that might be useful? May be too out of bounds
- Write down why we actually care -> be explicit (Xe135)
    - Iodine pit caused chernobyl

- Dont talk about nonproliferation
    - reactor design, decay heat (fuel storage)

# Slide 6
- spend more time here
- rections
- could be a good opportunity to put some quantification
- depeltions occupy a supercomputer if you want to get full detail
- occupy a cluster for days

# Slide 8
- good!

# Slide 9
- explains for the first time that we should couple transport from depletion
- You haven't mentioned this, might be good to do so around slide 5 or 6
- changing slides -> changes reactor physics
- include "flux", "cross section"

    first bullet -> problem defined
    second bullet -> material property looked up (file i/o), delete jeff, endf
    third bullet -> concentation of neutrons in the reactor, requries transport
        sim

    "we're not sure how accurate this is" -> see madicken's rephrase in the
    notes (hypothesis approach) "how accurate will this be"

# Slide 10
- Actually cite OpenMC
- Explain which pacakges OpenMC leverages h5py + numpy + matplotlib
- Call it what it is (Monte Carlo, we invented it!! john von neuman and
    stansilaw ulam invented it to solve neutron transport)

# Slide 11
same comment on packages

# Slide 12
- when you explain the terms in slide 5, think abt this slide and how these
    terms will connect to these functions
- put those variables in this slides
- reframing in earlier slides will help with this slide (independentoperator
    decoupling depletion from transport)

# Slide 13
- expand pwr
- reacalculated (typo)
- motivate case 3 (time dependent depletion simulation)
- label the colors
- Add real fuel pin picture, maybe switch to XZ axis
- Be more specific on why we picked two different timesteps
    - Xe135 (3 day) (short term), close time coupling
    - Extreme long, not as coupled

# Slide 15
- make it clear that transport coupled depletion is the ground truth (put this
    on the slide or in the caption)
- describe the plots, colors, axes (consider replotting the x-axes for B), or
    repeat this every slide
- "each of these in interesting in its own right, im gonna focus on plutoium"
- "there will be a similar story with each of these nuclides"

# Slide 17
- error coming from N or phi?
- Katy wants to see if error is coming from difference in phi or difference in
    N?
- "constant microscopic cross sections" -> make it clear that phi is constant
- explain what I mean by constant

# Slide 23
- much more convincing if I have an actual time for how long each simulation
    took!!! transport indepednent depletion is wayyy faster


go thru acknowldgements faster, don't need to state 
leave acks up while answering questions
