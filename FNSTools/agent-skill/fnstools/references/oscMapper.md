# oscMapper

Map OSC messages to parameters. Mappings are saved into the project folder by design.

- Category: Control & mapping
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/oscmapper/

## What it does

- **Learn-based OSC mapping**: Drag parameters onto the mapper, switch on Learn and move a fader or knob to assign it.
- **Mapping range**: Set the min/max range a mapped control drives.
- **Send values back to the controller**: Talkback sends values back out over OSC as they change, so a controller with motorised faders or LEDs can follow TouchDesigner.
- **Listen and send per project**: A new copy neither listens nor sends until you switch it on, and that choice stays with the project.

## Reach it

`op.AMB_OSC_MAPPER` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `AddParameter(parameter, channel='Learn', index='Learn')`: Add a parameter row to the mapping table, with its range and an address to learn.
- `AdjustValue(row, col, val)`: Write one cell of the mapping table.
- `ApplyMapping(channel, value)`: Called for an incoming OSC message: write the mapped parameters, 0..1 remapped into each one's range.
- `ChannelMap` (attribute)
- `ClearMapping()`: Forget the in-memory mapping.
- `ClearTable()`: Clear the mapping table, header kept, and the mapping.
- `Delete(row)`: Delete a row of the mapping table.
- `FillMapping()`: Rebuild the in-memory mapping from the table rows.
- `Learn(channel)`: While Learn is on, assign the incoming address to every row waiting to learn.
- `Mapping` (attribute)
- `ReturnMapping(parameter)`: Send a parameter's value back out over OSC on its mapped address, normalised to 0..1.
- `SetLearn(row)`: Set a row's address back to Learn.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`

## Parameters

### Custom

- **Clear** (`par.Clear`, Pulse): Delete every mapping in the table below.
- **Learn** (`par.Learn`, Toggle), default `off`: Listen for the next incoming OSC message and assign it to the parameter you dropped on the UI. Turn it off when you are done assigning.
- **Edit DAT** (`par.Edit`, Pulse): Open the mapping table, where each row is one mapping and its min/max range.
- **Active** (`par.Active`, Toggle), default `off`: Receive OSC. Off closes the listening port and leaves the mappings untouched.
- **Protocol** (`par.Protocol`, Menu), default `msging`, menu `msging`, `multicastmsging`, `reliablemsging`: The OSC transport to listen on. Messaging is the ordinary one; multicast receives from a group address, and reliable adds delivery guarantees at the cost of latency. It must match what the sender uses.
- **Port** (`par.Port`, Int), default `7000`: The UDP port to receive OSC on. It must match the port the sender transmits to.
- **OSC Address Scope** (`par.Addscope`, Str), default `*`: Which OSC addresses to accept, as a pattern. '*' takes everything. Narrow it when several tools share one port.
- **Local Address** (`par.Localaddress`, StrMenu), menu read from the computer it runs on: Which network interface to listen on. Empty means all of them; set it on a machine with several network cards.
- **Talkback Active** (`par.Active2`, Toggle), default `off`: Send values back out over OSC as they change, so a controller with motorised faders or LEDs can follow TouchDesigner.
- **Network Address** (`par.Address`, Str), default `localhost`: The host talkback is sent to. 127.0.0.1 stays on this machine; use the controller's IP to reach it over the network.
- **Local Address** (`par.Localaddress2`, StrMenu), default `*`, menu read from the computer it runs on: Which network interface talkback is sent from. '*' lets the OS choose.
- **Port** (`par.Port2`, Int), default `7000`: The UDP port talkback is sent to. It must match the port the receiving device listens on, and is normally not the port above.

### Repositorie

- **Mappingtable** (`par.Mappingtablerepositorie`, OP): The table DAT holding the mappings. Point it at another table to keep mappings somewhere else, in a shared component for instance.
- **Create** (`par.Mappingtablecreate`, Pulse): Create a mapping table and point the parameter above at it.
