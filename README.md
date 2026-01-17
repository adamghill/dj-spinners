# dj-spinners 💫

> Pure SVG loading spinners for Django.

## Installation 🤘

1. `uv add dj-spinners` OR `pip install dj-spinners`
2. Add to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS [
    ...
    "dj_spinners",
]
```

3. Use it in your templates

```html
{% load dj_spinners %}

{% spinner '3-dots-bounce' %}
```

![3 dots bounce](https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-bounce.svg)

NOTE: Most spinners are designed to fit within a 24 x 24 dp view box, though some (like bars) may have different aspect ratios. All previews below are scaled to a height of 24px.

## Spinners 🤩
### Rings
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/180-ring-with-bg.svg">180-ring-with-bg</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/180-ring-with-bg.svg" height="24" />
      </td>
      <td>499</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/180-ring.svg">180-ring</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/180-ring.svg" height="24" />
      </td>
      <td>400</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/270-ring-with-bg.svg">270-ring-with-bg</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/270-ring-with-bg.svg" height="24" />
      </td>
      <td>549</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/270-ring.svg">270-ring</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/270-ring.svg" height="24" />
      </td>
      <td>450</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/90-ring-with-bg.svg">90-ring-with-bg</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/90-ring-with-bg.svg" height="24" />
      </td>
      <td>493</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/90-ring-with-gradient.svg">90-ring-with-gradient</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/90-ring-with-gradient.svg" height="24" />
      </td>
      <td>493</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/90-ring.svg">90-ring</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/90-ring.svg" height="24" />
      </td>
      <td>394</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/oval.svg">oval</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/oval.svg" height="24" />
      </td>
      <td>464</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-ring.svg">pulse-ring</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-ring.svg" height="24" />
      </td>
      <td>422</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-rings-2.svg">pulse-rings-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-rings-2.svg" height="24" />
      </td>
      <td>442</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-rings-3.svg">pulse-rings-3</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-rings-3.svg" height="24" />
      </td>
      <td>645</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-rings-multiple.svg">pulse-rings-multiple</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-rings-multiple.svg" height="24" />
      </td>
      <td>649</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/ring-resize.svg">ring-resize</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/ring-resize.svg" height="24" />
      </td>
      <td>597</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/rings.svg">rings</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/rings.svg" height="24" />
      </td>
      <td>1185</td>
   </tr>
</table>
<br />

### Dots
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/12-dots-scale-rotate.svg">12-dots-scale-rotate</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/12-dots-scale-rotate.svg" height="24" />
      </td>
      <td>1435</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-bounce.svg">3-dots-bounce</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-bounce.svg" height="24" />
      </td>
      <td>593</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-fade.svg">3-dots-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-fade.svg" height="24" />
      </td>
      <td>442</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-move.svg">3-dots-move</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-move.svg" height="24" />
      </td>
      <td>571</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-rotate.svg">3-dots-rotate</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-rotate.svg" height="24" />
      </td>
      <td>379</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-scale-middle.svg">3-dots-scale-middle</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-scale-middle.svg" height="24" />
      </td>
      <td>401</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/3-dots-scale.svg">3-dots-scale</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/3-dots-scale.svg" height="24" />
      </td>
      <td>431</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/4-dots-gooey.svg">4-dots-gooey</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/4-dots-gooey.svg" height="24" />
      </td>
      <td>786</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/4-dots-rotate.svg">4-dots-rotate</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/4-dots-rotate.svg" height="24" />
      </td>
      <td>777</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/6-dots-rotate.svg">6-dots-rotate</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/6-dots-rotate.svg" height="24" />
      </td>
      <td>915</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/6-dots-scale-middle.svg">6-dots-scale-middle</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/6-dots-scale-middle.svg" height="24" />
      </td>
      <td>260</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/6-dots-scale.svg">6-dots-scale</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/6-dots-scale.svg" height="24" />
      </td>
      <td>252</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/8-dots-rotate-scale.svg">8-dots-rotate-scale</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/8-dots-rotate-scale.svg" height="24" />
      </td>
      <td>291</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/8-dots-rotate.svg">8-dots-rotate</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/8-dots-rotate.svg" height="24" />
      </td>
      <td>506</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/dot-revolve.svg">dot-revolve</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/dot-revolve.svg" height="24" />
      </td>
      <td>366</td>
   </tr>
</table>
<br />

### Bars
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars-fade.svg">bars-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars-fade.svg" height="24" />
      </td>
      <td>424</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars-rotate-fade.svg">bars-rotate-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars-rotate-fade.svg" height="24" />
      </td>
      <td>942</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars-scale-fade.svg">bars-scale-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars-scale-fade.svg" height="24" />
      </td>
      <td>460</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars-scale-middle.svg">bars-scale-middle</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars-scale-middle.svg" height="24" />
      </td>
      <td>748</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars-scale.svg">bars-scale</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars-scale.svg" height="24" />
      </td>
      <td>742</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bars.svg">bars</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bars.svg" height="24" />
      </td>
      <td>1760</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/horizontal-bar.svg">horizontal-bar</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/horizontal-bar.svg" height="24" />
      </td>
      <td>831</td>
   </tr>
</table>
<br />

### Blocks
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-scale.svg">blocks-scale</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-scale.svg" height="24" />
      </td>
      <td>1074</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-shuffle-2.svg">blocks-shuffle-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-shuffle-2.svg" height="24" />
      </td>
      <td>465</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-shuffle-3.svg">blocks-shuffle-3</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-shuffle-3.svg" height="24" />
      </td>
      <td>568</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-shuffle-4.svg">blocks-shuffle-4</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-shuffle-4.svg" height="24" />
      </td>
      <td>3658</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-shuffle-5.svg">blocks-shuffle-5</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-shuffle-5.svg" height="24" />
      </td>
      <td>3554</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/blocks-wave.svg">blocks-wave</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/blocks-wave.svg" height="24" />
      </td>
      <td>2082</td>
   </tr>
</table>
<br />

### Pulses
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/heart-pulse-2.svg">heart-pulse-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/heart-pulse-2.svg" height="24" />
      </td>
      <td>414</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/heart-pulse-3.svg">heart-pulse-3</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/heart-pulse-3.svg" height="24" />
      </td>
      <td>444</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/heart-pulse.svg">heart-pulse</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/heart-pulse.svg" height="24" />
      </td>
      <td>628</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/hearts.svg">hearts</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/hearts.svg" height="24" />
      </td>
      <td>1183</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-2.svg">pulse-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-2.svg" height="24" />
      </td>
      <td>166</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-3.svg">pulse-3</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-3.svg" height="24" />
      </td>
      <td>166</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse-multiple.svg">pulse-multiple</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse-multiple.svg" height="24" />
      </td>
      <td>170</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pulse.svg">pulse</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pulse.svg" height="24" />
      </td>
      <td>166</td>
   </tr>
</table>
<br />

### Cogs
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog01.svg">cog01</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog01.svg" height="24" />
      </td>
      <td>2461</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog02.svg">cog02</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog02.svg" height="24" />
      </td>
      <td>2693</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog03.svg">cog03</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog03.svg" height="24" />
      </td>
      <td>2948</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog04.svg">cog04</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog04.svg" height="24" />
      </td>
      <td>3956</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog05.svg">cog05</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog05.svg" height="24" />
      </td>
      <td>3359</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog06.svg">cog06</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog06.svg" height="24" />
      </td>
      <td>3387</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog07.svg">cog07</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog07.svg" height="24" />
      </td>
      <td>2050</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog08.svg">cog08</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog08.svg" height="24" />
      </td>
      <td>2197</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog09.svg">cog09</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog09.svg" height="24" />
      </td>
      <td>2255</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog10.svg">cog10</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog10.svg" height="24" />
      </td>
      <td>1520</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog11.svg">cog11</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog11.svg" height="24" />
      </td>
      <td>1652</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog12.svg">cog12</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog12.svg" height="24" />
      </td>
      <td>1524</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog13.svg">cog13</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog13.svg" height="24" />
      </td>
      <td>1400</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog14.svg">cog14</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog14.svg" height="24" />
      </td>
      <td>1497</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog15.svg">cog15</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog15.svg" height="24" />
      </td>
      <td>1393</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog16.svg">cog16</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog16.svg" height="24" />
      </td>
      <td>1512</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog17.svg">cog17</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog17.svg" height="24" />
      </td>
      <td>1359</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog18.svg">cog18</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog18.svg" height="24" />
      </td>
      <td>1267</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog19.svg">cog19</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog19.svg" height="24" />
      </td>
      <td>3328</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog20.svg">cog20</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog20.svg" height="24" />
      </td>
      <td>3552</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog21.svg">cog21</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog21.svg" height="24" />
      </td>
      <td>2576</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog22.svg">cog22</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog22.svg" height="24" />
      </td>
      <td>1387</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog23.svg">cog23</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog23.svg" height="24" />
      </td>
      <td>1387</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/cog24.svg">cog24</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/cog24.svg" height="24" />
      </td>
      <td>1177</td>
   </tr>
</table>
<br />

### Loaders
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader-wifi.svg">loader-wifi</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader-wifi.svg" height="24" />
      </td>
      <td>1340</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader1.svg">loader1</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader1.svg" height="24" />
      </td>
      <td>1499</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader10.svg">loader10</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader10.svg" height="24" />
      </td>
      <td>361</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader2.svg">loader2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader2.svg" height="24" />
      </td>
      <td>696</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader3.svg">loader3</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader3.svg" height="24" />
      </td>
      <td>411</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader4.svg">loader4</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader4.svg" height="24" />
      </td>
      <td>546</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader5.svg">loader5</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader5.svg" height="24" />
      </td>
      <td>667</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader6.svg">loader6</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader6.svg" height="24" />
      </td>
      <td>494</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader7.svg">loader7</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader7.svg" height="24" />
      </td>
      <td>966</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader8.svg">loader8</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader8.svg" height="24" />
      </td>
      <td>944</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/loader9.svg">loader9</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/loader9.svg" height="24" />
      </td>
      <td>710</td>
   </tr>
</table>
<br />

### Other
<table>
   <tr>
      <th>Name</th>
      <th>Preview</th>
      <th>Size in bytes</th>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/audio.svg">audio</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/audio.svg" height="24" />
      </td>
      <td>986</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/ball-triangle.svg">ball-triangle</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/ball-triangle.svg" height="24" />
      </td>
      <td>1116</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/bouncing-ball.svg">bouncing-ball</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/bouncing-ball.svg" height="24" />
      </td>
      <td>413</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/circle-fade.svg">circle-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/circle-fade.svg" height="24" />
      </td>
      <td>2020</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/circles.svg">circles</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/circles.svg" height="24" />
      </td>
      <td>1676</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/clock.svg">clock</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/clock.svg" height="24" />
      </td>
      <td>521</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/eclipse-half.svg">eclipse-half</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/eclipse-half.svg" height="24" />
      </td>
      <td>353</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/eclipse.svg">eclipse</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/eclipse.svg" height="24" />
      </td>
      <td>347</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/gooey-balls-1.svg">gooey-balls-1</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/gooey-balls-1.svg" height="24" />
      </td>
      <td>704</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/gooey-balls-2.svg">gooey-balls-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/gooey-balls-2.svg" height="24" />
      </td>
      <td>963</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/grid.svg">grid</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/grid.svg" height="24" />
      </td>
      <td>1606</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/jump.svg">jump</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/jump.svg" height="24" />
      </td>
      <td>2848</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/pacman.svg">pacman</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/pacman.svg" height="24" />
      </td>
      <td>1560</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/puff.svg">puff</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/puff.svg" height="24" />
      </td>
      <td>955</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/spinner-double.svg">spinner-double</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/spinner-double.svg" height="24" />
      </td>
      <td>2250</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/spinner-multiple-2.svg">spinner-multiple-2</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/spinner-multiple-2.svg" height="24" />
      </td>
      <td>1941</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/spinner-multiple.svg">spinner-multiple</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/spinner-multiple.svg" height="24" />
      </td>
      <td>733</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/spinner.svg">spinner</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/spinner.svg" height="24" />
      </td>
      <td>1100</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/spinning-circles.svg">spinning-circles</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/spinning-circles.svg" height="24" />
      </td>
      <td>1660</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/square.svg">square</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/square.svg" height="24" />
      </td>
      <td>422</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/tadpole.svg">tadpole</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/tadpole.svg" height="24" />
      </td>
      <td>366</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/tail-spin.svg">tail-spin</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/tail-spin.svg" height="24" />
      </td>
      <td>598</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/wifi-fade.svg">wifi-fade</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/wifi-fade.svg" height="24" />
      </td>
      <td>891</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/wifi.svg">wifi</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/wifi.svg" height="24" />
      </td>
      <td>901</td>
   </tr>
   <tr>
      <td><a href="https://github.com/adamghill/dj-spinners/blob/main/src/dj_spinners/assets/svg/wind-toy.svg">wind-toy</a></td>
      <td>
         <img src="https://raw.githubusercontent.com/adamghill/dj-spinners/refs/heads/main/src/dj_spinners/assets/svg/wind-toy.svg" height="24" />
      </td>
      <td>1275</td>
   </tr>
</table>
<br />

2. `just test`

## Inspiration 😍

- All spinners are from [shubhamjain/svg-spinners](https://github.com/shubhamjain/svg-spinners/)
