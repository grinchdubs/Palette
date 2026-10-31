# SeqMod

Watches a sequence of parameters on any COMP: name the target and the sequence, and the block parameters are published as one list, with a callback for every block added or removed.

- Category: Developer
- Version: 1.0.4
- Access: Base
- Docs: https://functionstore.tools/docs/seqmod/

## What it does

- **Follow a sequence's blocks**: Point it at a COMP and name the sequence, and the list of block parameters stays current as the sequence grows and shrinks.
- **Publish the block parameters**: Publishes the block parameters as name patterns in ParNames and as a table on out1, ready for a Parameter DAT, a UI builder or a script.
- **Add and remove callbacks**: Create Callbacks makes a DAT whose OnAddBlock and OnRemoveBlock hooks run once per block; errors are reported on SeqMod itself.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `seqMod` (Seq Mod) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/SeqMod.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `Comp` (property): The COMP whose sequence is modified (the Comp parameter).
- `Seq` (property): The target sequence on that COMP (Seqname), or None while either is unset.
- `SeqParNames` (attribute)

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

- **COMP** (`par.Comp`, COMP), default `..`: The COMP that owns the sequence, resolved like any OP parameter on SeqMod: a bare name ('geo1') is a sibling in the network SeqMod sits in, '..' is that network itself, and a child of SeqMod needs './name'.
- **Seq Name** (`par.Seqname`, Str): Name of the parameter sequence on the target COMP: the part before the block index (Items for Items0name, Items1name, ...). Empty publishes nothing.
- **ParNames** (`par.Parnames`, Str): Read-only. Every block parameter of the sequence as space-separated patterns (Items*name Items*level), republished whenever blocks are added or removed.

### Callbacks

- **Callbacks** (`par.Callbacks`, DAT): DAT holding OnAddBlock(seqBlock) and OnRemoveBlock(seqBlock_idx). A bare name is a sibling of SeqMod; a DAT inside it needs './name'. Defaults to the built-in no-op template; Create Callbacks makes an editable one.
- **Create Callbacks** (`par.Createcallbacks`, Pulse): Create an editable callbacks DAT from the template and point Callbacks at it.
