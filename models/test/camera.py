import bpy
import math
cam = bpy.data.objects["Camera"]
cam.rotation_mode = 'XYZ' #Not quaternions

DIRECTIONS = ['n','w', 's', 'e']

def renderDirection(vp, r, c, dir):
    cam.rotation_euler.z = (math.pi/2) * dir #Work with quarters
    bpy.context.scene.render.filepath = "/Users/gotankersley/desktop/img/%d-%d-%s.png" % (r,c, DIRECTIONS[dir])
    bpy.ops.render.render(write_still=True, use_viewport=True, scene="Camera")    
    print (r,c,dir)

#Loop through viewpoint empties
print ('---')
for obj in bpy.context.scene.objects:
    if obj.type == 'EMPTY' and obj.name.lower().startswith("v"):
        vp = obj
        dirs = vp['dir']
        
        cam.location = vp.location #Move camera to point
        r = math.floor(vp.location.y/3)
        c = math.floor(vp.location.x/3)
        
        # Render 
        #if 'n' in dirs: renderDirection(vp, r, c, 0)    
        if 'w' in dirs: renderDirection(vp, r, c, 1)    
        if 's' in dirs: renderDirection(vp, r, c, 2)    
        if 'e' in dirs: renderDirection(vp, r, c, 3)    
        

        
        
        
