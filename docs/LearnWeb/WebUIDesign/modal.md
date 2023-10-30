---
title: Modal
---

The easiest way to build a modal is to use the `dialog` html element.

Here is an example of vue code

```vue
<!-- modal.vue -->
<script setup>
const props = defineProps({ open: Boolean });
const emit = defineEmits(["update:open"]);
const dialogRef = ref(null);

watch(
  () => props.open,
  (newVal) => {
    if (newVal) {
      dialogRef.value.showModal();
    } else {
      dialogRef.value.close();
    }
  }
);

onMounted(() => {
  dialogRef.value.addEventListener("click", (e) => {
    const dialogDimensions = dialogRef.value.getBoundingClientRect();
    if (
      e.clientX < dialogDimensions.left ||
      e.clientX > dialogDimensions.right ||
      e.clientY < dialogDimensions.top ||
      e.clientY > dialogDimensions.bottom
    ) {
      emit("update:open", false);
      dialogRef.value.close();
    }
  });
});
</script>
<template>
  <dialog ref="dialogRef">
    <slot />
  </dialog>
</template>

<style scoped>
dialog::backdrop {
  background-color: rgba(50, 50, 50, 0.4);
}
</style>
```

## Usage

```vue
<script setup>
const isOpen = ref(false);
</script>
<template>
  <div>
    <button @click="isOpen = !isOpen">Open</button>
    <Modal v-model:open="isOpen">
      <p>Modal Opened</p>
    </Modal>
  </div>
</template>
```
