import jsbsim
sim = jsbsim.FGFDMExec(jsbsim.get_default_root_dir())
print(sim.load_model("c172x"))