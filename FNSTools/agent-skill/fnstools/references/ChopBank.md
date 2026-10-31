# ChopBank

A bank of channel processors: one block per channel, each with its own range, exponent curve, zero-below, lag and speed mode, built from the input with one Snap Input, with gain before and after and every block promoted as a property. An alternative for the Math CHOP and the Constant CHOP.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/chopbank/

## What it does

- **Shape each channel with its own block**: Each block shapes one channel with its own range remap, exponent curve, Zero Below, lag, and a speed mode that turns it into a running total.
- **Build the bank with Snap Input**: One press makes a block for every incoming channel, named after it and holding its value; a new block copies the previous block's settings.
- **Add channels the input lacks**: A block with no matching input channel outputs its own Value, so the bank can add channels.
- **Gain before and after**: Master gain on every channel before the blocks and after them.
- **Replace a Math or Constant CHOP**: Create a Math CHOP or Constant CHOP with the alternatives shortcut held and ChopBank is offered in its place, wired into the same spot.
- **Blocks as properties**: Each block is a property on the node, so Python reads and sets its Value by name.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `chopBank` (Chop Bank) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/ChopBank.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `Chan1` (property): The Value parameter of the block named 'chan1'; assign to set it.
- `Chan1_out` (property): The output of the block named 'chan1': the channel value for a number, else the table cell.
- `CompEditorExt` (attribute)
- `ConsumeParGroup(size: int, previous_size: int)`: Grow the sequence's block size to hold a multi-value Value parameter group of `size` components.
- `IsParGroup` (property): Returns whether the current parameter is a parameter group
- `OnAdd(block_idx: int, prev_name: str = None)`: Create, or rename, the promoted attribute pair of one block; called when a block is added or its Name changes.
- `OnPrefixChanged(old_prefix: str)`: Rebuild the promoted per-block attributes after the Prefix parameter changed from old_prefix.
- `OnTypeChanged(new_type: str)`: Rebuild every block's Value parameter in the new style (Float, Int, RGB, ...); called when the Type parameter changes.
- `OnValChanged(block_idx, _val)`: Called when a block's Value parameter changes; currently a no-op, the dependency update is disabled.
- `ParGroupChannels` (property): Returns a list of channel names for the parameter group, or an empty list if not a parameter group
- `ParGroupSize` (property): Returns the size of the parameter group, or 1 if not a parameter group
- `RefreshAllAttributes(old_prefix: str = None)`: Remove every promoted per-block attribute and create them again from the current blocks (when Promote is on).
- `SeqConst` (property): The sequence of constant blocks this tool manages (the Seqname sequence on the owner).

## Commands

No commands recorded for this package.

## Hotkeys

None.

## Alternative for

- `constantCHOP`
- `mathCHOP`

## Requires

- `FNS_OpMenuRegistry`

## Parameters

### Bank

- **In Scope** (`par.Scope`, Str), default `*`: Which input channels the bank takes, as a pattern like fader* . Only asked when the input has more than one channel.
- **Gain Pre** (`par.Mastergainpre`, Float), default `1.0`: Gain on every input channel before the bank processes it.
- **Gain Post** (`par.Mastergainpost`, Float), default `1.0`: Gain on every output channel after the bank.
- **Snap Input** (`par.Snapinput`, Pulse): Rebuild the bank from the input: one block per channel, named after it and holding its current value.
- **Bank** (`par.Bank`, Sequence), default `0`: One block per channel. Add a block to process one more channel.
- **Name** (`par.Bank0name`, Str): The input channel this block processes, and its output name. Empty takes the channel at this block's position. A name the input does not have makes a new channel from Value.
- **Value** (`par.Bank0value`, Float), default `0.0`: The value this block outputs while no input channel matches it.
- **Math** (`par.Bank0math`, Header)
- **Type** (`par.Bank0type`, Menu), default `off`, menu `off`, `clamp`, `loop`, `zigzag`: What happens outside the From Range: off lets values through, clamp holds them at the ends, loop wraps them round, zigzag bounces them back.
- **From Range** (`par.Bank0fromrange`, Float x2), default `0.0`: The input range. With Type set to clamp, loop or zigzag this is also the limit.
- **To Range** (`par.Bank0torange`, Float x2), default `0.0`: The output range the From Range maps onto.
- **Zero Below** (`par.Bank0zerobelow`, Toggle), default `off`: Output 0 while the input sits at the bottom of the From Range, instead of the bottom of the To Range. Only with Type set to clamp.
- **Exponent Value** (`par.Bank0expval`, Float), default `1.0`: Exponent for the curve between the ranges: 1 is linear, above 1 eases in, below 1 eases out.
- **Lag** (`par.Bank0lag`, Float x2), default `0.0`: Seconds to glide up and down toward a new value.
- **Speed** (`par.Bank0speed1`, Header)
- **Is Speed** (`par.Bank0isspeed`, Toggle), default `off`: Treat the processed value as a speed and output its running total instead, so a held input keeps moving.
- **Limit Type** (`par.Bank0limittype`, Menu), default `off`, menu `off`, `clamp`, `loop`, `zigzag`: What happens when the running total leaves Minimum and Maximum.
- **Minimum** (`par.Bank0min`, Float), default `0.0`: Lower limit for the running total.
- **Maximum** (`par.Bank0max`, Float), default `1.0`: Upper limit for the running total.
- **Reset Value** (`par.Bank0resetvalue`, Float), default `0.0`: The value the running total returns to on reset.
- **Reset** (`par.Bank0reset`, Toggle), default `off`: Hold the running total at the Reset Value while on.
- **Reset Pulse** (`par.Bank0resetpulse`, Pulse): Return the running total to the Reset Value once.

### Common

- **Promote to Property** (`par.Promote`, Toggle), default `on`: Expose each block as a property on this COMP, named after the block, that reads and sets its Value.
- **To get/set values as .{prefix}{name}** (`par.Header`, Header)
- **Property Prefix** (`par.Prefix`, Str), default `C_`: Put in front of every property name, to keep them clear of other names on the COMP.
- **Author: Function Store (@function.str)** (`par.Author`, Header)
