import jsbsim
sim = jsbsim.FGFDMExec(jsbsim.get_default_root_dir())
print(sim.load_model("f22"))
#print(sim.query_property_catalog("ic/"))
sim.set_property_value("ic/h-sl-ft", 3000)
sim.set_property_value("ic/vc-kts", 90)
sim.set_property_value("ic/psi-true-deg",90)
sim.run_ic()
print(sim.query_property_catalog("throttle"))
print(sim.query_property_catalog("fcs"))

