import bpy
cam = bpy.data.objects["Camera"]
cam.location = (0, 1, 0)
bpy.context.scene.render.filepath = "/Users/gotankersley/desktop/img/cool.png"
bpy.ops.render.render(write_still=True, use_viewport=True, scene="Camera")