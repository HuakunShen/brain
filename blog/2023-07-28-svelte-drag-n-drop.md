---
title: Svelte Drag and Drop
authors: [huakun]
tags: [Svelte]
---

Here is a Drag and Drop wrapper component I wrote for svelte.
It's important to note that, in order for the drop event to be fired properly, we also need to call `preentDefault()` on the `dragover` event.

```svelte
<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	function onDrop(e: DragEvent) {
		e.preventDefault();
		e.stopPropagation();
		dispatch('drop', e);
	}

	function onDragOver(e: DragEvent) {
		e.preventDefault();
		dispatch('dragover', e);
	}
</script>

<span
	class={$$props.class}
	on:dragenter
	on:drop={onDrop}
	on:dragleave
	on:dragover={onDragOver}
	on:dragend
	on:click
	role="none"
>
	<slot />
</span>

```

To use the component, here is an example. The UI requires tailwind and skeleton library to properly render. Just read the code to get the idea, it's quite simple to use in fact. `DragNDrop` is a wrapper, you need to set the size, and styles for it, then it's region will be file-droppable.

```svelte
<script lang="ts">
	import DragNDrop from './drag-n-drop.svelte';

	function onDrop(e: CustomEvent<DragEvent>) {
		console.log(e.detail.dataTransfer?.files);
	}

	let isOver = false;
	let fileInputEle: HTMLInputElement;
</script>

<DragNDrop
	class="flex flex-col justify-center items-center space-y-6 card {$$props.class} cursor-pointer"
	on:click={() => {
		fileInputEle.click();
	}}
	on:drop={onDrop}
	on:dragleave={() => {
		isOver = false;
	}}
	on:dragenter={() => {
		isOver = true;
	}}
>
	<iconify-icon class="text-6xl" icon="ic:round-upload" />
	{#if isOver}
		<span class="text-lg"><strong>Drop the file</strong></span>
	{:else}
		<span class="text-lg"><strong>Upload a file</strong> or drag and drop</span>
	{/if}
	<input
		type="file"
		class="hidden"
		multiple
		bind:this={fileInputEle}
		on:change={(e) => {
			// console.log(e.target);
		}}
	/>
</DragNDrop>

```