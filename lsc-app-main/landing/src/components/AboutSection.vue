<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>

<template>
  <section
  :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"

    class="about w-full px-4 min-h-screen lg:min-h-full 3xl:min-h-screen flex flex-col justify-center items-center"
    id="about"
  >
    <SectionTitle :title="t('About')" />
    <div
      class="flex flex-col w-full my-6 gap-4 lg:flex-row lg:space-y-0 lg:w-4/5 mx-auto"
    >
      <div class="about-img lg:w-1/2">
        <img
          class="w-full block rounded-t-2xl lg:rounded-2xl"
          src="../assets/images/work-2.jpg"
          alt=""
        />
      </div>
      <div
        class="about-content bg-white rounded-b-2xl lg:rounded-2xl px-6 py-4 flex flex-col justify-center items-center space-y-4 lg:w-1/2 lg:items-start lg:justify-between"
      >
        <h2 class="text-3xl font-semibold border-b border-primary pb-2">
          {{ $t("AboutSection.title") }}
        </h2>
        <p class="text-justify font-light">
          {{ $t("AboutSection.titleTextp1") }}
          <br />
          {{ $t("AboutSection.titleTextp2") }}
        </p>
        <h2 class="text-3xl font-semibold border-b border-primary pb-2">
          {{ $t("AboutSection.vision") }}
        </h2>
        <p class="text-justify font-light">
          {{ $t("AboutSection.visionText") }}
        </p>
        <h2 class="text-3xl font-semibold border-b border-primary pb-2">
          {{ $t("AboutSection.mission") }}
        </h2>
        <p class="text-justify font-light">
          {{ $t("AboutSection.missionText") }}
        </p>
        <div class="social-links flex gap-4">
          <a href="#">
            <img
              width="25"
              height="25"
              src="https://img.icons8.com/ios/25/FFFFFF/facebook--v1.png"
              alt="facebook--v1"
            />
          </a>
          <a href="#">
            <img
              width="25"
              height="25"
              src="https://img.icons8.com/ios/25/FFFFFF/twitterx--v1.png"
              alt="twitterx--v1"
            />
          </a>
          <a href="#">
            <img
              width="25"
              height="25"
              src="https://img.icons8.com/ios/25/FFFFFF/instagram-new--v1.png"
              alt="instagram-new--v1"
            />
          </a>
          <a href="#">
            <img
              width="25"
              height="25"
              src="https://img.icons8.com/ios/25/FFFFFF/snapchat--v1.png"
              alt="snapchat--v1"
            />
          </a>
        </div>
        <div class="about-cta flex gap-4 items-center">
          <button
            class="btn py-2 px-8 bg-primary border-primary text-white"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("AboutSection.requestService") }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.social-links a {
  padding: 8px;
  border: 1px solid transparent;
  background-color: #354f88;
  border-radius: 8px;
  transition: all 0.3s;
}
.social-links a:hover {
  padding: 8px;
  border: 1px solid #223458;
  background-color: #223458;
  border-radius: 8px;
}
</style>
