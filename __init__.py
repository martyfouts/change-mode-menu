# Copyright 2022 Martin Fouts
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# 

# Very small add on to start from

bl_info = {
    "name" : "Mode switch menu",
    "description" : "A menu for switching modes in the 3D viewport",
    "author" : "Marty",
    "version" : (0, 0, 1),
    "blender" : (2, 80, 0),
    "location" : "View3D",
    "warning" : "",
    "support" : "COMMUNITY",
    "doc_url" : "",
    "category" : "3D View"
}

import bpy
from bpy.types import Operator
from bpy.types import Menu
from bpy.props import StringProperty

class TLA_OT_changemode(Operator):
    """ Change the mode of an object """
    bl_idname = "tla.changemode"
    bl_label = "Change the 3D viewport mode"
    bl_options = {"REGISTER", "UNDO"}

    new_mode : StringProperty(name="new mode", description="Mode to change to", default="None")

    @classmethod
    def poll(cls, context):
        return True #context.active_object != None

    def execute(self, context):
        if context.object.mode != self.new_mode:
            bpy.ops.object.mode_set(mode = self.new_mode)
        return {'FINISHED'}


class TLA_OT_invokemenu(Operator):
    bl_idname = "tla.invokemenu"
    bl_label = "Change Mode Menu"
    
    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def execute(self, context):
        bpy.ops.wm.call_menu(name="TLA_MT_changemode")
        return {'FINISHED'}

class TLA_MT_changemode(Menu):
    """Change Mode menu for View_3d"""
    bl_label = "MODE"
    bl_idname = "TLA_MT_changemode"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TLA"

    def draw(self, context):
        object = context.active_object
        if not object:
            return
        self.layout.operator("tla.changemode", text="Object").new_mode='OBJECT'
        if object.type == 'ARMATURE':
            self.layout.operator("tla.changemode", text="Edit").new_mode='EDIT'
            self.layout.operator("tla.changemode", text="Pose").new_mode='POSE'
        elif object.type == 'MESH':
            self.layout.operator("tla.changemode", text="Edit").new_mode='EDIT'
            self.layout.operator("tla.changemode", text="Sculpt").new_mode='SCULPT'
            self.layout.operator("tla.changemode", text="Vertex Paint").new_mode='VERTEX_PAINT'
            self.layout.operator("tla.changemode", text="Weight Paint").new_mode='WEIGHT_PAINT'
            self.layout.operator("tla.changemode", text="Texture Paint").new_mode='TEXTURE_PAINT'
        elif object.type in {'CURVE', 'SURFACE', 'META', 'FONT'}:
            self.layout.operator("tla.changemode", text="Edit").new_mode='EDIT'
        elif object.type == 'GPENCIL':
            self.layout.operator("tla.changemode", text="Edit").new_mode='EDIT_GPENCIL'
            self.layout.operator("tla.changemode", text="Sculpt").new_mode='SCULPT_GPENCIL'
            self.layout.operator("tla.changemode", text="Paint").new_mode='PAINT_GPENCIL'
            self.layout.operator("tla.changemode", text="Weight Paint").new_mode='WEIGHT_GPENCIL'
            self.layout.operator("tla.changemode", text="Vertex Paint").new_mode='VERTEX_GPENCIL'
        elif object.type == 'LATTICE':
            self.layout.operator("tla.changemode", text="Edit").new_mode='EDIT'
            self.layout.operator("tla.changemode", text="Weight Paint").new_mode='WEIGHT_PAINT'

 
classes = [
    TLA_OT_changemode,
    TLA_OT_invokemenu,
    TLA_MT_changemode,
]

def register():
    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(
        name='3D View', 
        space_type='VIEW_3D'
    )
    item = keymap.keymap_items.new(
        "tla.invokemenu",
        type='W',
        value='PRESS',
        ctrl=True,
    )
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(
        name='3D View', 
        space_type='VIEW_3D'
    )
    for item in keymap.keymap_items:
        if item.idname == 'kmap.keyhit':
            keymap.keymap_items.remove(item)


if __name__ == '__main__':
    register()
    bpy.ops.wm.call_menu(name="TLA_MT_changemode")