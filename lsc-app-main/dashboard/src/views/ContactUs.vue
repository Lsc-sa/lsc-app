<template>
  <LoggedInTopNav :title="t('Contact Us')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="p-6 w-full px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
    >
      <h3
        class="text-lg font-bold text-center pb-2 flex flex-col gap-4 justify-center items-center"
      >
        <div
          class="icon flex justify-center items-center bg-primary text-white p-8 w-8 h-8 rounded-full"
        >
          <font-awesome-icon
            icon="fa-solid fa-headphones-simple"
            width="30"
            height="30"
          />
        </div>
        {{ $t("Phone Number") }}
        <a
          class="link link-hover text-primary"
          href="tel:966508062958"
          @click="copyClip"
          >0508062958</a
        >
      </h3>
      <h3
        class="text-lg font-bold text-center pb-2 flex flex-col gap-4 justify-center items-center"
      >
        <div
          class="icon bg-primary flex justify-center items-center text-white p-8 w-8 h-8 rounded-full"
        >
          <font-awesome-icon
            icon="fa-solid fa-message"
            width="30"
            height="30"
          />
        </div>
        {{ $t("Mail Us") }}
        <a
          class="link link-hover text-primary"
          href="mailto: info@lsc-sa.net"
          @click="copyClip"
        >
          info@lsc-sa.net
        </a>
      </h3>
    </div>
  </div>
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import { ref } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import showToastMessage from "../router/toastmessage";
const showToast = ref(false);
const toastMessage = ref(null);

function copyClip(event) {
  const textToCopy = event.target.innerText;

  navigator.clipboard
    .writeText(textToCopy)
    .then(() => {
      showToastMessage(t("Copied to clipboard"), toastMessage, showToast);
    })
    .catch((err) => {
      showToastMessage(
        t("An unexpected error occurred. Please try again later."),
        toastMessage,
        showToast
      );
    });
}
</script>
