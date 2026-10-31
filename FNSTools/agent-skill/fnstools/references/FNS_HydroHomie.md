# HydroHomie

Package `FNS_HydroHomie`.

A toolbar reminder to drink water at an interval you set. Off by default.

- Category: Miscellaneous
- Version: 3.2.11
- Access: Free
- Docs: https://functionstore.tools/docs/fns-hydrohomie/

## What it does

- **Drink water reminder**: A small alert icon pulses on the toolbar at each interval, 45 minutes by default; click it away until the next one.
- **Set your own interval**: Set the minutes between reminders, from the parameters or from quick-launch.
- **Enable at project start**: With On Start Active on, the reminders start as soon as the project opens.
- **Quiet during a show**: While FNSTools Perform Mode is on the reminder neither animates nor pops up.

## Reach it

`op.FNS_HYDROHOMIE` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `Dismiss()`: Hide the reminder and restart its timer while the tool is active.
- `OverlayShown()`: Is the reminder overlay currently visible?
- `SetInterval(minutes: float = 45)`: Set the hydration reminder interval in minutes.
- `Show` (attribute)
- `Toggle()`: Show or hide the hydration reminder overlay.

## Commands

- **Set HydroHomie interval** (id `setinterval`): Set the hydration reminder interval in minutes. Method `SetInterval`. Params: `minutes: float = 45`.
- **Toggle HydroHomie** (id `toggle`): Show or hide the hydration reminder overlay. Method `Toggle`.

## Hotkeys

None.

## Alternative for

None.

## Requires

- `FNS_ConfigRegistry`
- `FNS_ToolbarRegistry`

## Parameters

### Custom

- **Enable** (`par.Active`, Toggle), default `off`: Turn the reminder on. Off by default. With it off the component sits in the toolbar and never interrupts you.
- **Interval minutes** (`par.Intervalminutes`, Float), default `0.0`: Minutes between reminders. 45 by default; the countdown restarts when you click the alert away.
- **LFO Freq** (`par.Lfofreq`, Float), default `0.2`: How fast the alert icon pulses, in Hz. Lower is calmer; this only affects the animation, never the interval.
- **On Start Active** (`par.Onstartactive`, Toggle), default `off`: Start reminding as soon as the project opens, instead of waiting for Enable to be switched on by hand.
