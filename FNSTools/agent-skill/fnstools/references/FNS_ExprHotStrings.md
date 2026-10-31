# ExprHotStrings

Package `FNS_ExprHotStrings`.

Abbreviations that expand into TouchDesigner expressions as you type in a parameter field.

- Category: Parameters
- Version: 3.2.9
- Access: Free
- Docs: https://functionstore.tools/docs/fns-exprhotstrings/

## What it does

- **Abbreviation table**: A table of abbreviations and what they expand to, so `#AT` typed as an expression becomes `absTime.seconds`.
- **Inline expansion**: With Replace inline on, abbreviations also expand in the middle of an expression and can be combined, as in `#AT * 0.2`.
- **Externalize the table to a file**: With Externalize on, the table is kept in a file, so your abbreviations follow you from project to project.
- **Wrap a name in op()**: `#@noise1.par.amp` becomes `op('noise1').par.amp`.
- **Parent shortcut abbreviations**: `#!` becomes the closest parent shortcut, and `#!!` the same with `.par` after it.
- **Promote a parameter while typing**: `#@!` and `#@~` turn the parameter you are typing in into a custom parameter on its parent, linked by a bind or an expression.

## Reach it

`op.HOTSTRINGS` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `HotstringCheck(OP, PAR, EXPR, BINDEXPR, _depth=0)`: Expand a hotstring abbreviation found in a parameter's expression, or bind expression, into its full text; called when an expression changes.
- `OpenHotStrings()`: Open the expression hot-strings editor.

## Commands

- **Open hot-strings editor** (id `openhotstrings`): Open the expression hot-strings editor. Method `OpenHotStrings`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_HubRegistry`

## Parameters

### Custom

- **Replace inline** (`par.Replaceinline`, Toggle), default `off`: Expand an abbreviation anywhere inside an expression, not only when it is the whole expression. Off by default: with it on you can write '#AT * 0.2' and combine abbreviations.
- **CustomPar Promote Enable (#@! for binds, #!~ for refs)** (`par.Customparpromoteenable`, Toggle), default `on`: Enable the promote abbreviations: '#@!' binds a parameter to the parent and '#!~' references it. On by default.
- **Externalize** (`par.Sync`, Toggle), default `off`: Externalize the abbreviation table to a file on disk, so it can be edited outside TouchDesigner and version-controlled.
- **#@op Wrap Enable** (`par.Openable`, Toggle), default `off`: Enable the '#@' abbreviation, which wraps whatever follows in op('...'). '#@noise1.par.amp' becomes op('noise1').par.amp.
- **#! Parent Shortcut Enable** (`par.Parentshortcutenable`, Toggle), default `off`: Enable the '#!' abbreviations, which resolve to the closest parent shortcut ('#!' alone, or '#!!' with .par appended).
- **Edit Table** (`par.Open`, Pulse): Open the abbreviation table, where the first column is what you type and the second is what it expands to.
- **Author: Function Store @function.str** (`par.Author`, Header)
- **Usage:** (`par.Usage`, Header)
- **- add new lines to the table** (`par.L1`, Header)
- **- start abbreviation (first column) with a unique character** (`par.L2`, Header)
- **- it will expand to what you write in the second column** (`par.L3`, Header)
- **- type the abbreviation into a parameter's expression box** (`par.L4`, Header)
- **- and keep your mouse over it to expand!** (`par.L5`, Header)
- **- The contents of the table are saved across your projects if sync is enabled!** (`par.L6`, Header)
- **- If enabled #@ will wrap strings after it in op('...') in a smart way** (`par.L7`, Header)
- **- If enabled #! will resolve to the closest parent shortcut** (`par.L9`, Header)
- **-- and #!! will also add a .par after it** (`par.L10`, Header)
- **- If enabled #@! or #!~ will promote parameter as custom par** (`par.L11`, Header)
- **-- Can also directly write a custom name such as #@!Myfloat** (`par.L12`, Header)
- **- The definitions can be synced across projects if Externalized is enabled** (`par.L8`, Header)
