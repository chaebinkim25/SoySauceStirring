import bpy
import numpy as np



for obj in bpy.data.objects:
    obj.hide_viewport = False
    obj.hide_render = False
    obj.hide_set(False)

for obj in bpy.data.objects:
    obj.select_set(True)

# Clear existing objects
bpy.ops.object.delete()

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        print("delete cam")
        bpy.data.objects.remove(obj)
    elif obj.type == 'LIGHT':
        print("delete light")
        bpy.data.objects.remove(obj, do_unlink=True)
    elif obj.type == 'POINT':
        print("delete point")
        bpy.data.objects.remove(obj, do_unlink=True)
    elif obj.type == 'SUN':
        print("delete sun")
        bpy.data.objects.remove(obj, do_unlink=True)


world = bpy.context.scene.world
if not world:
    world = bpy.data.worlds.new("NewWorld")
    bpy.context.scene.world = world
    
world.use_nodes = True
bg_node = world.node_tree.nodes.get("Background")
if bg_node:
    bg_node.inputs["Color"].default_value = (1, 1, 1, 1);
    


# Create a cube and scale it into a long shape
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
long_cube = bpy.context.object
long_cube.name = "SpoonHandle"

# Scale the cube to make it long (e.g., a rectangular prism)
long_cube.scale = (2, 0.2, 0.1)  # Width, Depth, Height

bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=0.1, location=(1, 0, 0))
cylinder = bpy.context.object
cylinder.name = "SpoonHead"

cylinder.scale = (1, 0.7, 1)

long_cube.select_set(True)
cylinder.select_set(True)

bpy.context.view_layer.objects.active = cylinder

bpy.ops.object.join()
spoon = bpy.context.object

mat_spoon = bpy.data.materials.new(name=("SoySource"))
mat_spoon.diffuse_color = (0.3, 0.02, 0.02, 1)

spoon.data.materials.append(mat_spoon)



bpy.ops.mesh.primitive_cylinder_add(radius=0.4, depth=0.05, location=(0, 0, 0.075))
soySauce = bpy.context.object
soySauce.name = "SoySauce"

soySauce.scale = (1, 1, 1)

mat_soy = bpy.data.materials.new(name=("SoySource"))
mat_soy.diffuse_color = (0.08, 0.05, 0.03, 1)

soySauce.data.materials.append(mat_soy)
soySauce.parent = spoon






bpy.ops.mesh.primitive_cube_add(size=1, location=(1, -0.5 * 0.7, 0.05))
soySpill = bpy.context.object
soySpill.name = "Soyspill"
soySpill.data.materials.append(mat_soy)
soySpill.scale = (0, 0, 0)



bpy.ops.mesh.primitive_cylinder_add(radius=2, depth=1, location=(0, 0, -1.5))
pot_outer = bpy.context.object
pot_outer.name = "PotOuter"

bpy.ops.mesh.primitive_cylinder_add(radius=1.8, depth=0.8, location=(0, 0, -1.3))
pot_inner = bpy.context.object
pot_inner.name = "PotInner"

pot_outer.modifiers.new(name='Boolean', type='BOOLEAN')
print("HI")
print(pot_outer.modifiers.keys())
pot_outer.modifiers['Boolean'].operation = 'DIFFERENCE'
pot_outer.modifiers['Boolean'].object = pot_inner

bpy.ops.object.modifier_apply(modifier='BOOLEAN')

pot_outer.scale = (1, 1, 1)

pot_inner.hide_viewport = True
pot_inner.hide_render = True

mat_pot = bpy.data.materials.new(name=("Pot"))
mat_pot.diffuse_color = (0.02, 0.0, 0.0, 1)

pot_outer.data.materials.append(mat_pot)


bpy.ops.mesh.primitive_cylinder_add(radius=1.8, depth=0.6, location=(0, 0, -1.5))
soup = bpy.context.object
soup.name = "Soup"

soup.scale = (1, 1, 1)

mat_soup = bpy.data.materials.new(name=("Soup"))
mat_soup.diffuse_color = (0.9, 0.7, 0.5, 1)

soup.data.materials.append(mat_soup)


animation = True

print("Hi")

frame = 1

def one_iteration():

    global frame
    
    soySauce.hide_viewport = True
    soySauce.hide_render = True
    soySauce.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySauce.keyframe_insert(data_path="hide_render", frame=frame)
    
    frame += 1
    soySauce.scale = (0, 0, 0)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    
    soySauce.hide_viewport = False
    soySauce.hide_render = False
    soySauce.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySauce.keyframe_insert(data_path="hide_render", frame=frame)

    frame += 7
    soySauce.scale = (1, 1, 1)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    

    bpy.context.scene.frame_set(frame)
    spoon.rotation_euler.x += 0.1
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)
    soySauce.keyframe_insert(data_path="location", frame=frame)
    

    soySpill.hide_viewport = True
    soySpill.hide_render = True
    soySpill.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySpill.keyframe_insert(data_path="hide_render", frame=frame)
    
    frame += 7
    bpy.context.scene.frame_set(frame)
    spoon.rotation_euler.x += 0.1
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)

    r = 0.4 * soySauce.scale.x
    soySauce.location.y = -0.5 + r
    soySpill.scale = (0.1, 0.05, 0)

    soySauce.keyframe_insert(data_path="scale", frame=frame)
    soySauce.keyframe_insert(data_path="location", frame=frame)
    soySpill.keyframe_insert(data_path="scale", frame=frame)
    soySpill.keyframe_insert(data_path="location", frame=frame)
    

    soySpill.hide_viewport = False
    soySpill.hide_render = False
    soySpill.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySpill.keyframe_insert(data_path="hide_render", frame=frame)

    while soySauce.scale.x > 0.1:
        frame += 1
        bpy.context.scene.frame_set(frame)
        spoon.rotation_euler.x += 0.1
        soySauce.scale.x -= 0.1
        soySauce.scale.y -= 0.1
        r = 0.4 * soySauce.scale.x
        soySauce.location.y = -0.5 + r

        soySpill.scale.z += 0.1
        soySpill.location.z = 0.1 - 0.35 * np.sin(spoon.rotation_euler.x) - soySpill.scale.z / 2
        soySpill.location.y = -0.1 * np.sin(spoon.rotation_euler.x) -0.35 * np.cos(spoon.rotation_euler.x)
        
        spoon.keyframe_insert(data_path="rotation_euler", frame=frame)
        soySauce.keyframe_insert(data_path="scale", frame=frame)
        soySauce.keyframe_insert(data_path="location", frame=frame)
        soySpill.keyframe_insert(data_path="scale", frame=frame)
        soySpill.keyframe_insert(data_path="location", frame=frame)

    print(soySpill.location.z, soySpill.scale.z)
    soySauce.hide_viewport = True
    soySauce.hide_render = True
    soySauce.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySauce.keyframe_insert(data_path="hide_render", frame=frame)
    spoon.keyframe_insert(data_path="location", frame=frame)
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)

    while soySpill.scale.z > 0.1:
        frame += 1
        bpy.context.scene.frame_set(frame)
        
        soySpill.scale.z -= 0.2
        soySpill.location.z -= 0.1
        
        soySpill.keyframe_insert(data_path="scale", frame=frame)
        soySpill.keyframe_insert(data_path="location", frame=frame)

        print(soySpill.scale.z)
    
    soySpill.hide_viewport = True
    soySpill.hide_render = True
    soySpill.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySpill.keyframe_insert(data_path="hide_render", frame=frame)
    soySauce.keyframe_insert(data_path="scale", frame=frame)
    soySauce.keyframe_insert(data_path="location", frame=frame)

    frame += 5
    spoon.rotation_euler.y += np.pi / 2
    spoon.location.x = np.cos(0.4 * np.pi)
    spoon.location.y = -np.sin(0.4 * np.pi)
    spoon.location.z = -1.5
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)
    spoon.keyframe_insert(data_path="location", frame=frame)
   
    mat_soup.keyframe_insert(data_path="diffuse_color", frame=frame)
    
    for theta in np.arange(0.6 * np.pi, 2.1 * np.pi, 0.2 * np.pi):
        frame += 2
        spoon.location.x = np.cos(theta)
        spoon.location.y = -np.sin(theta)
        spoon.keyframe_insert(data_path="location", frame=frame)
        
        for i in range(3):
            mat_soup.diffuse_color[i] -= 0.01
        
        mat_soup.keyframe_insert(data_path="diffuse_color", frame=frame)
        
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    soySauce.scale = (0, 0, 0)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    
    soySauce.keyframe_insert(data_path="location", frame=frame)    
    soySauce.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySauce.keyframe_insert(data_path="hide_render", frame=frame)
    mat_soy.keyframe_insert(data_path="diffuse_color", frame=frame)

    frame += 5
    soySauce.hide_viewport = False
    soySauce.hide_render = False
    soySauce.scale = (0.8, 0.8, 0.8)
    soySauce.location = (0, 0, 0.075)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    
    soySauce.keyframe_insert(data_path="location", frame=frame)    
    soySauce.keyframe_insert(data_path="hide_viewport", frame=frame)
    soySauce.keyframe_insert(data_path="hide_render", frame=frame)

    mat_soy.diffuse_color = mat_soup.diffuse_color
    mat_soy.keyframe_insert(data_path="diffuse_color", frame=frame)

    frame += 15
    spoon.rotation_euler.x = 0
    spoon.rotation_euler.y = 0
    spoon.location.z = -0.5
    spoon.keyframe_insert(data_path="location", frame=frame)
    spoon.keyframe_insert(data_path="rotation_euler", frame=frame)

    
    frame += 2
    spoon.location.z = 0
    spoon.keyframe_insert(data_path="location", frame=frame)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    


    frame += 2
    soySauce.scale = (0, 0, 0)
    soySauce.keyframe_insert(data_path="scale", frame=frame)    
    mat_soy.keyframe_insert(data_path="diffuse_color", frame=frame)
    soySpill.keyframe_insert(data_path="location", frame=frame)
    soySpill.keyframe_insert(data_path="scale", frame=frame)


    frame += 2
    mat_soy.diffuse_color = (0.08, 0.05, 0.03, 1)
    mat_soy.keyframe_insert(data_path="diffuse_color", frame=frame)
    soySpill.location = (1, -0.5 * 0.7, 0.05)
    soySpill.scale = (0, 0, 0)
    soySpill.keyframe_insert(data_path="location", frame=frame)
    soySpill.keyframe_insert(data_path="scale", frame=frame)

    print("Frame:", frame)
    
    
    
if animation:
    for _ in range(3):
        one_iteration()

make_gif = True

bpy.ops.object.camera_add(location=(5, -4, 4.5))
camera = bpy.context.object
camera.rotation_euler=(np.pi*48/180, 0, np.pi*52/180)
bpy.context.scene.camera = camera

bpy.ops.object.light_add(type='SUN', location=(5, -5, 5))
light = bpy.context.object
light.name = "MyLight"

light.data.energy = 1
light.data.angle = np.pi

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = frame 
bpy.context.scene.frame_set(10)


if make_gif:
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "//animation_frames/"
    bpy.ops.render.render(animation=True)
