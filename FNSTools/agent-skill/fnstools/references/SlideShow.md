# SlideShow

A slideshow of a folder of images and movies: timed or stepped with next and previous, in order or random, moving on when a movie ends, with a crossfade between slides and a fitted output resolution.

- Category: Show & output
- Version: 1.0.7
- Access: Base
- Docs: https://functionstore.tools/docs/slideshow/

## What it does

- **Play a folder of images and movies**: Point it at a folder and it plays the images and movies in it, each fitted to the output resolution.
- **Timed playback**: Period advances the slides by itself, in seconds per slide.
- **Step through slides**: With Period at zero, Next and Prev step through the slides, from a button, a key or a MIDI note.
- **Jump to a slide**: Select goes straight to a slide.
- **Random order**: Random shuffles the order and draws a new shuffle each time the folder has been played through.
- **Crossfade between slides**: Every change crossfades from the old slide to the new one on the out1 TOP.
- **Move on when a movie ends**: Auto-Skip on Done goes to the next slide when a movie reaches its end, without waiting for Period.

## Reach it

No global shortcut. Place a copy: it is the FNS operator family member `slideShow` (Slide Show) on the FNS tab of the OP Create dialog, also at `<user palette>/FNSTools/FNS/SlideShow.tox`. Its promoted methods are called on the placed copy.

## Promoted API

- `OnCycle()`: Advance to the next slide; called by the timer each period.
- `OnMovieDone()`: A movie reached its end (Movies_callbacks): with Auto-Skip on Done, go on.
- `OnNext()`: Show the next slide, and restart the period when one is set.
- `OnPeriod(_val)`: Called when the Period parameter changes: restart the cycle timer, stopped at zero.
- `OnPrev()`: Show the previous slide, and restart the period when one is set.
- `OnRandom(_val)`: Random switched: off continues in order from the slide on screen, on starts a fresh shuffle from here.

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

- **Res** (`par.Res`, XYZW x2), default `0.0`: The output resolution. 1920 by 1080 unless you set it.
- **Folder** (`par.Folder`, Folder): The folder of images to play.
- **Select** (`par.Select`, Int), default `0`: The slide shown now. Next, Prev and the timer set it; set it yourself to jump to a slide.
- **Period** (`par.Period`, Float), default `10.0`: Seconds per slide. 0 stops the timer, so slides change only on Next and Prev.
- **Auto-Skip on Done** (`par.Autoskipondone`, Toggle), default `off`: For movies: go to the next slide when the current movie reaches its end, without waiting for Period. Stills are unaffected.
- **Crossfade Opacity** (`par.Opacity`, Float), default `0.9`: How strongly the previous slide lingers through the crossfade: higher is a longer fade.
- **Random** (`par.Random`, Toggle), default `off`: Shuffle the order, with a new shuffle each time the folder has played through.
- **Next** (`par.Next`, Pulse): Step to the next slide.
- **Prev** (`par.Prev`, Pulse): Step back to the previous slide.
