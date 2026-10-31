# ConstantCHOP

A Constant CHOP with typed values: numbers, toggles, tuples, text, paths or operator references, each promoted as a property you can read and set from Python, and a snap from its input. An alternative for the Constant CHOP.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/constantchop/

## What it does

- **Typed constants**: Every constant can be a float, integer, toggle, four-value tuple, string, file or folder path, or operator reference.
- **Channels plus a table**: Numbers, toggles and tuples come out as CHOP channels, and every constant also comes out as a DAT table of names and values.
- **Switch type without losing values**: Changing the type keeps each value wherever it converts.
- **Snap from the input**: Snap Input turns whatever is wired in into constants, one per channel, named and valued from it.
- **Replace a Constant CHOP**: Create a Constant CHOP with the alternatives shortcut held and ConstantCHOP is offered in its place.
- **Constants as properties**: Each constant is a property that reads and sets it, a _out property reads the output, and a prefix avoids clashes.

## Reach it

No global shortcut. The installer never places it into a network: its tox is in the store at `<user palette>/FNSTools/store/ConstantCHOP.tox` for the user to place by hand, and its promoted methods are called on that copy.

## Promoted API

- `Chan1` (property): The Value parameter of the block named 'chan1'; assign to set it.
- `Chan1_out` (property): The output of the block named 'chan1': the channel value for a number, else the table cell.
- `CompEditorExt` (attribute)
- `ConsumeParGroup(size: int, previous_size: int)`: Grow the sequence's block size to hold a multi-value Value parameter group of `size` components.
- `IsParGroup` (property): Returns whether the current parameter is a parameter group
- `OnAdd(block_idx: int, prev_name: str = None)`: Create, or rename, the promoted attribute pair of one block; called when a block is added or its Name changes.
- `OnPrefixChanged(old_prefix: str)`: Rebuild the promoted per-block attributes after the Prefix parameter changed from old_prefix.
- `OnTypeChanged(new_type: str)`: Rebuild every block's Value parameter in the new style (Float, Int, RGB, ...); called when the Type parameter changes.
- `OnValChanged(block_idx, _val)`: Called when a block's Value parameter changes; currently a no-op, the dependency update is disabled.
- `ParGroupChannels` (property): Returns a list of channel names for the parameter group, or an empty list if not a parameter group
- `ParGroupSize` (property): Returns the size of the parameter group, or 1 if not a parameter group
- `RefreshAllAttributes(old_prefix: str = None)`: Remove every promoted per-block attribute and create them again from the current blocks (when Promote is on).
- `SeqConst` (property): The sequence of constant blocks this tool manages (the Seqname sequence on the owner).

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `constantCHOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Constant

- **Type** (`par.Type`, Menu), default `Float`, menu `Float`, `Int`, `Toggle`, `Momentary`, `XYZW`, `RGBA`, `UVW`, `WH`, `Str`, `StrMenu`, `File`, `FileSave`, `Folder`, `Python`, `Object`, `OP`, `COMP`, `PanelCOMP`, `TOP`, `TOPMulti`, `CHOP`, `SOP`, `POP`, `MAT`, `DAT`: The kind of value every constant holds. Numbers, toggles and tuples come out of the CHOP output; text, paths and operator references come out of the DAT output. Switching keeps each value where it converts.
- **Constant** (`par.Constant`, Sequence), default `0`: One block per constant: add or remove blocks here.
- **Name** (`par.Constant0name`, Str): The channel name, and the property name when Promote to Property is on.
- **Value** (`par.Constant0value`, Float), default `0.0`: The constant's value.

### Common

- **Snap Input** (`par.Snapinput`, Pulse): Replace the constants with the channels wired into the input: one block per channel, named and valued from it. Float and Int only.
- **Promote to Property** (`par.Promote`, Toggle), default `on`: Expose each constant as a property on this COMP, so op(...).Name reads and sets its value and Name_out reads the output.
- **To get/set values as .{prefix}{name}** (`par.Header`, Header)
- **Property Prefix** (`par.Prefix`, Str), default `C_`: Put in front of every property name, to keep them clear of other names on the COMP.
- **Author: Function Store (@function.str)** (`par.Author`, Header)
