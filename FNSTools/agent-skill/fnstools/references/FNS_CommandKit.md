# CommandKit

Package `FNS_CommandKit`.

Drop-in kit that lets ANY component publish quick-launch commands to the in-TouchDesigner command palette and the TDX launcher: decorate a promoted method, or declare a spec. Guarded: with no registry in the session nothing happens and nothing errors.

- Category: Developer
- Version: 3.2.6
- Access: Free
- Docs: https://functionstore.tools/docs/fns-commandkit/

## What it does

- **Publish commands from any component**: Drop the kit in as a direct child and the methods you mark appear in the CommandPalette and the TDXL launcher.
- **Safe without a registry**: With no command registry in the session nothing happens and nothing errors, so the component works the same for people without the palette.
- **Decorator for command methods**: The fns_command decorator derives label, help and prompted parameters from the method name, docstring and signature; Literal hints become menus.
- **Context, state and identity options**: Decorator extras set a context for greying out, a live state chip, surface, capability, hidden, and a canonical identity shared across packages.
- **Declare commands without imports**: Promote an FnsCommands() method that returns a spec list, with no imports at all: id, label, method, help, prompted params and every decorator extra as plain dict keys.
- **Announces on load**: Once the component declares a command the kit tags it and registers it, so a registry that arrives later still finds it; nothing to unregister.
- **Check that commands arrived**: Three reads tell you whether your commands are served, and a short ladder says what to look at when one is missing.
- **Announce again after changes**: Call Announce() to republish the component after its command set changes at runtime.
- **Tell placed copies apart**: Promote FnsInstance() and FnsToolName() so palettes distinguish multiple copies and favourites reach all of them (FNS_CommandRegistry 3.2.1 or newer).

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_CommandKit')`; its promoted methods are called on that COMP.

## Promoted API

- `Announce()`: Re-register the hosting tool's commands (after changing them).

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

None.
