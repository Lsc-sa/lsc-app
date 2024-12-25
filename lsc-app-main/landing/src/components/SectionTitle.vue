<template>
  <div class="title relative pt-6 my-6 w-full text-primary">
    <h2 class="text-4xl font-black text-center">{{ computedTitle }}</h2>
    <h2
      class="text-6xl lg:text-8xl text-nowrap absolute -top-[15%] font-black opacity-10 left-1/2 -translate-x-1/2 text-center"
    >
      {{ computedTitle }}
    </h2>
    <div class="title-lines"></div>
  </div>
</template>

<style scoped>
.title-lines {
  position: absolute;
  top: 120%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20%;
  height: 2px;
  background-color: #354f88;
}
.title-lines::before {
  content: "";
  position: absolute;
  height: 1px;
  width: 70%;
  background-color: #354f88;
  top: -200%;
  left: 50%;
  transform: translateX(-50%);
}
.title-lines::after {
  content: "";
  position: absolute;
  border-top: 20px solid #354f88;
  border-bottom: 20px solid transparent;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  height: 2px;
  width: 2px;
  top: 0%;
  left: 50%;
  transform: translateX(-50%);
}
</style>

<script setup>
import { computed } from "vue";

const props = defineProps({
  title: {
    type: [String, Function],
    required: true,
  },
});

const computedTitle = computed(() => {
  return typeof props.title === "function" ? props.title() : props.title;
});
</script>
