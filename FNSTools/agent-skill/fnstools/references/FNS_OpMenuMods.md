# OpMenuMods

Package `FNS_OpMenuMods`.

OP Create dialog extras: IO filter buttons, your own search keywords per operator type, and acronym search (type m f o for Movie File Out).

- Category: Interface
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-opmenumods/

## What it does

- **Filter IO operators**: Buttons at the top right of the OP Create dialog show only IO operators, hide them, or show everything.
- **Custom search keywords**: Give any operator type your own search words, so typing music finds Audio File In and webcam finds Video Device In.
- **Keyword table in Hub**: The keywords live in one table, edited from the SearchWords tab of Hub and synced across project files.
- **Acronym search**: Type the start of each word of an operator's name, such as m f o, to find Movie File Out.
- **Remove cleanly, shared with other tools**: The mods apply through OpMenuRegistry, so several tools can decorate the dialog together and it returns to stock when they are removed.

## Reach it

`op.FNS_OPMOD` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `ResyncOpMenu()`: Re-collect the op-menu contributions from all tools.

## Commands

- **Resync op menu** (id `resyncopmenu`): Re-collect the op-menu contributions from all tools. Method `ResyncOpMenu`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`
- `FNS_OpMenuRegistry`

## Parameters

### IO Filter

- **IO Filter Active** (`par.Iofilteractive`, Toggle), default `on`: Add Greg Hermanovic's IO filter buttons to the top right of the OP Create dialog: IO shows only operators that talk to something outside TouchDesigner, -IO hides them, All is the default.
