# AutoRes

Package `FNS_AutoRes`.

Hold Alt while placing a generator TOP to have its resolution follow the project (or the panel it sits in).

- Category: Network
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-autores/

## What it does

- **Resolution that follows the project**: A generator TOP placed with `Alt` held gets a resolution expression that follows the `parent.Project` shortcut.
- **Panel size inside panels**: Inside a panel component, such as a Container COMP, the new TOP is set to Parent Panel Size.
- **Fallback size without a Project shortcut**: Where no `parent.Project` is found, the TOP uses the resolution you set on AutoRes.
- **Default colour format**: Sets the RGB mode and the Pixel Format of the new TOP too, where it has them.
- **Skip reloads and large batches**: Leaves operators from package reloads, replicators or loading components alone, and skips a batch too large to be a drop with a Textport note.

## Reach it

`op.AUTO_RES` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `SetRes(_op)`: Set a newly created generator TOP's resolution to the tool's choice while the modifier is held; called for each new operator.
- `ToggleActive()`: Enable or disable AutoRes.

## Commands

- **Toggle AutoRes** (id `toggleactive`): Enable or disable AutoRes. Method `ToggleActive`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `on`: Turn AutoRes on or off. When on, dropping a generator TOP with the modifier held sets its Output Resolution to follow the project instead of the 1280x720 default. Off leaves the component installed but idle.
- **Resolution** (`par.Resolution`, WH x2), default `1920.0`: The fallback resolution written into the dropped TOP's Custom Resolution. It is only reached when the network has no parent.Project shortcut to follow. With one, the TOP tracks that instead.
- **RGB** (`par.Rgb`, Menu), default `add`, menu `noise`, `multiply`, `add`, `subtract`: The RGB mode written onto generator TOPs that have one (the Noise TOP).
- **Pixel Format** (`par.Format`, Menu), default `useinput`, menu `useinput`, `rgba8fixed`, `srgba8fixed`, `rgba16float`, `rgba32float`, `_separator_`, `rgb10a2fixed`, `rgba16fixed`, `rgba11float`, `rgb16float`, `rgb32float`, `mono8fixed`, `mono16fixed`, `mono16float`, `mono32float`, `rg8fixed`, `rg16fixed`, `rg16float`, `rg32float`, `a8fixed`, `a16fixed`, `a16float`, `a32float`, `monoalpha8fixed`, `monoalpha16fixed`, `monoalpha16float`, `monoalpha32float`: The Pixel Format written onto the dropped TOP. 'Use Input' leaves TouchDesigner's own default alone.
- **Keys** (`par.Keys`, Str): The modifier keys held to trigger this gesture, space-separated (TouchDesigner key names). The default is an expression that picks the right keys per platform. Typing a plain value over it pins the tool to one OS.
