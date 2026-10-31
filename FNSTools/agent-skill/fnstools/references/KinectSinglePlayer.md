# KinectSinglePlayer

Picks one player out of a Kinect skeleton stream: whoever stands inside the bounds you set becomes the active player, and their joints ride out as clean channels until they leave.

- Category: CHOPs & sensing
- Version: 1.0.5
- Access: Base
- Docs: https://functionstore.tools/docs/kinectsingleplayer/

## What it does

- **Select a player by bounds**: Watches a chosen joint of every tracked player and promotes one whose joint sits inside the box you define to active player.
- **Track one player on stable channels**: The active player's joints come out under a stable name, whichever of the six Kinect slots they occupy.
- **Hand over to the next player**: When the active player walks out of the box, the next player in range takes over.
- **Detect whether a player is active**: A separate CHOP output reports whether a player is active right now.
- **Read live or recorded data**: Reads a Kinect CHOP, or any CHOP with Kinect-style channel names such as a recorded take.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `kinectSinglePlayer` (Kinect Single Player) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/KinectSinglePlayer.tox`. Its promoted methods are called on the placed copy.

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

- **Kinect Data** (`par.Kinectdata`, CHOP): Kinect CHOP (or any CHOP with Kinect-style channels such as p1/spine:tx, p1/id) to pick the single player from. Output channels follow the locked template in null1 (TouchDesigner Kinect v2 names with world, depth-space, bone rotation and length channels); input channels outside that set are not passed through.
- **Joint** (`par.Joint`, Str), default `spine`: Kinect joint tested against the bounds, matched as the whole joint name (p<N>/<Joint>:tx/ty/tz), so 'spine' does not also catch 'spine_mid'. TouchDesigner's Kinect CHOP names: hip, spine, neck, head, shoulder_c, shoulder_l/_r, elbow_l/_r, wrist_l/_r, hand_l/_r, hip_l/_r, knee_l/_r, ankle_l/_r, foot_l/_r.
- **X Bounds** (`par.Boundx`, Float x2), default `-0.5`: X range (min, max) in metres, Kinect camera space (0 = straight in front of the sensor). The joint must sit inside it for the player to count as in range.
- **Y Bounds** (`par.Boundy`, Float x2), default `-1.0`: Y range (min, max) in metres, Kinect camera space (0 = sensor height, + = up). The joint must sit inside it for the player to count as in range.
- **Z Bounds** (`par.Boundz`, Float x2), default `1.0`: Z range (min, max) in metres: distance in front of the sensor (Kinect reports 0.5 to about 4.5). The joint must sit inside it for the player to count as in range.
