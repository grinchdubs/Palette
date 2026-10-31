# ExpressionPOP

Per-point attribute expressions for POPs: write lines like P = P + N * 0.1 and they compile to a GLSL compute shader, with local variables carried between lines. An alternative for the Math Combine POP.

- Category: 3D and Particles
- Version: 1.0.6
- Access: Free
- Docs: https://functionstore.tools/docs/expressionpop/

## What it does

- **Point math in plain lines**: Write one expression per line, such as `P = P + N * 0.1`, and read any point attribute of the input by its name.
- **GPU compute shader from your lines**: The lines compile into a GLSL compute shader on the GPU, so the math stays fast however many points come in.
- **Local variables**: Typed locals such as `vec3 offset = N * 0.2` carry over to every later line, so a long calculation splits into readable steps.
- **GLSL code and compile errors**: The viewer switches between the points, the generated GLSL and the compile result, and the code and the result also come out as DATs.
- **Replace a Math Combine POP**: Offered in place of a Math Combine POP, wired into the same spot, when you create one with the alternatives shortcut held.

## Reach it

No global shortcut. The installer never places it into a network: its tox is in the store at `<user palette>/FNSTools/store/ExpressionPOP.tox` for the user to place by hand, and its promoted methods are called on that copy.

## Promoted API

No promoted API: the package has no extension. Its parameters, listed below, are its surface.

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `mathcombinePOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Custom

- **Expr** (`par.Expr`, Sequence), default `0`: One block per expression line, run in order on every point.
- **Attribute Expression** (`par.Expr0expression`, Str): One line such as P = P + N * 0.1. The left side is an output attribute (or a local when OutAttr/Local is on); input attributes are read by name on the right.
- **OutAttr/Local** (`par.Expr0leftmode`, Toggle), default `off`: local needs type declaration like vec3 etc, but then are reusable in consequent blocks
- **Info** (`par.Info`, Str): Read-only: the compile result of the generated shader, so an error shows here.
- **Out Attrs** (`par.Outattrs`, Str): Read-only: the attributes the shader writes, collected from the left side of every line.
- **View** (`par.View`, Menu), default `pop`, menu `pop`, `code`, `info`: What the node's viewer shows: the output points, the generated GLSL code, or the compile info.
