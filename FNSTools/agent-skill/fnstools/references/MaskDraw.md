# MaskDraw

Draw a mask with the mouse straight onto the image: a panel you paint in, with the mask and the masked image as outputs, a lock and a reset.

- Category: Visual
- Version: 1.0.6
- Access: Pro
- Docs: https://functionstore.tools/docs/maskdraw/

## What it does

- **Paint and erase on the image**: Paint on the input image with the left button and erase with the right; the panel follows the input's aspect.
- **Output the mask and the masked image**: Outputs the drawn mask and the input inside the painted area, to key a composite, drive a Level or mark a projection surface.
- **Reset the mask**: Middle-click in the panel clears the mask, and so does Reset, which keeps it clear while it is on.
- **Show or hide the button bar**: Ctrl and middle-click shows or hides the button bar, and Show Input, Show Mask and Show Brush choose what the panel draws.
- **Lock a finished mask**: Lock keeps a finished mask from being changed by a stray click or reset.
- **Pause drawing**: Switching Active off hides the brush and ignores the mouse, and the mask stays as it is.
- **Save the mask with the project**: Optionally bakes the mask into the component on every save, so it is back when the project reopens.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `maskDraw` (Mask Draw) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/MaskDraw.tox`. Its promoted methods are called on the placed copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Custom

- **Active** (`par.Active`, Toggle), default `off`: Enables drawing. Off hides the brush and ignores the mouse; the painted mask is kept.
- **Radius** (`par.Radius`, Float), default `0.1`: The brush radius, relative to the size of the mask.
- **Show Input** (`par.Showinput`, Toggle), default `off`: Shows the input image in the display panel behind the mask. Off shows the input only inside the painted area.
- **Show Mask** (`par.Showmask`, Toggle), default `off`: Draws the painted mask (white) over the image in the display panel.
- **Show Brush** (`par.Debug`, Toggle), default `off`: Shows the brush outline (red) under the pointer in the display panel.
- **Display UI** (`par.Display`, Toggle), default `on`: Shows the button bar in the display panel. Ctrl + middle-click in the panel toggles it.
- **Reset** (`par.Reset`, Toggle), default `off`: While on, clears the painted mask. A middle-click in the panel does the same. Ignored while Lock is on.
- **Lock** (`par.Lock`, Toggle), default `off`: Freezes the painted mask: new strokes, erasing and Reset are ignored until it is turned off. The mask lives in a feedback loop, so it is not saved with the file.
- **Save Mask With Project** (`par.Savemask`, Toggle), default `off`: On: the current mask is baked into the component on every project save (and by Bake Mask Now), so it is restored when the project is reopened. Off (default): the mask lives only in the session and nothing is written into the file.
- **Bake Mask Now** (`par.Bakemask`, Pulse): Capture the current mask into the component now, without waiting for a project save. Only with Save Mask With Project on.
