
# All values from https://agriculture.vic.gov.au/crops-and-horticulture/grains-pulses-and-cereals/crop-production/general-agronomy/estimating-crop-yields-and-crop-losses

# tonnes per hectare = (A × B) / K
# A = average number of grains per head
# B = average number of heads per 50 cm of row
# K the number of grains in the half metre of row at 17.5 cm row spacing that is equivalent to 1 Tonne per hectare

# [(Row Spacing (mm), Converstion Factor)]
rowComp = [
(150, 1.17),
(175, 1.00),
(200, 0.88),
(225, 0.78),
(250, 0.70),
(275, 0.64),
(300, 0.58),
(325, 0.54),
(350, 0.50)]

# Known constants (K)
# [(Weight of 100 grains (g), K)]
grainWeight = [
(2.6, 336),
(2.8, 312),
(3.0, 292),
(3.2, 273),
(3.4, 257),
(3.6, 243), # Wheat
(3.8, 230),
(4.0, 219), # Oats
(4.2, 208),
(4.4, 199), # Barley
(4.6, 190),
(4.8, 182),
(16, 55), # Lupin
(18, 47), # Chickpead
(50, 17.5),
(70, 12.5) # Faba Bean
]

def basicModel(grainsPerHead, headsPer50cm, K, rowCompensation):
    return ((grainsPerHead*headsPer50cm)/K) * rowCompensation