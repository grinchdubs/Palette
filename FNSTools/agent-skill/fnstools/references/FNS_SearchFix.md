# SearchFix

Package `FNS_SearchFix`.

Makes the network editor's find bar find things: any part of a name, case-insensitive, with wildcards, optionally fuzzy and inside child networks. Keeps the bar's arrows and Home toggle; a Legacy toggle brings TouchDesigner's own search back.

- Category: Network
- Version: 0.2.8
- Access: Free
- Docs: https://functionstore.tools/docs/fns-searchfix/

## What it does

- **Find any part of a name**: Finds operators by any part of their name in any case; typed spaces become underscores, and a text split into parts needs every part to match.
- **Wildcard patterns**: Patterns like `noise*`, `*out?` and `[ab]lur*` match whole names as in TouchDesigner's pattern fields, and a leading `^` inverts the match.
- **Fuzzy matching**: When switched on, also finds word initials, a typo or two, or the letters in order, listed after every plain hit.
- **Rank the best results first**: Exact names rank first, then names starting with the text, then word matches, then anywhere, with shallower operators before deeper ones.
- **Step through results**: The arrows step through results, the first is picked as you type, and with Home on the pane centres on the picked operator.
- **Deep search into child networks**: A Deep checkbox and depth field in each pane's bar search the networks inside the current one; picking a hit takes the pane into its network.
- **Restore TouchDesigner's own search**: A Legacy checkbox in the find bar brings back TouchDesigner's own search for every pane, and switching SearchFix off restores every bar as it was.
- **Close the bar from inside it**: The find bar shortcut also closes the bar while you are typing in it.

## Reach it

`op.FNS_SEARCHFIX` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `FillResults(scriptOp: 'scriptDAT')`: The script_results cook: one row per hit, its path relative to the search root.
- `PatchAll()`: Patch every find bar there is, or unpatch them all when Active is off.
- `Pick(fb: 'COMP', index: 'int')`: Make result `index` current and selected, entering its network if needed, and home on it when the bar's Home toggle is on.
- `RepatchFindBars()`: Apply the search to every find bar again, for example after TouchDesigner rebuilt one.
- `Search(root: 'COMP', text: 'str', legacy: 'bool' = False, fuzzy: 'bool' = False, depth: 'int' = 1, limit: 'int' = 500)`: Paths of the operators matching `text`, relative to `root`, best first.
- `Step(fb: 'COMP', delta: 'int')`: Back (-1) or forward (+1) through the results.
- `ToggleActive()`: Switch the Python find-bar search on or off; off is TouchDesigner's own find bar.
- `ToggleFuzzy()`: Also match loosely in the find bar: first letters of words, a typo or two.
- `ToggleLegacy()`: Search like TouchDesigner's own find bar: names that start with the text, case-sensitive.

## Commands

- **Repatch find bars** (id `repatchfindbars`): Apply the search to every find bar again, for example after TouchDesigner rebuilt one. Method `RepatchFindBars`.
- **Toggle SearchFix** (id `toggleactive`): Switch the Python find-bar search on or off; off is TouchDesigner's own find bar. Method `ToggleActive`.
- **Toggle fuzzy find** (id `togglefuzzy`): Also match loosely in the find bar: first letters of words, a typo or two. Method `ToggleFuzzy`.
- **Toggle legacy find** (id `togglelegacy`): Search like TouchDesigner's own find bar: names that start with the text, case-sensitive. Method `ToggleLegacy`.

## Hotkeys

- `ctrl.f` (`Findbarshortcut` on `FNS_SearchFix`)

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_PaneSearchRegistry`

## Parameters

### SearchFix

- **Active** (`par.Active`, Toggle), default `on`: Patch every network editor find bar with the Python search. Off: every find bar is exactly as TouchDesigner made it.
- **Legacy Search** (`par.Legacy`, Toggle), default `off`: TouchDesigner's own search: names that start with the text, case-sensitive, in the current network only. Also a toggle in each find bar.
- **Fuzzy** (`par.Fuzzy`, Toggle), default `off`: Also match loosely: the first letters of words (sschg), one or two typos (nosie), or the letters in order. Ranked below every exact, prefix, word and substring hit. Also a toggle in each find bar.
- **Deep Depth** (`par.Depth`, Int), default `3`: Where a find bar's depth field starts when its Deep toggle is first switched on. Counted like findChildren's limit: 1 is the current network only, 2 adds the networks inside it, and so on. Each pane's bar keeps its own.
- **Max Results** (`par.Maxresults`, Int), default `500`: The most results kept per search, best first. The search runs on every keystroke, so this bounds its cost on large networks.
- **Shortcut Closes Find Bar** (`par.Togglefindbar`, Toggle), default `on`: TouchDesigner's find bar shortcut does nothing while you type in the bar. On: the shortcut closes the bar from there too, with the bar's own close button. Off: TouchDesigner's behaviour.
- **Find Bar Shortcut** (`par.Findbarshortcut`, Str): TouchDesigner's own find bar shortcut, which this listens for to close an open bar. It cannot move TouchDesigner's shortcut, so change it only if TouchDesigner's has changed.
- **Repatch Find Bars** (`par.Repatch`, Pulse): Apply the patch to every find bar again, for example after TouchDesigner rebuilt its UI.
