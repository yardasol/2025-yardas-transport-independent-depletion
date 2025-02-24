import argparse

import numpy as np

import openmc
from openmc.deplete import get_microxs_and_flux, MicroXS
from openmc.mgxs import GROUP_STRUCTURES

#def parse_arguments():
#    parser = argparse.ArgumentParser()
#   parser.add_argument('-m', choices=['simple', 'full'],
#                       type=str,
#                       default='simple',
#                       help='depletion chain complexity')

#   args = parser.parse_args()
#   return str(args.m)

fuel = openmc.Material(name="uo2")
fuel.add_element("U", 1, percent_type="ao", enrichment=4.25)
fuel.add_element("O", 2)
fuel.set_density("g/cc", 10.4)

clad = openmc.Material(name="clad")
clad.add_element("Zr", 1)
clad.set_density("g/cc", 6)

water = openmc.Material(name="water")
water.add_element("O", 1)
water.add_element("H", 2)
water.set_density("g/cc", 1.0)
water.add_s_alpha_beta("c_H_in_H2O")

radii = [0.42, 0.45]
fuel.volume = np.pi * radii[0] ** 2

materials = openmc.Materials([fuel, clad, water])

pin_surfaces = [openmc.ZCylinder(r=r) for r in radii]
pin_univ = openmc.model.pin(pin_surfaces, materials)
bound_box = openmc.model.RectangularPrism(1.24, 1.24, boundary_type="reflective")
root_cell = openmc.Cell(fill=pin_univ, region=-bound_box)
geometry = openmc.Geometry([root_cell])

mode_dict = {'simple': (openmc.Settings(**{'batches': 50,
                                         'inactive': 10,
                                         'particles': 1000}),
                        '../../../openmc/tests/chain_simple.xml'),
             'full': (openmc.Settings(**{'batches': 125,
                                       'inactive': 25,
                                       'particles': 100000,
                                       'tallies': False}),
                      'chain_endbf71_pwr.xml')
            }
#mode = parse_arguments()
mode = 'full'
from_mg_flux = False
settings, chain_file = mode_dict[mode]
#settings.export_to_xml(f'settings-{mode}.xml')
#materials.export_to_xml('materials.xml')
#geometry.export_to_xml('geometry.xml')
energies = GROUP_STRUCTURES['CASMO-8'] ## Need to pick energy group
if from_mg_flux:
    flux = np.loadtxt(f'flux_{mode}.csv')
    micro = MicroXS.from_multigroup_flux('CASMO-8', flux, chain_file=chain_file)
    micro.to_csv(f'micro_xs_{mode}_mg.csv')
else:
    model = openmc.Model(geometry, materials, settings)
    fluxes, micros = get_microxs_and_flux(model, [materials[0]], energies=energies,
                                        chain_file=chain_file)
    # There's only one element but it's a list so we gotta pick out the singular
    # element
    np.savetxt(f'flux_{mode}.csv', fluxes[0], delimiter=',')
    micros[0].to_csv(f'micro_xs_{mode}.csv')

