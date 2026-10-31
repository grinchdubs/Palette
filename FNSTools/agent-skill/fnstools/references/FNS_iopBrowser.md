# iopBrowser

Package `FNS_iopBrowser`.

Browse the internal operators and the OP tree of the network you are in, from a popup opened off the pane bar. One browser instance serves every pane; the bar carries only the button.

- Category: Network
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-iopbrowser/

## What it does

- **Browse the iops in reach**: A button on the pane bar lists the iops available from the COMP you are in, those of every parent from the nearest up.
- **Drag or jump to an iop**: Drag any listed iop straight into the network editor, or use the list to navigate to it.
- **Find an operator in the OP tree**: The popup carries the network's OP tree with search, for finding an operator without leaving the pane.
- **Add an iop by drop**: Dropping an operator on the button makes it an internal operator shortcut of the network you are in, root included; CustomParTools, if installed, asks for the name.
- **Open from ParentHierarchy**: ParentHierarchy opens the browser for you when both are installed.
- **Share one browser across panes**: Each pane bar carries only the button, and every button calls the same browser.

## Reach it

`op.FNS_IOPBROWSER` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_NavbarRegistry`

## Parameters

None.
