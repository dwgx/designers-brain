import bpy, json
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.rigidbody.world_add()
rw = bpy.context.scene.rigidbody_world
print("DEFAULTS:", json.dumps({"substeps": rw.substeps_per_frame, "iters": rw.solver_iterations,
      "time_scale": rw.time_scale, "use_split_impulse": getattr(rw,'use_split_impulse','n/a'),
      "fps": rw.point_cache.frame_step if hasattr(rw.point_cache,'frame_step') else 'n/a'}))
