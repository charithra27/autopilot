import jsbsim
sim = jsbsim.FGFDMExec(jsbsim.get_default_root_dir())
print(sim.load_model("f22"))
print(sim.query_property_catalog("throttle"))