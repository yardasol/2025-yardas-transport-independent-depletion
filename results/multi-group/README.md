## Multi-group transport-independent depletion

### Setup
To generate fluxes and cross sections for a new group strucutre, run:
```bash
python -g <group_structure_string>
```
`<group_strucutre_string>` must be a valid key of the `mgxs.GROUP_STRUCUTRES`
dictionary. If you want to get higher resolutuion cross sections for the full
depletion chain, run
```bash
python -m full -g <group_structure_string>
```

A directory matching the name of the group strucutre will be automatically
created, for example, for the `CASMO-8` group, results will be stored in the
`casmo8` directory.

### Running the depletion 

There is a `GRPS` array in the `run_cases.sh` script. You will need to run the
setup script for each entry you want to run depletion for.
