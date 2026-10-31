# Hub

Package `FNS_Hub`.

The FNS button in TouchDesigner's main-menu bar and the one-stop manager window behind it: the Toolbar, Navbar and Main Menu configurators as tabs, the console, and any tab a tool contributes. Drop a panel COMP on the button to register it into a surface.

- Category: Core
- Version: 3.2.16
- Access: Free
- Docs: https://functionstore.tools/docs/fns-hub/

## What it does

- **Open the hub**: Left-click the FNS button in the main-menu bar, or run Open FNS Hub from quick-launch, and the hub opens on the tab you were last on.
- **Jump to any tab from the FNS button**: Right-click the FNS button to jump to any tab or console page, bring a hidden tab back, switch Perform Mode, or open the docs.
- **Toolbar configurator**: Reorder, group, hide and show the widgets on TouchDesigner's bookmark bar, and add dividers between them.
- **Navbar configurator**: Reorder pane-bar items, flip them between the left and right side, and show, hide or group them.
- **Main menu configurator**: Arrange the main-menu bar with TouchDesigner's own items included, so your entries can sit between them.
- **Reorder OP Create contributions**: Reorder what tools add to the OP Create dialog, or switch a contribution off without uninstalling its tool.
- **Network overlay layout**: Reorder, show and hide what tools draw on the network editor, and move each corner list to another corner.
- **Console tab**: The toolkit's web console renders inside the hub, and its browser runs only while the tab is shown.
- **Commands tab**: Lists every command the command registry serves, hidden and built-in ones included, to star or hide.
- **Tool tabs**: The larger tool UIs, such as the OSC and MIDI mappers, sit in the same window, exactly the ones you have installed.
- **Arrange and hide tabs**: Drag tabs into your order, hide one from its tool's Shown in Hub parameter, and pick a wrapping or single-row tab bar; the layout roams with your settings.
- **Perform Mode**: Stops the tools that only serve the network editor for a show, turns the FNS button red, and brings everything back as it was. Follows TouchDesigner's Perform Mode by default.
- **Drop to register**: Drop a panel COMP on the FNS button, pick a surface, and it gets a self-registering host and appears there at once.
- **Open a tab from Python**: `op.FNS_HUBREGISTRY.Open(tab='navbar')` opens the hub on a tab by its canonical name, contributed tabs included.
- **Contribute a tab**: A tool carrying a stamped FNS_HubRegistry host gets a tab showing itself, an inner panel, an operator in an OP Viewer, or a parameter page.

## Reach it

No global shortcut. A child of the toolkit root, reached as `op.FNS.op('FNS_Hub')`; its promoted methods are called on that COMP.

## Promoted API

- `AcceptsDrop(items)`: Whether any of the dragged items is a panel COMP the Hub can show as a tab.
- `Close()`: Close the Hub window and un-expose every tab.
- `HiddenTabs()`: Registered tabs currently hidden (the right-click menu offers them back).
- `OnActivetabChanged(name)`: The Active Tab par changed from outside (a roamed value landing after boot, or a script) -- follow it.
- `OnParChange(name, value)`: Called by the parameter execute when Activetab or Tabbar changes.
- `OnPulse(name)`: Called by the parameter execute for the Open and Refreshtabs pulses.
- `OnTabReorder(fromIndex, toIndex)`: Move a tab on the bar: the order persists on Tab User Order.
- `OnTabSelected(name)`: A tab on the bar was clicked (tabbar/tabs_exec).
- `Open(tab=None)`: Open the window; `tab` = a canonical name to switch to (a hidden tab is shown again first).
- `OpenHub()`: Open the FNS Hub window: every registry's configurator, the console, and any tab a tool contributes.
- `OpenMainMenuConfigurator()`: Open FNS Hub on the Main Menu tab (the configurator lives in the hub).
- `OpenMenu()`: Right-click on the FNS button: jump straight to a tab, to one of the console's pages, toggle FNSTools Perform Mode, or go to the documentation, the website or the Patreon join page.
- `OpenTabParameters(index)`: The owning tool's parameter window (the mappers are configured there), from a tab's right-click menu.
- `PerformOn()`: State chip for TogglePerform: the toolkit root's Perform Mode (docs/PerformMode.md).
- `RefreshTabs()`: Rebuild the folder-tab bar from the registry and show the active tab.
- `RouteDrop(items)`: Drop entry point (drop_callbacks).
- `ShowTab(name, displayed=True)`: Show or hide a Hub tab by canonical name; the choice roams with the layout.
- `Tabs()`: The shown tabs, in bar order (dicts from FNS_HubRegistry.Tabs).
- `TogglePerform()`: Toggle FNSTools Perform Mode: the tools that only serve the network editor stop, and come back as they were.

## Commands

- **Open FNS Hub** (id `openhub`): Open the FNS Hub window: every registry's configurator, the console, and any tab a tool contributes. Method `OpenHub`.
- **Open main-menu configurator** (id `openmainmenuconfigurator`): Open FNS Hub on the Main Menu tab (the configurator lives in the hub). Method `OpenMainMenuConfigurator`.
- **Toggle FNSTools perform mode** (id `toggleperform`): Toggle FNSTools Perform Mode: the tools that only serve the network editor stop, and come back as they were. Method `TogglePerform`.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Hub

- **Open Hub** (`par.Open`, Pulse): Open the FNS Hub window, the toolkit's one-stop manager: every registry's configurator, the console, and any tab a tool contributes.
- **Tab Bar** (`par.Tabbar`, Menu), default `rows`, menu `rows`, `strip`: How the hub's tab bar lays out. Rows: fixed-width tabs that wrap into as many rows as needed. Strip: TouchDesigner's folder-tabs widget: one row with scroll arrows and a dropdown, and drag-to-reorder. Neither has close buttons: hide a tab from its tool's Registry page, bring it back from the right-click menu.
- **Active Tab** (`par.Activetab`, Str): Canonical name of the tab currently shown. Written by the tab bar; roams with the config registry so the hub reopens where you left it.
- **Tab User Order** (`par.Tabuserorder`, Str): Space-separated canonical names in the order you dragged the tabs into. Tabs not listed follow in their registered order. Roams with the config registry.
- **Refresh Tabs** (`par.Refreshtabs`, Pulse): Re-read the hub registry and rebuild the tab bar. Normally automatic; use after a manual edit inside the tabs container.
