# midiMapper

Map MIDI controls to parameters, with a learn mode you drive by dropping a parameter on the toolbar button. Mappings are saved into the project folder by design; the tool's own settings roam through config.

- Category: Control & mapping
- Version: 3.2.10
- Access: Free
- Docs: https://functionstore.tools/docs/midimapper/

## What it does

- **Drag-and-drop MIDI learn**: Drop parameters onto the mapper, switch on Learn and move a fader or knob to assign it.
- **Range per mapping**: Each mapping has its own min and max, so a full fader sweep can cover just part of a parameter.
- **Learn from the toolbar**: Drop a parameter on the toolbar button and move a knob to map it, without opening the mapper.
- **Open the mapper from the toolbar**: Click the toolbar button to open the MIDI Mapper, or right-click it for the mapper's settings.
- **Settings across projects**: The tool's settings follow you across projects through ConfigRegistry, while the mappings stay with the project.
- **Reset a stuck MIDI device**: ResetMIDIPls bypasses and un-bypasses MIDI operators to unstick them, for one device or all of them.
- **Reset all from the toolbar**: Middle-click the midiMapper toolbar button to reset all MIDI operators.
- **Auto-reset on startup**: Can reset all MIDI operators automatically on startup.

## Reach it

`op.FNS_MULTIMIDI` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `AddParameter(parameter, channel='Learn', index='Learn')`: Add a parameter row to the mapping table, with its range and a channel and index to learn.
- `AdjustValue(row, col, val)`: Write one cell of the mapping table.
- `ApplyMapping(channel, index, value)`: Called for an incoming MIDI message: write the mapped parameters, 0..127 remapped into each one's range.
- `ClearMapping()`: Forget the in-memory mapping.
- `ClearTable()`: Clear the mapping table, header kept, and the mapping.
- `Delete(row)`: Delete a row of the mapping table.
- `FillMapping()`: Rebuild the in-memory mapping from the table rows.
- `Learn(channel, index)`: While Learn is on, assign the incoming channel and index to every row waiting to learn.
- `Mapping` (attribute)
- `SetLearn(row)`: Set a row's channel and index back to Learn.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Device ID** (`par.Id`, Int), default `1`: Which MIDI device the Reset button acts on. Middle-clicking the toolbar button resets every device instead.
- **Clear** (`par.Clear`, Pulse): Delete every mapping in the table below.
- **Learn** (`par.Learn`, Toggle), default `off`: Listen for the next incoming MIDI message and assign it to the parameter you dropped on the UI. Turn it off when you are done assigning.
- **Edit Midimap DAT** (`par.Edit`, Pulse): Open the midimap table, where each row is one mapping and its min/max range.
- **Reset All Midi** (`par.Resetall`, Pulse): Bypass and un-bypass every MIDI operator to unstick a device that has stopped responding.
- **Reset Delay (Ms)** (`par.Resetdelayms`, Float), default `0.0`: How long to leave the MIDI operators bypassed during a reset, in milliseconds. Raise it if a device needs longer to let go of the port.

### Repositorie

- **Mappingtable** (`par.Mappingtablerepositorie`, OP): The table DAT holding the mappings. Point it at another table to keep mappings somewhere else, in a shared component for instance.
- **Create** (`par.Mappingtablecreate`, Pulse): Create a mapping table and point the parameter above at it.
