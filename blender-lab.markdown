---
layout: default
title: MTEC2002 - Blender Lab
---
Blender Lab
===

###Objectives
* Generate objects in blender.
* Simple animation and keyboard control in blender.

###Starting Blender w/ Output to Terminal
* To see debug info from the scripts that you run in Blender:
* Open Finder.
* In finder, navigate to the Applications folder (click on Macintosh HD -> Applications).
* Right click or control click on the Blender icon.  
* Choose "Show Package Contents" from the context menu.

![context menu](./resources/img/package-contents.png)

* Go into Contents -> MacOS.
* Double-click on blender to start.


![blender icon](./resources/img/blender.png)

* Switch to scripting layout

![Scripting layout](./resources/img/scripting-layout.png)

* You can create scripts in the text window
* You can run commands in the interactive Python shell

### bpy
The built-in blender python module is called bpy.  See the [quickstart guide](http://www.blender.org/documentation/blender_python_api_2_59_0/info_quickstart.html) for an overview.  Check out the [api documentation](http://www.blender.org/documentation/blender_python_api_2_63_2/)

Note that __this version of blender comes with Python 3__ installed!

{% highlight pycon %}
>>> import bpy
>>> dir(bpy)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'app', 'context', 'data', 'ops', 'path', 'props', 'types', 'utils']
{% endhighlight %}

### Tips 
* find sample scripts here:
 /Applications/blender-2.63-release-OSX_10.5_i386/blender.app/Contents/MacOS/2.63/scripts/addons/
* use ctrl + SPACE to autocomplete in Python console
* hover over ui elements to see Python code


![Hover](./resources/img/hover-code.png)

### bpy.data
bpy.data represents blender "datablocks".  They can be objects, scenes, materials, etc...
{% highlight pycon %}
>>> bpy.data
<bpy_struct, BlendData at 0x554b020>

{% endhighlight %}

### bpy.data.objects and object attributes
{% highlight pycon %}
>>> bpy.data.objects
<bpy_collection[3], BlendDataObjects>

>>> bpy.data.objects[0]
bpy.data.objects['Camera']

>>> bpy.data.objects[1]
bpy.data.objects['Cube']

>>> bpy.data.objects[2]
bpy.data.objects['Lamp']

>>> bpy.data.objects['Cube']
bpy.data.objects['Cube']

>>> dir(bpy.data.objects['Cube'])
['__doc__', '__module__', '__slots__', 'active_material', 'active_material_index', 'active_shape_key', 'active_shape_key_index', 'animation_data', 'animation_data_clear', 'animation_data_create', 'animation_visualisation', 'bl_rna', 'bound_box', 'children', 'closest_point_on_mesh', 'collision', 'color', 'constraints', 'copy', 'cycles_visibility', 'data', 'delta_location', 'delta_rotation_euler', 'delta_rotation_quaternion', 'delta_scale', 'dimensions', 'draw_bounds_type', 'draw_type', 'dupli_faces_scale', 'dupli_frames_end', 'dupli_frames_off', 'dupli_frames_on', 'dupli_frames_start', 'dupli_group', 'dupli_list', 'dupli_list_clear', 'dupli_list_create', 'dupli_type', 'empty_draw_size', 'empty_draw_type', 'empty_image_offset', 'field', 'find_armature', 'game', 'grease_pencil', 'hide', 'hide_render', 'hide_select', 'is_duplicator', 'is_modified', 'is_updated', 'is_updated_data', 'is_visible', 'layers', 'library', 'location', 'lock_location', 'lock_rotation', 'lock_rotation_w', 'lock_rotations_4d', 'lock_scale', 'material_slots', 'matrix_basis', 'matrix_local', 'matrix_parent_inverse', 'matrix_world', 'mode', 'modifiers', 'motion_path', 'name', 'parent', 'parent_bone', 'parent_type', 'parent_vertices', 'particle_systems', 'pass_index', 'pose', 'pose_library', 'proxy', 'proxy_group', 'ray_cast', 'rna_type', 'rotation_axis_angle', 'rotation_euler', 'rotation_mode', 'rotation_quaternion', 'scale', 'select', 'shape_key_add', 'show_axis', 'show_bounds', 'show_name', 'show_only_shape_key', 'show_texture_space', 'show_transparent', 'show_wire', 'show_x_ray', 'slow_parent_offset', 'soft_body', 'tag', 'to_mesh', 'track_axis', 'type', 'up_axis', 'update_tag', 'use_dupli_faces_scale', 'use_dupli_frames_speed', 'use_dupli_vertices_rotation', 'use_fake_user', 'use_shape_key_edit_mode', 'use_slow_parent', 'user_clear', 'users', 'users_group', 'users_scene', 'vertex_groups']

>>> bpy.data.objects['Cube'].name
'Cube'

>>> bpy.data.objects['Cube'].type
'MESH'

>>> bpy.data.objects['Cube'].location
Vector((0.0, 0.0, 0.0))

bpy.data.objects['Cube'].location.z = 5
>>> bpy.data.objects['Cube'].location.y = 5

{% endhighlight %}


### bpy.data.scenes and scene attributes
{% highlight pycon %}
>>> bpy.data.scenes
<bpy_collection[1], BlendDataScenes>

>>> bpy.data.scenes[0]
bpy.data.scenes['Scene']

>>> dir(bpy.data.scenes[0])
['__doc__', '__module__', '__slots__', 'active_clip', 'active_layer', 'animation_data', 'animation_data_clear', 'animation_data_create', 'audio_distance_model', 'audio_doppler_factor', 'audio_doppler_speed', 'audio_volume', 'background_set', 'bl_rna', 'camera', 'collada_export', 'copy', 'cursor_location', 'cycles', 'frame_current', 'frame_end', 'frame_preview_end', 'frame_preview_start', 'frame_set', 'frame_start', 'frame_step', 'frame_subframe', 'game_settings', 'gravity', 'grease_pencil', 'is_nla_tweakmode', 'is_updated', 'is_updated_data', 'keying_sets', 'keying_sets_all', 'layers', 'library', 'name', 'node_tree', 'object_bases', 'objects', 'orientations', 'render', 'rna_type', 'sequence_editor', 'statistics', 'sync_mode', 'tag', 'timeline_markers', 'tool_settings', 'unit_settings', 'update', 'update_tag', 'use_audio', 'use_audio_scrub', 'use_audio_sync', 'use_fake_user', 'use_frame_drop', 'use_gravity', 'use_nodes', 'use_preview_range', 'use_stamp_note', 'user_clear', 'users', 'world']
{% endhighlight %}

### bpy.context
Only access what the user has selected...
{% highlight pycon %}
>>> bpy.context.selected_objects
[bpy.data.objects['Cube']]
{% endhighlight %}


### bpy.ops
bpy.ops represents the operations that you can perform through the blender user interface.

Try apple + SPACE after typing in bpy.ops to see what can be operated on.

Try apple + SPACE after typing in bpy.ops.mesh to show what you can do with a mesh

{% highlight pycon %}
>>> bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
{'FINISHED'}

>>> bpy.ops.mesh.primitive_cube_add(location=(8,5,0))
{'FINISHED'}

>>> bpy.ops.mesh.primitive_cube_add(location=(5,0,0))
{'FINISHED'}

>>> bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 3))
{'FINISHED'}

{% endhighlight %}


### bpy.data.meshes.new and from_pydata
{% highlight pycon %}
>>> # create a list of faces - should be a list of lists, with each inner list representing the index of the element
>>> faces = [[1,2,3]]
>>> 
>>> triangle_mesh = bpy.data.meshes.new('triangle data')
>>> 
>>> triangle_mesh.from_pydata(verts, [], faces)
>>> 
>>> triangle_mesh.update()
>>> 
>>> triangle_obj = bpy.data.objects.new('triangle_obj', triangle_mesh)
>>> 
>>> bpy.context.scene .objects.link(triangle_obj)
{% endhighlight %}
{% highlight pycon %}
{% endhighlight %}

### Using the text editor
* Create a new text file

![Creating a text file](./resources/img/create-text.png)

* Turn on syntax highlighting, numbering and wrapping by activating three buttons on the lower right hand corner of the script window

![Editor Options](./resources/img/editor-options.png)
