# LinkOPs

Links the parameters of several operators so a change on one lands on all of them, with exceptions by operator and by parameter, an automatic mode and a one-shot sync.

- Category: Parameters
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/linkops/

## What it does

- **Link operators by pattern**: Name the operators with patterns such as `noise*` or `level1 level2`, and a parameter changed on one is written to the others.
- **Link expressions and modes**: Values follow, and by default so do expressions and parameter modes.
- **Exclude operators and parameters**: Leave out operators that match the pattern anyway, and parameters such as `t? seed` to keep transforms and seeds independent.
- **Constant-only linking**: Link only parameters in constant mode on both sides, so an expression on one operator is never overwritten.
- **Auto-update the operator list**: With Auto on, the list follows operators as they are added, renamed or removed.
- **Sync on demand**: Operators added later join when you press Sync.
- **Match parameters by name across types**: Operators of different types can share a link; the parameters they have in common by name are kept in step.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `linkOPs` (Link OPs) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/LinkOPs.tox`. Its promoted methods are called on the placed copy.

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

- **Active** (`par.Active`, Toggle), default `on`: Master switch. When off, parameter changes are no longer propagated between the linked operators.
- **OPs** (`par.Ops`, Str): Space-separated operator name patterns (wildcards allowed, e.g. noise* level1) to link, searched in the network LinkOPs sits in.
- **Except** (`par.Except`, Str): Space-separated operator name patterns to leave out of the link even when they match Ops.
- **Par Except** (`par.Parexcept`, Str): Space-separated parameter name patterns (e.g. t? seed) that are never propagated.
- **Auto** (`par.Auto`, Toggle), default `off`: Keep the list of linked operators up to date automatically as operators are added, renamed or removed.
- **Sync** (`par.Sync`, Pulse): Rescan the network for operators matching Ops now. Use this when Auto is off.
- **Constant Only** (`par.Constantonly`, Toggle), default `off`: Only propagate between parameters that are in constant mode on both sides; expressions, exports and binds are left alone.
