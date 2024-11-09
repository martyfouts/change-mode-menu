# Deprecated
This repository is now deprecated. The examples apply to Blender versions 3.x. It has not been tested on newer versions of Blender.

This Blender Add-on is a replacement for the CTRL-TAB mode change menu in the
3D Viewport.  It is invoked by CTRL-W (can be changed in preferences keymap).

The entire addon is in __init__.py.

# Operators
## `TLA_OT_changemode`

Trivial operator that changes the active object's mode if it is different
than the desired new mode

## `TLA_OT_invokemenu`

Trivial operator that invokes the menu that contains the buttons to invoke
the change mode operator with different arguments.

# Menu

# `TLA_MT_changemode`

The menu with entries for the modes.  This tries to be a "smart" menu
and only presents legitimate modes for the active object.  It probably
has some unintended omissions.

# Usage

Type CTRL-W and select a new mode from the popup menu

#  Shortcut

To change the shortcut key, edit preferences and in the Keymap tab make sure that
search mode is set to 'Name'.  The easiest way to find the keymap entry is
to type 'tla' and look for "Change Mode Menu".  Open it and set the
shortcut to whatever you want.
