<template>
  <section
  :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"

    class="services w-full my-4 px-4 min-h-screen lg:min-h-full 3xl:min-h-screen flex flex-col justify-center items-center"
    id="services"
  >
    <SectionTitle :title="t('Services')" />

    <div class="flex flex-col w-full my-6 space-y-4 lg:w-4/5 mx-auto">
      <div
        class="services-cards flex flex-col space-y-4 justify-center lg:grid lg:gap-6 justify-items-stretch lg:grid-cols-3 lg:grid-rows-2 lg:space-y-0"
      >
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/dotty/80/FFFFFF/scales.png"
              alt="scales"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.consultation.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              {{ $t("ServicesSection.consultation.content") }}
            </p>
          </div>
        </div>
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/wired/64/FFFFFF/law.png"
              alt="law"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.action.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              {{ $t("ServicesSection.action.content") }}
            </p>
          </div>
        </div>
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/external-justicon-lineal-justicon/64/FFFFFF/external-hand-shake-woman-day-justicon-lineal-justicon.png"
              alt="external-hand-shake-woman-day-justicon-lineal-justicon"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.judgement.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              {{ $t("ServicesSection.judgement.content") }}
            </p>
          </div>
        </div>
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/external-justicon-lineal-justicon/64/FFFFFF/external-hand-shake-woman-day-justicon-lineal-justicon.png"
              alt="external-hand-shake-woman-day-justicon-lineal-justicon"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.settlement.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              {{ $t("ServicesSection.settlement.content1") }}
              <br />
              {{ $t("ServicesSection.settlement.content2") }}
            </p>
          </div>
        </div>
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/external-becris-lineal-becris/64/FFFFFF/external-responsive-job-resume-becris-lineal-becris.png"
              alt="external-responsive-job-resume-becris-lineal-becris"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.counseling.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              <span class="block text-center text-2xl pb-2">
                {{ $t("ServicesSection.counseling.content") }}
              </span>
            </p>
          </div>
        </div>
        <div
          class="serv-card min-h-96 bg-white flex flex-col items-center text-center space-y-4 shadow-sm rounded-lg p-8 duration-300 hover:scale-105 hover:bg-primary hover:text-white"
        >
          <div
            class="serv-card__icon p-4 duration-300 flex items-center justify-center border rounded-full w-16 h-16 bg-primary text-white"
          >
            <img
              width="64"
              height="64"
              src="https://img.icons8.com/ios/50/FFFFFF/light-on--v1.png"
              alt="light-on--v1"
            />
          </div>
          <div class="serv-card_title">
            <h2 class="text-2xl font-bold text-primary">
              {{ $t("ServicesSection.teaching.title") }}
            </h2>
          </div>
          <div class="serv-card_content">
            <p class="text-sm font-light text-justify">
              {{ $t("ServicesSection.teaching.content") }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.serv-card:hover {
  .serv-card__icon {
    color: #354f88;
    background-color: rgb(5, 150, 105);
  }
  .serv-card_title {
    h2 {
      color: white;
    }
  }
}
</style>

<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>
