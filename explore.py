import jsbsim
sim = jsbsim.FGFDMExec(jsbsim.get_default_root_dir())
print(sim.load_model("c172x"))
#print(sim.query_property_catalog("ic/"))
sim.set_property_value("ic/h-sl-ft", 3000)
sim.set_property_value("ic/vc-kts", 90)
sim.set_property_value("ic/psi-true-deg",90)
sim.run_ic()
print(sim.get_property_value("ic/terrain-elevation-ft"))
for i in range(7200):
    sim.run()
    if i% 120 == 0:
        print("Sim time: ", sim.get_sim_time())
        print("Position: ", sim.get_property_value("position/h-sl-ft"))
        print("Velocity: ", sim.get_property_value("velocities/vc-kts"))
        print("Attitude: ", sim.get_property_value("attitude/psi-deg"))
        print("Altitude AGL: ", sim.get_property_value("position/h-agl-ft"))

        print("next second")
print (sim.get_property_value("position/h-sl-ft"))
print (sim.get_property_value("velocities/vc-kts"))
print (sim.get_property_value("attitude/psi-deg"))
print(sim.get_property_value("position/h-agl-ft"))

print(sim.get_sim_time())

print(sim.query_property_catalog("agl"))
print(sim.query_property_catalog("terrain"))
