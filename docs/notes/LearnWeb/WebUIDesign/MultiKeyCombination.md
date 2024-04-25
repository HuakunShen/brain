# Mulit-Key Combination Detection

Key combination can be easily detected using JS map. Set also works.

In `keydown` event, a key is added to map.

In `keyup` event, a key is removed from map.

Any number of key press at the samed time will be recorded in the map (set).

[Sandbox](https://codesandbox.io/embed/general-multiple-key-press-combination-b575y7?fontsize=14&hidenavigation=1&theme=dark)

<iframe
	src="https://codesandbox.io/embed/general-multiple-key-press-combination-b575y7?fontsize=14&hidenavigation=1&theme=dark"
	width="100%"
    height="500"
	title="General Multiple Key Press Combination"
	allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
	sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
></iframe>

## Shortcut Selection Example (Svelte)

```svelte
<script lang="ts">
  import { cloneDeep } from 'lodash';
  import { onDestroy } from 'svelte';

  function isLetter(letter: string): boolean {
    if (letter.length != 1) return false;
    return letter.match(/[a-zA-Z]/) ? true : false;
  }

  function isShortcut(letters: string[]): boolean {
    if (letters.length <= 1 || letters.length > 3) return false;
    return letters.filter((letter) => isLetter(letter)).length == 1;
  }

  let keyCombination = '';
  let curKeyCombinationArr: string[] = [];
  let keyCombMemo: string[] = [];
  const keyDownMap = new Map();

  const updatePressedKeys = () => {
    console.log('update');

    curKeyCombinationArr = [];
    keyDownMap.forEach((value, key, map) => {
      if (value) curKeyCombinationArr.push(key);
    });
    if (isShortcut(curKeyCombinationArr)) {
      keyCombMemo = cloneDeep(curKeyCombinationArr);
    }
  };

  function onKeyDown(e: KeyboardEvent) {
    keyDownMap.set(e.key, true);
    updatePressedKeys();
  }
  function onKeyUp(e: KeyboardEvent) {
    keyDownMap.delete(e.key);
    updatePressedKeys();
  }

  document.addEventListener('keydown', onKeyDown);
  document.addEventListener('keyup', onKeyUp);
  $: keyCombination = keyCombMemo.join('+');

  onDestroy(() => {
    document.removeEventListener('keydown', onKeyDown);
    document.removeEventListener('keyup', onKeyUp);
  });
</script>

<div>
  <p>Hotkey Select</p>
  <p>{keyCombination}</p>
</div>

```
