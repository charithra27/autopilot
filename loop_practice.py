for i in range(5):
    print(i)

for i in range(7200):
    sim.run()
    if i% 120 == 0:
        print("Sim time: ", sim.get_sim_time())
        print("Position: ", sim.get_property_value("position/h-sl-ft"))
        print("Velocity: ", sim.get_property_value("velocities/vc-kts"))
        print("Attitude: ", sim.get_property_value("attitude/psi-deg"))
        print("next second")
print (sim.get_property_value("position/h-sl-ft"))
print (sim.get_property_value("velocities/vc-kts"))
print (sim.get_property_value("attitude/psi-deg"))
